import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# 1. Fix Ruk el Héroe grid cards symmetry and badges
ruk_path = os.path.join(base, 'ruk-el-heroe', 'index.html')
if os.path.exists(ruk_path):
    with open(ruk_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Replace grid HTML with perfectly symmetric, badge-styled cards
    old_grid_pattern = r'<div class="hub-grid">.*?</div>\s*</main>'
    
    new_grid_html = '''<div class="hub-grid">
            <div class="btn-hub-card" onclick="mostrarSeccion('seccion-lectura', 'lectura')">
                <span style="display:inline-block; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.25rem 0.65rem; border-radius:9999px; background:rgba(212,175,55,0.15); color:#D4AF37; border:1px solid rgba(212,175,55,0.3); margin-bottom:0.6rem;">Saga de 9 Capítulos</span>
                <h3 class="hub-card-title">Lectura de Capítulos</h3>
                <p class="hub-card-desc">Explora la saga completa desde el Capítulo 1 hasta el 9 con controles de lectura personalizados.</p>
            </div>

            <div class="btn-hub-card" style="cursor: default; opacity: 0.9;" title="Fichas en proceso de creación">
                <span style="display:inline-block; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.25rem 0.65rem; border-radius:9999px; background:rgba(212,175,55,0.15); color:#D4AF37; border:1px solid rgba(212,175,55,0.3); margin-bottom:0.6rem;">En proceso de creación</span>
                <h3 class="hub-card-title">Fichas de Personajes</h3>
                <p class="hub-card-desc">Las fichas ilustradas y perfiles de los personajes se encuentran en proceso de creación.</p>
            </div>

            <div class="btn-hub-card" onclick="mostrarSeccion('seccion-actos', 'actos')">
                <span style="display:inline-block; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.25rem 0.65rem; border-radius:9999px; background:rgba(212,175,55,0.15); color:#D4AF37; border:1px solid rgba(212,175,55,0.3); margin-bottom:0.6rem;">Cronología Escénica</span>
                <h3 class="hub-card-title">Estructura en Actos</h3>
                <p class="hub-card-desc">Recorre la cronología escénica del ascenso de los héroes y las batallas decisivas.</p>
            </div>

            <div class="btn-hub-card" onclick="mostrarSeccion('seccion-moraleja', 'citas')">
                <span style="display:inline-block; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.25rem 0.65rem; border-radius:9999px; background:rgba(212,175,55,0.15); color:#D4AF37; border:1px solid rgba(212,175,55,0.3); margin-bottom:0.6rem;">Frases Célebres</span>
                <h3 class="hub-card-title">Citas y Reflexiones</h3>
                <p class="hub-card-desc">Descubre las frases célebres de la historia y sus reflexiones principales.</p>
            </div>
        </div>
        </main>'''

    c = re.sub(old_grid_pattern, new_grid_html, c, flags=re.DOTALL)

    # Clean out any leftover empty hub-icon CSS rule or empty divs
    c = re.sub(r'<div class="hub-icon">\s*</div>', '', c)

    with open(ruk_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed cards in Ruk el Héroe!")


# 2. Fix Forgotten Sword
fs_path = os.path.join(base, 'forgotten-sword', 'index.html')
if os.path.exists(fs_path):
    with open(fs_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Remove empty btn-icon
    c = c.replace('<span class="btn-icon"></span>', '')

    new_fs_btn = '''<a href="capitulos.html" class="btn-option" style="text-decoration: none; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 18px 20px;">
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(255,68,68,0.15); color:#FF4444; border:1px solid rgba(255,68,68,0.3);">Saga de 15 Capítulos</span>
<span style="font-weight: 700; font-size: 1.1rem; color: var(--text-main);">Lista de Capítulos</span>
<span style="font-size: 0.85rem; color: var(--text-muted); font-weight: normal; text-align: center;">Accede a la lectura de los 15 capítulos redactados.</span>
</a>'''

    c = re.sub(r'<button class="btn-option"[^>]*mostrarSeccion\(\'seccion-capitulos\'.*?</button>', new_fs_btn, c, flags=re.DOTALL)
    c = re.sub(r'<a href="capitulos.html" class="btn-option".*?</a>', new_fs_btn, c, flags=re.DOTALL)

    with open(fs_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed cards in Forgotten Sword!")


# 3. Fix Getting to Know
gk_path = os.path.join(base, 'getting-to-know', 'index.html')
if os.path.exists(gk_path):
    with open(gk_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    c = c.replace('<span class="btn-icon"></span>', '')

    new_gk_btn = '''<a href="getting-to-know.html" class="btn-hub-option" style="text-decoration: none; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 18px 20px;">
<span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(45,106,79,0.15); color:#2d6a4f; border:1px solid rgba(45,106,79,0.3);">Novela Completa</span>
<span style="font-weight: 700; font-size: 1.1rem; color: #1b4332;">Lista de Capítulos</span>
<span style="font-size: 0.85rem; color: #2d6a4f; font-weight: normal; text-align: center;">Accede a la lectura completa de la obra.</span>
</a>'''

    c = re.sub(r'<a href="getting-to-know.html" class="btn-hub-option".*?</a>', new_gk_btn, c, flags=re.DOTALL)

    with open(gk_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed cards in Getting to Know!")


# 4. Fix Marriage of the Republic and La Piedra sin Pulir empty icon divs
for rel in ['marriage-of-the-republic/index.html', 'la-piedra-sin-pulir/index.html']:
    p = os.path.join(base, rel)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        c = re.sub(r'<div class="(hub-card-icon|card-icon)">\s*</div>', '', c)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Cleaned empty icon divs in {rel}")

print("\nDone fixing card symmetry and empty icon spaces!")
