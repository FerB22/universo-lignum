import os, glob

ruk_editado = r"c:\Users\Barra\Documents\Ruk - Historia Completa\Ruk_Editado"
files = glob.glob(os.path.join(ruk_editado, "*.md"))

total_replacements = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("Dementi", "Demeti").replace("dementi", "demeti")
    new_content = new_content.replace("Dementianos", "Demetianos").replace("dementianos", "demetianos")
    
    if content != new_content:
        count = content.count("Dementi") + content.count("dementi") + content.count("dementianos") + content.count("Dementianos")
        total_replacements += count
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced {count} occurrences in: {os.path.basename(filepath)}")

print(f"Total Dementi -> Demeti replacements: {total_replacements}")
