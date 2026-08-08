import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'

# 1. Update Ruk el Héroe header CSS
ruk_path = os.path.join(base, 'ruk-el-heroe', 'index.html')
if os.path.exists(ruk_path):
    with open(ruk_path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    old_app_header_css = '''/* Header / Navbar */
 .app-header {
 width: 100%;
 max-width: 1200px;
 padding: 12px 24px;
 display: flex;
 justify-content: space-between;
 align-items: center;
 border-bottom: 1px solid var(--gold-border);
 background: var(--bg-card);
 box-shadow: var(--card-shadow);
 position: sticky;
 top: 0;
 z-index: 900;
 backdrop-filter: blur(10px);
 }'''

    new_app_header_css = '''/* Header / Navbar */
 .app-header {
 width: calc(100% - 24px);
 max-width: 1100px;
 margin: 10px auto 0 auto;
 padding: 12px 24px;
 display: flex;
 justify-content: space-between;
 align-items: center;
 border: 1.5px solid var(--gold-border);
 border-radius: 20px;
 background: var(--bg-card);
 box-shadow: var(--card-shadow);
 position: sticky;
 top: 10px;
 z-index: 900;
 backdrop-filter: blur(10px);
 }'''

    if old_app_header_css in c:
        c = c.replace(old_app_header_css, new_app_header_css)
    else:
        # Regex replacement fallback
        c = re.sub(
            r'\.app-header\s*\{[^}]*\}',
            '''app-header {
 width: calc(100% - 24px);
 max-width: 1100px;
 margin: 10px auto 0 auto;
 padding: 12px 24px;
 display: flex;
 justify-content: space-between;
 align-items: center;
 border: 1.5px solid var(--gold-border);
 border-radius: 20px;
 background: var(--bg-card);
 box-shadow: var(--card-shadow);
 position: sticky;
 top: 10px;
 z-index: 900;
 backdrop-filter: blur(10px);
 }''',
            c
        )

    with open(ruk_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated Ruk el Héroe app-header to rounded floating navbar!")

# 2. Check and round headers in other stories
for story_dir in ['la-piedra-sin-pulir', 'forgotten-sword', 'sangre-y-cadaveres', 'marriage-of-the-republic', 'getting-to-know']:
    fpath = os.path.join(base, story_dir, 'index.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        sc = f.read()

    modified = False
    # Ensure site-header or nav headers have rounded corners
    if '.site-header {' in sc and 'border-radius:' not in sc.split('.site-header {')[1].split('}')[0]:
        sc = sc.replace('.site-header {', '.site-header {\n border-radius: 20px;\n margin: 10px auto;\n width: calc(100% - 24px);', 1)
        modified = True
    elif '.top-nav {' in sc and 'border-radius:' not in sc.split('.top-nav {')[1].split('}')[0]:
        sc = sc.replace('.top-nav {', '.top-nav {\n border-radius: 20px;\n margin: 10px auto;\n width: calc(100% - 24px);', 1)
        modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(sc)
        print(f"Added rounded corners to header in {story_dir}")

print("\nDone adding rounded corners to headers!")
