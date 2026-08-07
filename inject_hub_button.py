import os
import re

base_lignum = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
base_historias = r'C:\Users\Barra\Documents\HISTORIAS'

btn_css = """
<style>
  .btn-back-to-hub-floating {
    position: fixed;
    top: 14px;
    left: 14px;
    z-index: 999999;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 15px;
    background: rgba(15, 20, 30, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 20px;
    color: #F8FAFC !important;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.25s ease;
  }
  .btn-back-to-hub-floating:hover {
    background: #38BDF8;
    color: #000000 !important;
    border-color: #38BDF8;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.5);
  }
  @media (max-width: 600px) {
    .btn-back-to-hub-floating {
      top: 10px;
      left: 10px;
      padding: 5px 12px;
      font-size: 11px;
    }
  }
</style>
"""

def inject_file(file_path, depth):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'btn-back-to-hub-floating' in content:
        return

    rel_path = "../" * depth + "index.html"
    btn_html = f'<a href="{rel_path}" class="btn-back-to-hub-floating">🌌 Volver a Historias</a>'

    if '</head>' in content:
        content = content.replace('</head>', f'{btn_css}\n</head>', 1)
    if '<body' in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + btn_html, content, count=1, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Injected button in: {file_path}')

# Process UNIVERSO LIGNUM
for root, dirs, files in os.walk(base_lignum):
    if root == base_lignum:
        continue
    rel = os.path.relpath(root, base_lignum)
    depth = len(rel.split(os.sep))
    for f in files:
        if f.endswith('.html'):
            inject_file(os.path.join(root, f), depth)

# Process HISTORIAS
for root, dirs, files in os.walk(base_historias):
    if root == base_historias:
        continue
    rel = os.path.relpath(root, base_historias)
    depth = len(rel.split(os.sep))
    for f in files:
        if f.endswith('.html'):
            inject_file(os.path.join(root, f), depth)

print('All HTML pages updated with floating return button!')
