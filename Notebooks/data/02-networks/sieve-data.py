from json import loads, load, dump
from os import listdir
from re import match
from zipfile import ZipFile
from tqdm import tqdm
from random import randint
  
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
        for link in links:
            self.links.append(register_name(link))
    
    def reduce_links(self):
        self.links = [link for link in self.links if lookup_name(link) in page_map.keys()]
    
    def to_json(self):
        return {
            "name": lookup_name(self.name),
            "links": [
                lookup_name(link) for link in self.links
            ]
        }
        

page_map: dict[str, Page] = {}
page_name_map: dict[int, str] = {}
page_name_reverse_map: dict[str, int]= {}
parts_directory: str = "./Notebooks/data/02-networks/parts/"
graph_directory: str = "./Notebooks/data/02-networks/"
encoding: str = 'utf-8'

def interpret_json_content(content: str):
    for pre_page in content:
        page = Page(**pre_page)
        name: str = lookup_name(page.name).lower()
        if "data" in name or "science" in name:
            page_map[lookup_name(page.name)] = page

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

def dump_graph():
    with open(graph_directory + "/graph.json", "w", encoding=encoding) as file:
        dump([page.to_json() for page in page_map.values() if len(page.links) > 0], file, ensure_ascii=False, indent=4)
    

load_dumped_pages()
for page in page_map.values():
    page.reduce_links()
print(len(page_map))
dump_graph()