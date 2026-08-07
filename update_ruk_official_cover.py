import os
import re

ruk_official_url = "https://i.ibb.co/jvP88cKJ/Portada-en-Creaci-n.png"

base_lignum = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
base_historias = r'C:\Users\Barra\Documents\HISTORIAS'

# 1. Update update_master_hub_covers.py
hub_py_path = os.path.join(base_lignum, 'update_master_hub_covers.py')
if os.path.exists(hub_py_path):
    with open(hub_py_path, 'r', encoding='utf-8') as f:
        hub_py_content = f.read()
    hub_py_content = hub_py_content.replace('./ruk-el-heroe/fichas_img/ruk_en_creacion.png', ruk_official_url)
    hub_py_content = hub_py_content.replace('./ruk-el-heroe/fichas_img/ruk.png', ruk_official_url)
    with open(hub_py_path, 'w', encoding='utf-8') as f:
        f.write(hub_py_content)

# 2. Update index.html in UNIVERSO LIGNUM
master_index = os.path.join(base_lignum, 'index.html')
if os.path.exists(master_index):
    with open(master_index, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    idx_content = idx_content.replace('./ruk-el-heroe/fichas_img/ruk_en_creacion.png', ruk_official_url)
    idx_content = idx_content.replace('./ruk-el-heroe/fichas_img/ruk.png', ruk_official_url)
    with open(master_index, 'w', encoding='utf-8') as f:
        f.write(idx_content)

# 3. Update ruk-el-heroe/index.html in UNIVERSO LIGNUM and HISTORIAS
def update_ruk_index(path):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c = c.replace('./fichas_img/ruk_en_creacion.png', ruk_official_url)
    c = c.replace('fichas_img/ruk.png', ruk_official_url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

update_ruk_index(os.path.join(base_lignum, 'ruk-el-heroe', 'index.html'))
update_ruk_index(os.path.join(base_historias, 'HISTORIA - Ruk el Héroe', 'index.html'))

print('Replaced Ruk el Héroe cover image with official URL!')
