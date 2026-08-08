import os
import re

base = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM'
fpath = os.path.join(base, 'forgotten-sword', 'capitulos.html')

with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

pattern_ch14 = r'<div class="tarjeta-capitulo" style="opacity:0\.75;.*?CAPÍTULO 14.*?</div>\s*</div>'

new_ch14 = '''<div class="tarjeta-capitulo" style="opacity:0.9; cursor:default; border:1px dashed #FF4444; background:rgba(239,68,68,0.12); pointer-events:none; user-select:none;">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <span style="font-size:10px; color:#FF6666; font-family:'Cinzel',serif; letter-spacing:2px; font-weight:700;">CAPÍTULO 14</span>
    <span style="font-size:9px; color:#FF4444; font-family:'Cinzel',serif; letter-spacing:1px; background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.5); padding:2px 8px; border-radius:4px; text-transform:uppercase; font-weight:700;">En proceso de escritura</span>
  </div>
  <p style="margin:4px 0 0 0; font-size:14px; color:#FFCCCC; font-weight:600; line-height:1.3;">El renacer de la paz</p>
  <span style="font-size:11px; color:#FF8888; font-style:italic; display:block; margin-top:3px;">Capítulo 14 en proceso de escritura</span>
</div>'''

c = re.sub(pattern_ch14, new_ch14, c, flags=re.DOTALL)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated Chapter 14 in capitulos.html to red badge!")
