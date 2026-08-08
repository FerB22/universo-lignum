import os, re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
fixes_log = []

def fix_file(path, replacements):
    """Apply a list of (old, new) replacements to a file."""
    if not os.path.exists(path):
        fixes_log.append(f'  [SKIP] Not found: {path}')
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        fixes_log.append(f'  [OK] Fixed: {os.path.relpath(path, base)}')
    else:
        fixes_log.append(f'  [--] No change: {os.path.relpath(path, base)}')

# ════════════════════════════════════════════════
# FIX 1 — Título de pestaña: Getting to Know
# ════════════════════════════════════════════════
print('FIX 1: Título de pestaña Getting to Know...')
fix_file(
    os.path.join(base, 'getting-to-know', 'index.html'),
    [('<title>Getting to Know - Menú Principal</title>',
      '<title>Getting to Know | Universo Lignum</title>')]
)

# ════════════════════════════════════════════════
# FIX 2 — Subtítulo "Selecciona una opción"
# ════════════════════════════════════════════════
print('FIX 2: Subtítulo "Selecciona una opción"...')
fix_file(
    os.path.join(base, 'forgotten-sword', 'index.html'),
    [('<p class="saga-subtitle">Selecciona una opción</p>',
      '<p class="saga-subtitle">Una saga de guerras, mando y sacrificio</p>')]
)
fix_file(
    os.path.join(base, 'getting-to-know', 'index.html'),
    [('<p class="hub-subtitle">Selecciona una opción</p>',
      '<p class="hub-subtitle">Una historia de refugio, confianza y pertenencia</p>')]
)

# ════════════════════════════════════════════════
# FIX 3 — Encabezado <h2>Menú Principal</h2> en Marriage
# ════════════════════════════════════════════════
print('FIX 3: Encabezado "Menú Principal" en Marriage of the Republic...')
fix_file(
    os.path.join(base, 'marriage-of-the-republic', 'index.html'),
    [('<h2 class="hub-title">Menú Principal</h2>',
      '<h2 class="hub-title">The Marriage of the Republic</h2>')]
)

# ════════════════════════════════════════════════
# FIX 4 — Año © 2025 → © 2026
# ════════════════════════════════════════════════
print('FIX 4: Anno (c) 2025 -> (c) 2026...')
files_2025 = [
    os.path.join(base, 'getting-to-know', 'index.html'),
    os.path.join(base, 'getting-to-know', 'getting-to-know.html'),
    os.path.join(base, 'getting-to-know', 'personajes', 'ficha-heya.html'),
    os.path.join(base, 'getting-to-know', 'personajes', 'ficha-amera.html'),
    os.path.join(base, 'getting-to-know', 'personajes', 'ficha-hesis.html'),
    os.path.join(base, 'getting-to-know', 'personajes', 'ficha-lomen.html'),
    os.path.join(base, 'getting-to-know', 'personajes', 'ficha-derk.html'),
]
for fpath in files_2025:
    fix_file(fpath, [('© 2025', '© 2026')])

# ════════════════════════════════════════════════
# FIX 5 — CSS muerto .brand-icon en index.html
# ════════════════════════════════════════════════
print('FIX 5: CSS muerto .brand-icon en portal...')
hub_path = os.path.join(base, 'index.html')
with open(hub_path, 'r', encoding='utf-8') as f:
    hub = f.read()

dead_css = """    .brand-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: radial-gradient(circle, #38BDF8 0%, rgba(0,0,0,0.6) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #38BDF8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }"""
hub_cleaned = hub.replace(dead_css, '')
if hub_cleaned != hub:
    with open(hub_path, 'w', encoding='utf-8') as f:
        f.write(hub_cleaned)
    fixes_log.append('  [OK] Fixed: index.html — removed dead .brand-icon CSS')
else:
    fixes_log.append('  [--] No change: index.html — .brand-icon not found or already removed')

# ════════════════════════════════════════════════
# FIX 6 — href="#" en logo del portal
# ════════════════════════════════════════════════
print('FIX 6: href="#" en logo del portal...')
fix_file(
    hub_path,
    [('<a href="#" class="brand">',
      '<a href="./index.html" class="brand">')]
)

# ════════════════════════════════════════════════
# FIX 7 — "← Volver al Menú Principal" → "← Portada"
# ════════════════════════════════════════════════
print('FIX 7: Botones "← Volver al Menú Principal"...')
story_indexes = [
    'la-piedra-sin-pulir/index.html',
    'forgotten-sword/index.html',
    'ruk-el-heroe/index.html',
    'sangre-y-cadaveres/index.html',
    'getting-to-know/index.html',
    'marriage-of-the-republic/index.html',
]
for rel_path in story_indexes:
    fix_file(
        os.path.join(base, rel_path),
        [('← Volver al Menú Principal', '← Volver al inicio')]
    )
# Also fix "← Menú Principal" variant (sangre y cadáveres)
fix_file(
    os.path.join(base, 'sangre-y-cadaveres', 'index.html'),
    [('← Menú Principal', '← Volver al inicio')]
)
# Also fix "🏠 Menú Principal" button in ruk-el-heroe
fix_file(
    os.path.join(base, 'ruk-el-heroe', 'index.html'),
    [('🏠 Menú Principal', '🏠 Volver al inicio')]
)

# ════════════════════════════════════════════════
# FIX 8 — "Archivo personal" en fichas de Getting to Know
# ════════════════════════════════════════════════
print('FIX 8: "Archivo personal" en fichas de Getting to Know...')
fichas = [
    'getting-to-know/personajes/ficha-heya.html',
    'getting-to-know/personajes/ficha-amera.html',
    'getting-to-know/personajes/ficha-hesis.html',
    'getting-to-know/personajes/ficha-lomen.html',
    'getting-to-know/personajes/ficha-derk.html',
]
for rel_path in fichas:
    fix_file(
        os.path.join(base, rel_path),
        [('Archivo personal · Fernando Barra · ', 'Fernando Barra · ')]
    )

# ════════════════════════════════════════════════
# PRINT SUMMARY
# ════════════════════════════════════════════════
print('\n══════════ RESUMEN ══════════')
for line in fixes_log:
    print(line)
print('══════════ FIN ══════════')
