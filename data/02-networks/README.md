# Abhängigkeiten
Die Datei graph.json wird sowohl von den Notebooks 02-networks und 04_Ex4 verwendet.

Die Datei download-data.py und sieve-data.py verwenden Python. Python3, Pip und python3.12-venv können per apt mit
```bash
sudo apt install pip python3 python3.12-venv
```
installiert werden. In download-data.py wird tqdm verwendet. Dazu wurde zuerst eine [venv](https://python.land/virtual-environments/virtualenv) erstellt
```bash
python3 -m venv venv
```
Die Environment wird mit
```bash
source venv/bin/activate
```
aktiviert und mit 
```bash
deactivate
```
deaktiviert werden. In dieser Environment kann man ein Paket installieren mit
```bash
pip install tqdm
```
Innerhalb der venv können die Skripte ausgeführt werden, um a) die Wikipedia Daten herunterzuladen und b) die Datei graph.json zu generieren. Dieser Prozess dauert möglicherweise mehrere Tage, weil versucht wird Metadaten der gesamten englischsprachigen Wikipedia herunterzuladen!