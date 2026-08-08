import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

stories_info = {
    'ruk-el-heroe': {
        'cover_url': 'https://i.ibb.co/jvP88cKJ/Portada-en-Creaci-n.png',
        'alt': 'Portada de Ruk el Héroe',
        'border': 'rgba(212,175,55,0.4)',
    },
    'la-piedra-sin-pulir': {
        'cover_url': 'https://i.ibb.co/NdxnWgmS/Portada-de-La-Piedra-sin-Pulir.png',
        'alt': 'Portada de La Piedra sin Pulir',
        'border': 'rgba(255,204,51,0.4)',
    },
    'forgotten-sword': {
        'cover_url': 'https://i.ibb.co/5hfYDKFT/Portada-de-Forgotten-Sword.png',
        'alt': 'Portada de Forgotten Sword',
        'border': 'rgba(255,68,68,0.4)',
    },
    'sangre-y-cadaveres': {
        'cover_url': 'https://i.ibb.co/MQxMcc6/Portada-de-Sangre-y-Cad-veres.png',
        'alt': 'Portada de Sangre y Cadáveres',
        'border': 'rgba(202,11,11,0.4)',
    },
    'marriage-of-the-republic': {
        'cover_url': 'https://i.ibb.co/SXNrFc51/Portada-de-The-Marriage-of-the-Republic.png',
        'alt': 'Portada de The Marriage of the Republic',
        'border': 'rgba(139,90,43,0.4)',
    },
}

for story_dir, info in stories_info.items():
    fpath = os.path.join(base, story_dir, 'index.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Clean out ALL cover image divs from inside <header>...</header>
    def clean_header(match):
        header_text = match.group(0)
        # Remove story-official-cover-img or story-cover-hero divs
        cleaned = re.sub(r'<div[^>]*story-official-cover-img[^>]*>.*?</div>', '', header_text, flags=re.DOTALL)
        cleaned = re.sub(r'<div[^>]*story-cover-hero[^>]*>.*?</div>', '', cleaned, flags=re.DOTALL)
        cleaned = re.sub(r'<div style="text-align: center; margin: 1\.5rem 0;">.*?</div>', '', cleaned, flags=re.DOTALL)
        return cleaned

    content = re.sub(r'<header.*?</header>', clean_header, content, flags=re.DOTALL)

    # 2. Also ensure no duplicate cover HTML exists in body
    content = re.sub(r'<div class="story-cover-hero".*?</div>', '', content, flags=re.DOTALL)

    # 3. Create responsive cover block (max-width 240px, width 60%, responsive height auto)
    cover_block = f'''
    <div class="story-cover-hero" style="text-align: center; margin: 1.25rem 0;">
      <img src="{info['cover_url']}" alt="{info['alt']}" style="max-width: 240px; width: 65%; height: auto; border-radius: 12px; border: 2px solid {info['border']}; box-shadow: 0 8px 25px rgba(0,0,0,0.5); display: inline-block;">
    </div>'''

    # 4. Insert cover into main hero container
    if story_dir == 'ruk-el-heroe':
        # Adjust app-header padding to be compact & responsive
        content = content.replace('padding: 20px 30px;', 'padding: 12px 24px;')
        if '<div class="hero-emblem">' in content:
            content = content.replace('<div class="hero-emblem">⚔️</div>', f'<div class="hero-emblem">⚔️</div>\n{cover_block}', 1)
        elif '<h1 class="hero-title">' in content:
            content = content.replace('<h1 class="hero-title">', f'{cover_block}\n<h1 class="hero-title">', 1)

    elif story_dir == 'la-piedra-sin-pulir':
        if '<h1 class="hero-title">' in content:
            content = content.replace('<h1 class="hero-title">', f'{cover_block}\n<h1 class="hero-title">', 1)
        elif '<main' in content:
            p = content.find('<main')
            ep = content.find('>', p) + 1
            content = content[:ep] + f'\n{cover_block}' + content[ep:]

    elif story_dir == 'forgotten-sword':
        if '<h1 class="saga-title">' in content:
            content = content.replace('<h1 class="saga-title">', f'{cover_block}\n<h1 class="saga-title">', 1)
        elif '<h2 class="saga-title">' in content:
            content = content.replace('<h2 class="saga-title">', f'{cover_block}\n<h2 class="saga-title">', 1)

    elif story_dir == 'sangre-y-cadaveres':
        if '<h1 class="main-title">' in content:
            content = content.replace('<h1 class="main-title">', f'<h1 class="main-title">\n{cover_block}', 1)
        elif '<p class="main-subtitle">' in content:
            content = content.replace('<p class="main-subtitle">', f'{cover_block}\n<p class="main-subtitle">', 1)

    elif story_dir == 'marriage-of-the-republic':
        if '<h2 class="hub-title">' in content:
            content = content.replace('<h2 class="hub-title">', f'<h2 class="hub-title">\n{cover_block}', 1)
        elif '<h1 class="hero-title">' in content:
            content = content.replace('<h1 class="hero-title">', f'{cover_block}\n<h1 class="hero-title">', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned header and placed responsive cover in {story_dir}")

