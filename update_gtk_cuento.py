import os

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# 1. Update getting-to-know/index.html
gk_index = os.path.join(base, 'getting-to-know', 'index.html')
if os.path.exists(gk_index):
    with open(gk_index, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c = c.replace('Novela Completa', 'Cuento Completo')
    with open(gk_index, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated getting-to-know/index.html to say Cuento Completo!")

# 2. Update index.html (Master Portal Hub) if needed
master_index = os.path.join(base, 'index.html')
if os.path.exists(master_index):
    with open(master_index, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c = c.replace('novela', 'cuento')
    c = c.replace('Novela', 'Cuento')
    with open(master_index, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated index.html references to Cuento!")

# 3. Update update_literary_tags.py
sc_path = os.path.join(base, 'update_literary_tags.py')
if os.path.exists(sc_path):
    with open(sc_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c = c.replace('Novela Completa', 'Cuento Completo')
    c = c.replace('novela', 'cuento')
    with open(sc_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated update_literary_tags.py to Cuento!")

print("\nDone updating all references of Getting to Know to CUENTO!")
