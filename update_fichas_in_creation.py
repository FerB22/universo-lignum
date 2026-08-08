import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# 1. Update Ruk el Héroe
ruk_path = os.path.join(base, 'ruk-el-heroe', 'index.html')
if os.path.exists(ruk_path):
    with open(ruk_path, 'r', encoding='utf-8', errors='ignore') as f:
        ruk_content = f.read()

    old_ruk_card = '''<div class="btn-hub-card" onclick="mostrarSeccion('seccion-personajes', 'personajes')">
<div class="hub-icon"></div>
<h3 class="hub-card-title">Fichas de Personajes</h3>
<p class="hub-card-desc">Conoce a Ruk, Kairo, Riav, Ruval, Muvar, Orwin y los valientes defensores.</p>
</div>'''

    new_ruk_card = '''<div class="btn-hub-card" style="cursor: default; opacity: 0.9;" title="Fichas en proceso de creación">
<span style="display:inline-block; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.25rem 0.65rem; border-radius:9999px; background:rgba(212,175,55,0.15); color:#D4AF37; border:1px solid rgba(212,175,55,0.3); margin-bottom:0.6rem;">En proceso de creación</span>
<h3 class="hub-card-title">Fichas de Personajes</h3>
<p class="hub-card-desc">Las fichas ilustradas y perfiles de los personajes se encuentran en proceso de creación.</p>
</div>'''

    if old_ruk_card in ruk_content:
        ruk_content = ruk_content.replace(old_ruk_card, new_ruk_card)
    else:
        # Regex fallback
        ruk_content = re.sub(
            r'<div class="btn-hub-card"[^>]*mostrarSeccion\(\'seccion-personajes\'.*?</div>\s*</div>',
            new_ruk_card,
            ruk_content,
            flags=re.DOTALL
        )

    with open(ruk_path, 'w', encoding='utf-8') as f:
        f.write(ruk_content)
    print("Updated Ruk el Héroe Fichas card!")

# 2. Update Forgotten Sword
fs_path = os.path.join(base, 'forgotten-sword', 'index.html')
if os.path.exists(fs_path):
    with open(fs_path, 'r', encoding='utf-8', errors='ignore') as f:
        fs_content = f.read()

    old_fs_btn = '''<button class="btn-option" onclick="mostrarSeccion('seccion-fichas', 'fichas')">
<span class="btn-icon"></span>
<span>Fichas de Personajes</span>
</button>'''

    new_fs_card = '''<div class="btn-option" style="cursor: default; opacity: 0.9; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 18px 20px;">
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(255,68,68,0.15); color:#FF4444; border:1px solid rgba(255,68,68,0.3);">En proceso de creación</span>
<span style="font-weight: 700; font-size: 1.1rem; color: var(--text-main);">Fichas de Personajes</span>
<span style="font-size: 0.85rem; color: var(--text-muted); font-weight: normal; text-align: center;">Las fichas de los personajes se encuentran en proceso de creación.</span>
</div>'''

    if old_fs_btn in fs_content:
        fs_content = fs_content.replace(old_fs_btn, new_fs_card)
    else:
        fs_content = re.sub(
            r'<button class="btn-option"[^>]*mostrarSeccion\(\'seccion-fichas\'.*?</button>',
            new_fs_card,
            fs_content,
            flags=re.DOTALL
        )

    with open(fs_path, 'w', encoding='utf-8') as f:
        f.write(fs_content)
    print("Updated Forgotten Sword Fichas card!")

# 3. Update Getting to Know
gk_path = os.path.join(base, 'getting-to-know', 'index.html')
if os.path.exists(gk_path):
    with open(gk_path, 'r', encoding='utf-8', errors='ignore') as f:
        gk_content = f.read()

    old_gk_btn = '''<button class="btn-hub-option" onclick="mostrarFichas()">
<span class="btn-icon"></span>
<span>Fichas de Personajes</span>
</button>'''

    new_gk_card = '''<div class="btn-hub-option" style="cursor: default; opacity: 0.9; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 18px 20px;">
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(45,106,79,0.15); color:#2d6a4f; border:1px solid rgba(45,106,79,0.3);">En proceso de creación</span>
<span style="font-weight: 700; font-size: 1.1rem; color: #1b4332;">Fichas de Personajes</span>
<span style="font-size: 0.85rem; color: #2d6a4f; font-weight: normal; text-align: center;">Las fichas de los personajes se encuentran en proceso de creación.</span>
</div>'''

    if old_gk_btn in gk_content:
        gk_content = gk_content.replace(old_gk_btn, new_gk_card)
    else:
        gk_content = re.sub(
            r'<button class="btn-hub-option"[^>]*mostrarFichas\(\).*?</button>',
            new_gk_card,
            gk_content,
            flags=re.DOTALL
        )

    with open(gk_path, 'w', encoding='utf-8') as f:
        f.write(gk_content)
    print("Updated Getting to Know Fichas card!")

# 4. Update Marriage of the Republic
mar_path = os.path.join(base, 'marriage-of-the-republic', 'index.html')
if os.path.exists(mar_path):
    with open(mar_path, 'r', encoding='utf-8', errors='ignore') as f:
        mar_content = f.read()

    old_mar_card = '''<!-- Card 3: Fichas de Personajes -->
 <a href="#personajes" class="hub-card" data-target="personajes">
 <div>
 <div class="hub-card-icon"></div>
 <h3 class="hub-card-title">Fichas de Personajes</h3>
 <p class="hub-card-desc">Galería de personajes principales de la obra (próximamente).</p>
 </div>
 <div class="hub-card-footer">
 <span>Ver Apartado</span>
 <span class="hub-card-arrow">→</span>
 </div>
 </a>'''

    new_mar_card = '''<!-- Card 3: Fichas de Personajes -->
 <div class="hub-card" style="cursor: default; opacity: 0.9;">
 <div>
 <span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(139,90,43,0.15); color:#8B5A2B; border:1px solid rgba(139,90,43,0.3); margin-bottom:0.5rem;">En proceso de creación</span>
 <h3 class="hub-card-title">Fichas de Personajes</h3>
 <p class="hub-card-desc">Las fichas de los personajes se encuentran en proceso de creación.</p>
 </div>
 <div class="hub-card-footer">
 <span>En proceso de creación</span>
 </div>
 </div>'''

    if old_mar_card in mar_content:
        mar_content = mar_content.replace(old_mar_card, new_mar_card)
    else:
        mar_content = re.sub(
            r'<!-- Card 3: Fichas de Personajes -->\s*<a href="#personajes".*?</a>',
            new_mar_card,
            mar_content,
            flags=re.DOTALL
        )

    with open(mar_path, 'w', encoding='utf-8') as f:
        f.write(mar_content)
    print("Updated Marriage of the Republic Fichas card!")

