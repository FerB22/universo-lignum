import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

def fix_story_cover(rel_path, cover_url, alt_text, border_color):
    path = os.path.join(base, rel_path, 'index.html')
    if not os.path.exists(path):
        print(f"Skipping {rel_path}: file not found")
        return

    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Remove cover div from inside <header>...</header>
    # Regex to match the injected cover div inside header or anywhere before main
    pattern_header_img = r'<div style="text-align: center; margin: 1\.5rem 0;"><img src="[^"]+"[^>]*></div>'
    content_clean = re.sub(pattern_header_img, '', content)

    # 2. Prepare clean cover HTML block
    cover_html = f'''
    <div class="story-cover-hero" style="text-align: center; margin: 1.5rem 0;">
        <img src="{cover_url}" alt="{alt_text}" style="max-width: 260px; width: 75%; height: auto; border-radius: 14px; border: 2px solid {border_color}; box-shadow: 0 10px 28px rgba(0,0,0,0.4); transition: transform 0.3s ease;">
    </div>'''

    # 3. Insert into the main hero area depending on story structure
    if rel_path == 'ruk-el-heroe':
        # Insert inside .hero-banner after .hero-emblem
        if '<div class="hero-emblem">' in content_clean:
            content_clean = content_clean.replace('<div class="hero-emblem">⚔️</div>', f'<div class="hero-emblem">⚔️</div>\n{cover_html}', 1)
        elif '<h1 class="hero-title">' in content_clean:
            content_clean = content_clean.replace('<h1 class="hero-title">', f'{cover_html}\n<h1 class="hero-title">', 1)

    elif rel_path == 'la-piedra-sin-pulir':
        # Insert in main container hero card
        if '<h1 class="hero-title">' in content_clean:
            content_clean = content_clean.replace('<h1 class="hero-title">', f'{cover_html}\n<h1 class="hero-title">', 1)
        elif '<main' in content_clean:
            pos = content_clean.find('<main')
            end_pos = content_clean.find('>', pos) + 1
            content_clean = content_clean[:end_pos] + f'\n{cover_html}' + content_clean[end_pos:]

    elif rel_path == 'forgotten-sword':
        # Insert inside hero banner
        if '<p class="saga-subtitle">' in content_clean:
            pos = content_clean.find('</p>', content_clean.find('<p class="saga-subtitle">')) + 4
            content_clean = content_clean[:pos] + f'\n{cover_html}' + content_clean[pos:]

    elif rel_path == 'sangre-y-cadaveres':
        if '<h1' in content_clean:
            pos = content_clean.find('</h1>', content_clean.find('<h1')) + 5
            content_clean = content_clean[:pos] + f'\n{cover_html}' + content_clean[pos:]

    elif rel_path == 'marriage-of-the-republic':
        if '<h2 class="hub-title">' in content_clean:
            pos = content_clean.find('</h2>', content_clean.find('<h2 class="hub-title">')) + 5
            content_clean = content_clean[:pos] + f'\n{cover_html}' + content_clean[pos:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content_clean)

    print(f"Successfully repositioned cover in {rel_path}!")

# Apply to all 5 stories that had header covers
fix_story_cover('ruk-el-heroe', 'https://i.ibb.co/jvP88cKJ/Portada-en-Creaci-n.png', 'Portada de Ruk el Héroe', 'rgba(212,175,55,0.5)')
fix_story_cover('la-piedra-sin-pulir', 'https://i.ibb.co/NdxnWgmS/Portada-de-La-Piedra-sin-Pulir.png', 'Portada de La Piedra sin Pulir', 'rgba(255,204,51,0.5)')
fix_story_cover('forgotten-sword', 'https://i.ibb.co/5hfYDKFT/Portada-de-Forgotten-Sword.png', 'Portada de Forgotten Sword', 'rgba(255,68,68,0.5)')
fix_story_cover('sangre-y-cadaveres', 'https://i.ibb.co/MQxMcc6/Portada-de-Sangre-y-Cad-veres.png', 'Portada de Sangre y Cadáveres', 'rgba(202,11,11,0.5)')
fix_story_cover('marriage-of-the-republic', 'https://i.ibb.co/SXNrFc51/Portada-de-The-Marriage-of-the-Republic.png', 'Portada de The Marriage of the Republic', 'rgba(139,90,43,0.5)')

