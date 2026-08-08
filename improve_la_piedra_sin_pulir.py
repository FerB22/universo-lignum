import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
piedra_path = os.path.join(base, 'la-piedra-sin-pulir', 'index.html')

if os.path.exists(piedra_path):
    with open(piedra_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # 1. Fix .site-header CSS rule
    old_header_css = r'\.site-header\s*\{[^}]*\}'
    new_header_css = '''.site-header {
  width: calc(100% - 24px);
  max-width: 960px;
  margin: 10px auto 25px auto;
  padding: 20px 24px;
  border: 1.5px solid var(--card-border);
  border-radius: 20px;
  background: var(--card-bg);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(12px);
  text-align: center;
  position: sticky;
  top: 10px;
  z-index: 900;
}'''

    c = re.sub(old_header_css, new_header_css, c, count=1)

    # 2. Fix header title left offset to avoid collision with Volver a Historias button
    c = c.replace('.header-title {', '.header-title {\n  margin-left: 140px;', 1)

    # 3. Fix card-opcion CSS: cursor: pointer for interactive cards
    c = c.replace('.card-opcion {\n  background: var(--card-bg);\n  border: 2px solid var(--card-border);\n  border-radius: 16px;\n  padding: 30px 24px;\n  text-align: left;\n  cursor: default;',
                  '.card-opcion {\n  background: var(--card-bg);\n  border: 2px solid var(--card-border);\n  border-radius: 16px;\n  padding: 30px 24px;\n  text-align: left;\n  cursor: pointer;')

    # 4. Replace card 3 with "En proceso de creación" disabled card
    old_card3 = r'<!-- Opción 3: Personajes -->\s*<div class="card-opcion card-personajes".*?</div>\s*</div>'
    new_card3 = '''<!-- Opción 3: Personajes -->
        <div class="card-opcion card-personajes" style="cursor: default; opacity: 0.85;" title="Fichas en proceso de creación">
          <div>
            <span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(16,185,129,0.15); color:var(--color-emerald); border:1px solid rgba(16,185,129,0.3); margin-bottom:0.75rem;">En proceso de creación</span>
            <div class="card-title">
              Linaje & Personajes
            </div>
            <div class="card-desc">
              Las fichas ilustradas y perfiles de los personajes se encuentran en proceso de creación.
            </div>
          </div>
          <div class="card-action" style="color: var(--text-muted);">
            En proceso de creación
          </div>
        </div>'''

    c = re.sub(old_card3, new_card3, c, flags=re.DOTALL)

    # 5. Add badges to Card 1, 2, and 4 for visual symmetry
    if '<div class="card-title">\nHistoria Completa' in c or '<div class="card-title">\n Historia Completa' in c:
        c = re.sub(
            r'(<div class="card-opcion card-historia"[^>]*>\s*<div>)',
            r'\1\n            <span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(255,204,51,0.15); color:var(--color-gold); border:1px solid rgba(255,204,51,0.3); margin-bottom:0.75rem;">Relato Narrativo Original</span>',
            c
        )

    if '<div class="card-title">\nActos Escénicos' in c or '<div class="card-title">\n Actos Escénicos' in c:
        c = re.sub(
            r'(<div class="card-opcion card-actos"[^>]*>\s*<div>)',
            r'\1\n            <span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(239,68,68,0.15); color:var(--color-crimson); border:1px solid rgba(239,68,68,0.3); margin-bottom:0.75rem;">Estructura en 4 Actos</span>',
            c
        )

    if '<div class="card-title">\nReflexión al Lector' in c or '<div class="card-title">\n Reflexión al Lector' in c:
        c = re.sub(
            r'(<div class="card-opcion card-moraleja"[^>]*>\s*<div>)',
            r'\1\n            <span style="display:inline-block; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.2rem 0.55rem; border-radius:9999px; background:rgba(168,85,247,0.15); color:var(--color-purple); border:1px solid rgba(168,85,247,0.3); margin-bottom:0.75rem;">Enseñanzas Universales</span>',
            c
        )

    with open(piedra_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Improved La Piedra sin Pulir page design!")
