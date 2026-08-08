import os
import glob
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
html_files = glob.glob(base + '/**/*.html', recursive=True)

print("=== FIX 1: Puntos finales fuera de las comillas angulares (.» -> ».) ===")
dot_inside_count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace .» with ».
    content_new = re.sub(r'(\w+)\.»', r'\1».', content)
    content_new = re.sub(r'\.»', '».', content_new)

    if content_new != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print(f"  Fixed guillemets in: {os.path.relpath(fpath, base)}")
        dot_inside_count += 1

print(f"Total files fixed for guillemets: {dot_inside_count}\n")


print("=== FIX 2: Desactivar la copia de frases ===")

# Ruk el Héroe
ruk_path = os.path.join(base, 'ruk-el-heroe', 'index.html')
if os.path.exists(ruk_path):
    with open(ruk_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # 1. Remove instruction paragraph
    c = re.sub(r'<p[^>]*>\s*<em>Haz clic en cualquier recuadro de frase.*?</p>', '', c, flags=re.DOTALL)

    # 2. Remove onclick="copyQuote(...)"
    c = re.sub(r'\s*onclick="copyQuote\([^)]*\)"', '', c)

    # 3. Remove copy-hint div
    c = re.sub(r'\s*<div class="copy-hint">.*?</div>', '', c)

    # 4. Change cursor on .quote-card to default
    c = c.replace('cursor: pointer;', 'cursor: default;')

    with open(ruk_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Removed copy features from Ruk el Héroe quotes section.")

# La Piedra sin Pulir
piedra_path = os.path.join(base, 'la-piedra-sin-pulir', 'index.html')
if os.path.exists(piedra_path):
    with open(piedra_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Remove title="Haz clic para copiar..."
    c = re.sub(r'title="Haz clic para copiar[^"]*"', '', c)
    # Remove clipboard copy JS logic inside <script>
    c = re.sub(r'// Copiar citas al hacer clic.*?showToast\([^\)]+\);\s*}\);', '', c, flags=re.DOTALL)
    # Change cursor pointer to default for quote blocks
    c = c.replace('cursor: pointer;', 'cursor: default;')

    with open(piedra_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Removed copy features from La Piedra sin Pulir quotes section.\n")


print("=== FIX 3: Evitar colisión de 'Volver a Historias' con el título de cabecera ===")

if os.path.exists(ruk_path):
    with open(ruk_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Add margin-left to brand-title in app-header
    if '.brand-title {' in c and 'margin-left: 165px;' not in c:
        c = c.replace(
            '.brand-title {',
            '''.brand-title {
            margin-left: 165px;''',
            1
        )

    # Add media query for mobile margin-left
    mobile_css_patch = '''
        @media (max-width: 600px) {
            .app-header .brand-title {
                margin-left: 135px;
                font-size: 1.15rem;
            }
        }
'''
    if '@media (max-width: 600px)' in c and 'margin-left: 135px' not in c:
        c = c.replace('@media (max-width: 600px) {', '@media (max-width: 600px) {\n' + mobile_css_patch, 1)

    with open(ruk_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Added left margin offset to Ruk el Héroe header title to prevent collision with 'Volver a Historias'!")

# Also check other stories to make sure no title collides
for sdir in ['la-piedra-sin-pulir', 'forgotten-sword', 'sangre-y-cadaveres', 'marriage-of-the-republic', 'getting-to-know']:
    sp = os.path.join(base, sdir, 'index.html')
    if not os.path.exists(sp):
        continue
    with open(sp, 'r', encoding='utf-8', errors='ignore') as f:
        sc = f.read()

    # Ensure floating button has clear z-index and spacing
    if '.btn-back-to-hub-floating' in sc:
        # Check if header padding needs margin offset
        if '.app-header' in sc or '.site-header' in sc:
            if 'margin-left: 165px' not in sc and 'padding-left: 175px' not in sc:
                sc = sc.replace('.app-header {', '.app-header {\n            padding-left: 175px;', 1)
                sc = sc.replace('.site-header {', '.site-header {\n            padding-left: 175px;', 1)
                with open(sp, 'w', encoding='utf-8') as f:
                    f.write(sc)
                print(f"  Padded sticky header in {sdir}")

print("\nDone fixing all 3 requested issues!")
