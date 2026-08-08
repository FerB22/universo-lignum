import os
import glob
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
html_files = glob.glob(base + '/**/*.html', recursive=True)

# Broad emoji and decorative symbol pattern
emoji_pattern = re.compile(
    r'[\U0001F000-\U0010FFFF\u2600-\u26FF\u2700-\u27BF\u2300-\u23FF\u2B50\uFE0F\u200D✦❖]+'
)

files_modified = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # Remove emojis
    content = emoji_pattern.sub('', content)

    # Clean up double spaces created by emoji removal inside tags/text
    content = re.sub(r'  +', ' ', content)
    content = content.replace('> <', '><')

    # Specific common text cleanup
    content = content.replace('Volver a Historias', 'Volver a Historias')
    content = content.replace('Volver al inicio', 'Volver al inicio')

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_modified += 1
        print(f"Removed emojis from: {os.path.relpath(fpath, base)}")

print(f"\nDone! Modified {files_modified} HTML files.")
