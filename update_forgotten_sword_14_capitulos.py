import os
import glob
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# 1. Update index.html (Master Portal Hub)
master_index = os.path.join(base, 'index.html')
if os.path.exists(master_index):
    with open(master_index, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Replace description 15 capítulos -> 14 capítulos
    c = c.replace('Saga épica de 15 capítulos.', 'Saga épica de 14 capítulos.')

    # Replace feature tags
    old_tags = '''          <div class="card-features">
            <span class="feat-tag">Saga de 15 Capítulos</span>
            <span class="feat-tag">Guerras Tribales</span>
            <span class="feat-tag">Responsabilidad del Mando</span>
            <span class="feat-tag">Prólogo & Fichas</span>
          </div>'''

    new_tags = '''          <div class="card-features">
            <span class="feat-tag">Saga de 14 Capítulos</span>
            <span class="feat-tag" style="color: #FF4444; border-color: rgba(255, 68, 68, 0.4); background: rgba(255, 68, 68, 0.12); font-weight: 700;">Capítulo 14 en proceso de escritura</span>
            <span class="feat-tag">Guerras Tribales</span>
            <span class="feat-tag">Responsabilidad del Mando</span>
          </div>'''

    if old_tags in c:
        c = c.replace(old_tags, new_tags)
    else:
        c = c.replace('<span class="feat-tag">Saga de 15 Capítulos</span>', '<span class="feat-tag">Saga de 14 Capítulos</span>\n            <span class="feat-tag" style="color: #FF4444; border-color: rgba(255, 68, 68, 0.4); background: rgba(255, 68, 68, 0.12); font-weight: 700;">Capítulo 14 en proceso de escritura</span>')

    with open(master_index, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated Forgotten Sword card on master index.html!")

# 2. Update forgotten-sword/index.html
fs_index = os.path.join(base, 'forgotten-sword', 'index.html')
if os.path.exists(fs_index):
    with open(fs_index, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    c = c.replace('Saga de 15 Capítulos', 'Saga de 14 Capítulos')
    c = c.replace('Saga de 15 capítulos', 'Saga de 14 capítulos')
    c = c.replace('15 capítulos', '14 capítulos')

    old_fs_card = '''<a href="capitulos.html" class="btn-option" style="text-decoration: none; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 18px 20px;">
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(255,68,68,0.15); color:#FF4444; border:1px solid rgba(255,68,68,0.3);">Saga de 14 Capítulos</span>
<span style="font-weight: 700; font-size: 1.1rem; color: var(--text-main);">Lista de Capítulos</span>
<span style="font-size: 0.85rem; color: var(--text-muted); font-weight: normal; text-align: center;">Accede a la lectura de los 15 capítulos redactados.</span>
</a>'''

    new_fs_card = '''<a href="capitulos.html" class="btn-option" style="text-decoration: none; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 18px 20px;">
<div style="display:flex; gap:6px; flex-wrap:wrap; justify-content:center;">
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(255,68,68,0.15); color:#FF4444; border:1px solid rgba(255,68,68,0.3);">Saga de 14 Capítulos</span>
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(239,68,68,0.2); color:#FF4444; border:1px solid rgba(239,68,68,0.5);">Capítulo 14 en proceso de escritura</span>
</div>
<span style="font-weight: 700; font-size: 1.1rem; color: var(--text-main); margin-top: 4px;">Lista de Capítulos</span>
<span style="font-size: 0.85rem; color: var(--text-muted); font-weight: normal; text-align: center;">Accede a la lectura de los 14 capítulos (Capítulo 14 en proceso de escritura).</span>
</a>'''

    if old_fs_card in c:
        c = c.replace(old_fs_card, new_fs_card)
    else:
        c = c.replace('Accede a la lectura de los 15 capítulos redactados.', 'Accede a la lectura de los 14 capítulos (Capítulo 14 en proceso de escritura).')

    with open(fs_index, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated forgotten-sword/index.html!")

# 3. Update forgotten-sword/capitulos.html
fs_capitulos = os.path.join(base, 'forgotten-sword', 'capitulos.html')
if os.path.exists(fs_capitulos):
    with open(fs_capitulos, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    old_ch14_card = '''<div class="tarjeta-capitulo" style="opacity:0.75; cursor:default; border:1px dashed #8c6d31; background:rgba(28,19,12,0.65); pointer-events:none; user-select:none;">
<div style="display:flex; justify-content:space-between; align-items:center;">
<span style="font-size:10px; color:#9e8237; font-family:\'Cinzel\',serif; letter-spacing:2px;">CAPÍTULO 14</span>
<span style="font-size:9px; color:#d4af37; font-family:\'Cinzel\',serif; letter-spacing:1px; background:rgba(212,175,55,0.12); border:1px solid rgba(212,175,55,0.3); padding:1px 6px; border-radius:4px; text-transform:uppercase;">En proceso</span>
</div>
<p style="margin:4px 0 0 0; font-size:14px; color:#c4b296; font-weight:600; line-height:1.3;">El renacer de la paz</p>
<span style="font-size:11px; color:#a89274; font-style:italic; display:block; margin-top:3px;">En proceso de finalización</span>
</div>'''

    new_ch14_card = '''<div class="tarjeta-capitulo" style="opacity:0.9; cursor:default; border:1px dashed #EF4444; background:rgba(239,68,68,0.1); pointer-events:none; user-select:none;">
<div style="display:flex; justify-content:space-between; align-items:center;">
<span style="font-size:10px; color:#FF6666; font-family:\'Cinzel\',serif; letter-spacing:2px; font-weight:700;">CAPÍTULO 14</span>
<span style="font-size:9px; color:#FF4444; font-family:\'Cinzel\',serif; letter-spacing:1px; background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.5); padding:2px 8px; border-radius:4px; text-transform:uppercase; font-weight:700;">En proceso de escritura</span>
</div>
<p style="margin:4px 0 0 0; font-size:14px; color:#FFCCCC; font-weight:600; line-height:1.3;">El renacer de la paz</p>
<span style="font-size:11px; color:#FF8888; font-style:italic; display:block; margin-top:3px;">Capítulo 14 en proceso de escritura</span>
</div>'''

    if old_ch14_card in c:
        c = c.replace(old_ch14_card, new_ch14_card)

    c = c.replace('15 capítulos', '14 capítulos')

    with open(fs_capitulos, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated forgotten-sword/capitulos.html with red Chapter 14 tag!")

# 4. Update generator python scripts
for script in ['update_master_hub_covers.py', 'update_literary_tags.py', 'fix_card_icons_and_badges.py']:
    sp = os.path.join(base, script)
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8', errors='ignore') as f:
            sc = f.read()
        sc = sc.replace('Saga de 15 Capítulos', 'Saga de 14 Capítulos')
        sc = sc.replace('15 capítulos', '14 capítulos')
        sc = sc.replace('15 Capítulos', '14 Capítulos')
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(sc)

print("\nDone updating all 15 -> 14 chapter references and adding red Chapter 14 tag!")
