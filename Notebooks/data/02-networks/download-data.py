from concurrent.futures import ThreadPoolExecutor
from urllib import request
from json import loads, dump, load, dumps
from time import time
from os import listdir
from re import match
from zipfile import ZipFile, ZIP_DEFLATED
import os
from tqdm import tqdm
from random import randint

def resolve(name: str):
    _name: str = name.replace(" ", "_")
    if _name in page_map.keys() or ":" in _name:
        return
    page: Page = Page(_name)
    url: str = "https://en.wikipedia.org/w/api.php?action=parse&page=" + _name + "&prop=links&format=json"
    obj = loads(request.urlopen(url).read())
    for link in obj["parse"]["links"]:
        if ':' not in link["*"]:
            page.add_link(link["*"])
    page_map[_name] = page
    new_pages.append(page)
    return page
  
def register_name(name: str) -> int:
    if name in page_name_reverse_map.keys():
        return page_name_reverse_map[name]
    while True:
        id = randint(0, 9223372036854775807)
        if not id in page_name_map.keys():
            page_name_map[id] = name
            page_name_reverse_map[name] = id
            return id

def lookup_name(id: int) -> str:
    return page_name_map[id]  


class Page:
        
    def __init__(self, name:str, links:list[str]=[]):
        self.name:int = register_name(name)
        self.links:list[int] = []
        self._unresolved_pages: list[int] = []
        for link in links:
            self.add_link(link)
    
    def add_link(self, name: str):
        link_id = register_name(name)
        self._unresolved_pages.append(link_id)
        self.links.append(link_id)
    
    def is_resolved(self) -> bool:
        return len(self._unresolved_pages) == 0
    
    def resolve(self):
        if self.is_resolved():
            return
        # print("resolving", str(len(self._unresolved_pages)), "pages in parallel for page", lookup_name(self.name))
        executor = ThreadPoolExecutor(max_workers=500)
        for link in self._unresolved_pages:
            page_name: str = lookup_name(link)
            if not page_name in page_map:
                executor.submit(resolve, page_name)
        executor.shutdown(wait=True)
        self._unresolved_pages.clear()
    
    def json_dict(self):
        links = [lookup_name(id) for id in self.links]
        return {
                    "links": links,
                    "name": lookup_name(self.name)
                }
        

page_map: dict[str, Page] = {}
page_name_map: dict[int, str] = {}
page_name_reverse_map: dict[str, int]= {}
new_pages: list[Page] = []
unresolved_pages: list[Page] = [resolve("Data_science")]
parts_directory: str = "./Notebooks/data/02-networks/parts/"
encoding: str = 'utf-8'
MIN_PAGES_PER_JSON_FILE: int = 5000
JSON_FILES_PER_ZIP: int = 20

def dump_map():
    # print("dumping", str(len(new_pages)), "new pages")
    with open(parts_directory + str(int(time())) + ".json", 'w', encoding=encoding) as file:
        dump([page.json_dict() for page in new_pages], file, ensure_ascii=False, indent=4)
    new_pages.clear()

def compress_parts():
    json_files = [parts_directory + file for file in listdir(parts_directory) if match(r'.+\.json', file)]
    if len(json_files) < JSON_FILES_PER_ZIP:
        return
    if len(json_files) > JSON_FILES_PER_ZIP:
        json_files = json_files[:JSON_FILES_PER_ZIP]
    with ZipFile(parts_directory + str(int(time())) + '.zip', 'w') as archive:
        for file in json_files:
            archive.write(file, compress_type=ZIP_DEFLATED)
    for file in json_files:
        os.remove(file)

def interpret_json_content(content: str):
    for pre_page in content:
        page = Page(**pre_page)
        page_map[page.name] = page

def load_dumped_pages():
    print("loading zip files")
    zip_files = [parts_directory + file for file in listdir(parts_directory) if match(r'.+\.zip', file)]
    for i in tqdm(range(len(zip_files))):
        zip_file = zip_files[i]
        archive = ZipFile(zip_file, 'r')
        for file in archive.namelist():
            if match(r'.+\.json', file):
                try:
                    interpret_json_content(loads(archive.open(file, "r").read()))
                except Exception as exception:
                    print("error while loading file", file)
                    raise exception
                    

    print("loading json_files")
    json_files = [parts_directory + file for file in listdir(parts_directory) if match(r'.+\.json', file)]
    for i in tqdm(range(len(json_files))):
        with open(json_files[i], encoding=encoding) as f:
            interpret_json_content(load(f))

def update_unresolved():
    print("updating unresolved list")
    unresolved_pages.clear()
    for page in page_map.values():
        if not page.is_resolved():
            unresolved_pages.append(page)

load_dumped_pages()
update_unresolved()
while len(unresolved_pages) > 0:
    with tqdm(total=MIN_PAGES_PER_JSON_FILE, unit="page") as progress_bar:
        for page in unresolved_pages:
            pre_count: int = len(new_pages)
            progress_bar.set_postfix({
                "current page": lookup_name(page.name),
                "links of page": len(page.links)
            })
            page.resolve()
            progress_bar.set_description("currently " + str(len(page_name_map.values())) + " pages known")
            progress_bar.update(len(new_pages) - pre_count)
            if len(new_pages) > MIN_PAGES_PER_JSON_FILE:
                dump_map()
                compress_parts()
                break
    update_unresolved()