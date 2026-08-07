import os

base_lignum = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
base_historias = r'C:\Users\Barra\Documents\HISTORIAS'

covers = {
    'la-piedra-sin-pulir': 'https://i.ibb.co/NdxnWgmS/Portada-de-La-Piedra-sin-Pulir.png',
    'forgotten-sword': 'https://i.ibb.co/5hfYDKFT/Portada-de-Forgotten-Sword.png',
    'sangre-y-cadaveres': 'https://i.ibb.co/MQxMcc6/Portada-de-Sangre-y-Cad-veres.png',
    'marriage-of-the-republic': 'https://i.ibb.co/SXNrFc51/Portada-de-The-Marriage-of-the-Republic.png',
    'getting-to-know': 'https://i.ibb.co/TM63LgTZ/Portada-de-Getting-to-Know.png'
}

def inject_cover_to_index(index_path, cover_url):
    if not os.path.exists(index_path):
        return
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'story-official-cover-img' in content:
        return

    cover_html = f'''
    <div style="text-align: center; margin: 1.5rem 0;">
      <img src="{cover_url}" alt="Portada Oficial" class="story-official-cover-img" style="max-width: 320px; width: 85%; border-radius: 14px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 10px 30px rgba(0,0,0,0.6); transition: transform 0.3s ease;">
    </div>
    '''

    # Place cover after title or hero section
    if '</header>' in content:
        content = content.replace('</header>', f'{cover_html}\n</header>', 1)
    elif '<div class="divider">' in content:
        content = content.replace('<div class="divider">', f'{cover_html}\n<div class="divider">', 1)
    elif '<div class="hub-diamonds">' in content:
        content = content.replace('<div class="hub-diamonds">', f'{cover_html}\n<div class="hub-diamonds">', 1)
    elif '<main' in content:
        pos = content.find('<main')
        end_pos = content.find('>', pos) + 1
        content = content[:end_pos] + '\n' + cover_html + content[end_pos:]

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Injected cover into: {index_path}')

# Inject into UNIVERSO LIGNUM subfolders
for slug, url in covers.items():
    idx = os.path.join(base_lignum, slug, 'index.html')
    inject_cover_to_index(idx, url)

# Inject into HISTORIAS subfolders
historias_map = {
    'HISTORIA - La Piedra sin Pulir': 'https://i.ibb.co/NdxnWgmS/Portada-de-La-Piedra-sin-Pulir.png',
    'HISTORIA - Forgotten Sword/Fichas_Personajes': 'https://i.ibb.co/5hfYDKFT/Portada-de-Forgotten-Sword.png',
    'HISTORIA - Sangre y Cadáveres': 'https://i.ibb.co/MQxMcc6/Portada-de-Sangre-y-Cad-veres.png',
    'HISTORIA - The Marriage of the Republic': 'https://i.ibb.co/SXNrFc51/Portada-de-The-Marriage-of-the-Republic.png',
    'HISTORIA - Getting to Know': 'https://i.ibb.co/TM63LgTZ/Portada-de-Getting-to-Know.png'
}

for folder, url in historias_map.items():
    idx = os.path.join(base_historias, folder, 'index.html')
    inject_cover_to_index(idx, url)

print('Finished adding official story covers to individual story websites!')
