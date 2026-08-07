import os

def inject_ruk_cover(index_path):
    if not os.path.exists(index_path):
        return
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'ruk_en_creacion.png' in content:
        return

    cover_html = '<div style="text-align: center; margin: 1.5rem 0;"><img src="./fichas_img/ruk_en_creacion.png" alt="Ruk el Héroe - En Creación" style="max-width: 320px; width: 85%; border-radius: 14px; border: 2px solid rgba(212,175,55,0.4); box-shadow: 0 10px 30px rgba(0,0,0,0.6);"></div>'

    if '</header>' in content:
        content = content.replace('</header>', f'{cover_html}\n</header>', 1)
    elif '<main' in content:
        pos = content.find('<main')
        end_pos = content.find('>', pos) + 1
        content = content[:end_pos] + '\n' + cover_html + content[end_pos:]

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Injected Ruk cover into: {index_path}')

inject_ruk_cover(r'C:\Users\Barra\Documents\UNIVERSO LIGNUM\ruk-el-heroe\index.html')
inject_ruk_cover(r'C:\Users\Barra\Documents\HISTORIAS\HISTORIA - Ruk el Héroe\index.html')
