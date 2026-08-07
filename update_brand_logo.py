import os

logo_url = "https://i.ibb.co/Vc9BJn4r/Logo-Lignum.png"

base_lignum = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
index_path = os.path.join(base_lignum, 'index.html')

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update CSS if needed
    if '.brand-logo-img' not in content:
        content = content.replace('.brand-icon {', '''.brand-logo-img {
      width: 44px;
      height: 44px;
      object-fit: contain;
      border-radius: 10px;
      transition: transform 0.3s ease;
      filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.4));
    }
    .brand-logo-img:hover {
      transform: scale(1.08);
    }
    .brand-icon {''', 1)

    # 2. Replace brand-icon div with img element
    old_icon_pattern = '''<div class="brand-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>'''
    new_img_tag = f'<img src="{logo_url}" alt="Logo Universo Lignum" class="brand-logo-img">'

    if old_icon_pattern in content:
        content = content.replace(old_icon_pattern, new_img_tag)
    elif '<div class="brand-icon">' in content:
        import re
        content = re.sub(r'<div class="brand-icon">.*?</div>', new_img_tag, content, flags=re.DOTALL)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update scripts
for script_name in ['update_master_hub_covers.py', 'update_literary_tags.py']:
    sp = os.path.join(base_lignum, script_name)
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8') as f:
            c = f.read()
        if old_icon_pattern in c:
            c = c.replace(old_icon_pattern, new_img_tag)
        elif '<div class="brand-icon">' in c:
            import re
            c = re.sub(r'<div class="brand-icon">.*?</div>', new_img_tag, c, flags=re.DOTALL)
        with open(sp, 'w', encoding='utf-8') as f:
            f.write(c)

print('Updated brand logo in header with Logo-Lignum.png!')
