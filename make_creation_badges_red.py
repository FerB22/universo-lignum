import os
import glob
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

red_style_badge = 'font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0.25rem 0.65rem; border-radius:9999px; background:rgba(239,68,68,0.12); color:#EF4444; border:1px solid rgba(239,68,68,0.4); margin-bottom:0.6rem;'

# 1. Update Ruk el Héroe
ruk_path = os.path.join(base, 'ruk-el-heroe', 'index.html')
if os.path.exists(ruk_path):
    with open(ruk_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Change golden badge to vibrant red badge
    old_ruk_badge = r'<span style="display:inline-block; font-size:0\.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:0\.25rem 0\.65rem; border-radius:9999px; background:rgba\(212,175,55,0\.15\); color:#D4AF37; border:1px solid rgba\(212,175,55,0\.3\); margin-bottom:0\.6rem;">En proceso de creación</span>'
    new_ruk_badge = f'<span style="display:inline-block; {red_style_badge}">En proceso de creación</span>'

    c = re.sub(old_ruk_badge, new_ruk_badge, c)

    with open(ruk_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated Ruk el Héroe Fichas badge to RED!")

# 2. Update master hub index.html
hub_path = os.path.join(base, 'index.html')
if os.path.exists(hub_path):
    with open(hub_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    c = c.replace('<span class="card-badge" style="color: #D4AF37; border-color: #D4AF37;">En Creación · Fantasía Épica</span>',
                  '<span class="card-badge" style="color: #EF4444; border-color: #EF4444; background: rgba(239,68,68,0.12);">En Creación · Fantasía Épica</span>')

    with open(hub_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated master hub index.html Ruk badge to RED!")

# 3. Update all story index files for any remaining "En proceso de creación" badges
for rel_path in ['la-piedra-sin-pulir/index.html', 'forgotten-sword/index.html', 'getting-to-know/index.html', 'marriage-of-the-republic/index.html']:
    sp = os.path.join(base, rel_path)
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8', errors='ignore') as f:
            sc = f.read()

        # Ensure all En proceso de creación spans have red text #EF4444 and red border
        sc = re.sub(r'color:#2d6a4f; border:1px solid rgba\(45,106,79,0\.3\);', 'color:#EF4444; border:1px solid rgba(239,68,68,0.4); background:rgba(239,68,68,0.12);', sc)
        sc = re.sub(r'color:#8B5A2B; border:1px solid rgba\(139,90,43,0\.3\);', 'color:#EF4444; border:1px solid rgba(239,68,68,0.4); background:rgba(239,68,68,0.12);', sc)
        sc = re.sub(r'color:var\(--color-emerald\); border:1px solid rgba\(16,185,129,0\.3\);', 'color:#EF4444; border:1px solid rgba(239,68,68,0.4); background:rgba(239,68,68,0.12);', sc)

        with open(sp, 'w', encoding='utf-8') as f:
            f.write(sc)
        print(f"Updated badges to RED in {rel_path}!")

print("\nDone setting all 'En proceso de creación' badges to RED!")
