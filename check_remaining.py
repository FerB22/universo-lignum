import os

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# Check year 2025 in getting-to-know files
gk_index = os.path.join(base, 'getting-to-know', 'index.html')
with open(gk_index, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print('=== getting-to-know/index.html: 2025/2026 occurrences ===')
for i, l in enumerate(lines, 1):
    if '2025' in l or '2026' in l:
        print(f'  L{i}: {l.rstrip()}')

print()
# Check ficha file
ficha = os.path.join(base, 'getting-to-know', 'personajes', 'ficha-heya.html')
with open(ficha, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
idx2025 = content.find('2025')
idx2026 = content.find('2026')
print(f'ficha-heya: 2025 at pos={idx2025}, 2026 at pos={idx2026}')
if idx2025 >= 0:
    print(f'context 2025: {content[max(0,idx2025-60):idx2025+60]}')

print()
# Check index.html brand-icon and href
hub = os.path.join(base, 'index.html')
with open(hub, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
print('=== index.html: brand-icon + href ===')
for i, l in enumerate(lines, 1):
    if 'brand-icon' in l or 'href="#"' in l or 'href="./index.html"' in l:
        print(f'  L{i}: {l.rstrip()}')
