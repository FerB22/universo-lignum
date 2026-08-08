import os

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
piedra_path = os.path.join(base, 'la-piedra-sin-pulir', 'index.html')

if os.path.exists(piedra_path):
    with open(piedra_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    duplicate_action = '''          <div class="card-action" style="color: var(--text-muted);">
            En proceso de creación
          </div>
        </div>
 <div class="card-action" style="color: var(--color-emerald);">
 Ver Personajes <span>→</span>
 </div>
 </div>'''

    clean_action = '''          <div class="card-action" style="color: var(--text-muted);">
            En proceso de creación
          </div>
        </div>'''

    if duplicate_action in c:
        c = c.replace(duplicate_action, clean_action)
    else:
        c = c.replace('<div class="card-action" style="color: var(--color-emerald);">\n Ver Personajes <span>→</span>\n </div>', '')

    with open(piedra_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Cleaned up card 3 in La Piedra sin Pulir!")
