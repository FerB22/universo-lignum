import os, re

story_dirs = [
    'la-piedra-sin-pulir',
    'forgotten-sword',
    'ruk-el-heroe',
    'sangre-y-cadaveres',
    'marriage-of-the-republic',
    'getting-to-know',
]
base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

for d in story_dirs:
    path = os.path.join(base, d, 'index.html')
    if not os.path.exists(path):
        print(f'MISSING: {path}')
        continue
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    has_back_btn = 'btn-back-to-hub-floating' in content or 'Volver a Historias' in content
    has_ruk_gen = 'ruk_en_creacion.png' in content
    has_title = '<title>' in content
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title_text = title_match.group(1) if title_match else 'NO TITLE'
    has_meta_desc = 'meta name="description"' in content.lower()
    has_lang = 'lang=' in content
    
    print(f'=== {d} ===')
    print(f'  Back button: {has_back_btn}')
    print(f'  Title: {title_text}')
    print(f'  Meta description: {has_meta_desc}')
    print(f'  Lang attr: {has_lang}')
    print(f'  Has old ruk_en_creacion.png ref: {has_ruk_gen}')
    print()

# Also check master hub
hub_path = os.path.join(base, 'index.html')
with open(hub_path, 'r', encoding='utf-8', errors='ignore') as f:
    hub = f.read()
    
hub_title = re.search(r'<title>(.*?)</title>', hub, re.IGNORECASE)
print('=== PORTAL HUB (index.html) ===')
print(f'  Title: {hub_title.group(1) if hub_title else "NO TITLE"}')
print(f'  Meta description: {"meta name=\"description\"" in hub.lower()}')
print(f'  Dead CSS .brand-icon left: {".brand-icon {" in hub}')
print(f'  Href="#" on brand link (stays on page): {"href=\"#\"" in hub}')
print()
