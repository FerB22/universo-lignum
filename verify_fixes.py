import os

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# Verify all audit fixes are actually in place
print('=== VERIFICACION FINAL DE TODOS LOS FIXES ===\n')

# Fix 1: Title
gk_idx = open(os.path.join(base, 'getting-to-know', 'index.html'), encoding='utf-8', errors='replace').read()
print('FIX 1 (titulo pestaña GTK):', 'OK' if 'Getting to Know | Universo Lignum' in gk_idx else 'FALTA')

# Fix 2: Subtitulo
fs = open(os.path.join(base, 'forgotten-sword', 'index.html'), encoding='utf-8', errors='replace').read()
print('FIX 2a (subtitle Forgotten Sword):', 'OK' if 'Selecciona una' not in fs else 'FALTA')
print('FIX 2b (subtitle Getting to Know):', 'OK' if 'Selecciona una' not in gk_idx else 'FALTA')

# Fix 3: Marriage h2
mar = open(os.path.join(base, 'marriage-of-the-republic', 'index.html'), encoding='utf-8', errors='replace').read()
print('FIX 3 (marriage h2):', 'OK' if '<h2 class="hub-title">The Marriage of the Republic</h2>' in mar else 'FALTA')

# Fix 4: Año 2026
gk_footer = open(os.path.join(base, 'getting-to-know', 'getting-to-know.html'), encoding='utf-8', errors='replace').read()
print('FIX 4a (GTK footer year):', 'OK' if '2025' not in gk_footer else 'FALTA - 2025 still found')
ficha_heya = open(os.path.join(base, 'getting-to-know', 'personajes', 'ficha-heya.html'), encoding='utf-8', errors='replace').read()
print('FIX 4b (ficha-heya year):', 'OK' if '2025' not in ficha_heya else 'FALTA - 2025 still found')

# Fix 5: Dead CSS
hub = open(os.path.join(base, 'index.html'), encoding='utf-8', errors='replace').read()
print('FIX 5 (dead CSS brand-icon):', 'OK' if '.brand-icon {' not in hub else 'FALTA')

# Fix 6: href
print('FIX 6 (href logo portal):', 'OK' if 'href="./index.html" class="brand"' in hub else 'FALTA')

# Fix 7: Volver al Menu Principal
stories = {
    'la-piedra-sin-pulir': open(os.path.join(base, 'la-piedra-sin-pulir', 'index.html'), encoding='utf-8', errors='replace').read(),
    'forgotten-sword': fs,
    'ruk-el-heroe': open(os.path.join(base, 'ruk-el-heroe', 'index.html'), encoding='utf-8', errors='replace').read(),
    'sangre-y-cadaveres': open(os.path.join(base, 'sangre-y-cadaveres', 'index.html'), encoding='utf-8', errors='replace').read(),
    'getting-to-know': gk_idx,
    'marriage': mar,
}
all_ok = True
for name, content in stories.items():
    if 'Volver al Men' in content:
        print(f'FIX 7 ({name}): FALTA - "Volver al Menu" still found')
        all_ok = False
if all_ok:
    print('FIX 7 (botones "Volver al Menu"): OK en todas las historias')

# Fix 8: Archivo personal
fichas = ['ficha-heya', 'ficha-amera', 'ficha-hesis', 'ficha-lomen', 'ficha-derk']
all_ok8 = True
for ficha_name in fichas:
    path = os.path.join(base, 'getting-to-know', 'personajes', f'{ficha_name}.html')
    c = open(path, encoding='utf-8', errors='replace').read()
    if 'Archivo personal' in c:
        print(f'FIX 8 ({ficha_name}): FALTA')
        all_ok8 = False
if all_ok8:
    print('FIX 8 ("Archivo personal"): OK en todas las fichas')

print('\n=== FIN VERIFICACION ===')
