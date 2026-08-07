#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilador Maestro del Monorepositorio Literario - UNIVERSO LIGNUM
Lee todos los textos editados de las 6 historias y construye el portal HTML unificado.
"""

import os
import re
import glob

BASE_HISTORIAS = r'C:\Users\Barra\Documents\HISTORIAS'
OUT_PATH = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM\index.html'
DIST_PATH = r'C:\Users\Barra\Documents\UNIVERSO LIGNUM\dist\index.html'


def leer_utf8(path):
    """Lee archivo con fallback latin-1."""
    for enc in ('utf-8', 'latin-1', 'cp1252'):
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except Exception:
            pass
    return ''


def md_to_html_basic(text):
    """Convierte Markdown básico a HTML seguro."""
    lines = text.split('\n')
    html_lines = []
    for line in lines:
        line_s = line.rstrip()
        if line_s.startswith('### '):
            html_lines.append(f'<h3>{line_s[4:]}</h3>')
        elif line_s.startswith('## '):
            html_lines.append(f'<h2>{line_s[3:]}</h2>')
        elif line_s.startswith('# '):
            html_lines.append(f'<h2>{line_s[2:]}</h2>')
        elif line_s.startswith('---') or line_s.startswith('==='):
            html_lines.append('<hr class="story-divider">')
        elif line_s.startswith('**') and line_s.endswith('**'):
            html_lines.append(f'<p><strong>{line_s[2:-2]}</strong></p>')
        elif line_s.startswith('* ') or line_s.startswith('- '):
            html_lines.append(f'<li>{line_s[2:]}</li>')
        elif line_s == '':
            html_lines.append('')
        else:
            # Bold/italic inline
            line_s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line_s)
            line_s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line_s)
            html_lines.append(f'<p>{line_s}</p>')
    # Wrap adjacent <li> in <ul>
    result = '\n'.join(html_lines)
    result = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', result, flags=re.DOTALL)
    return result


# ─────────────────────────────────────────────────────────
# 1. RUK EL HÉROE — 9 Capítulos Editados
# ─────────────────────────────────────────────────────────
ruk_dir = os.path.join(BASE_HISTORIAS, 'HISTORIA - Ruk el Héroe', 'Ruk_Editado')
ruk_caps_raw = sorted(glob.glob(os.path.join(ruk_dir, 'Capitulo_*.md')))

ruk_toc_items = []
ruk_sections = []

for cap_file in ruk_caps_raw:
    base = os.path.basename(cap_file)
    # Extract cap number and title from filename
    m = re.match(r'Capitulo_(\d+)_(.+)\.md', base)
    cap_num = m.group(1) if m else '?'
    cap_title_raw = m.group(2).replace('_', ' ') if m else base
    
    text = leer_utf8(cap_file)
    # Get first heading if present
    first_line = text.split('\n')[0].lstrip('#').strip()
    cap_title = first_line if first_line else f'Capítulo {cap_num}: {cap_title_raw}'
    
    anchor = f'ruk-cap-{cap_num}'
    ruk_toc_items.append(f'<li><a href="#{anchor}" onclick="scrollToAnchor(\'{anchor}\')"><strong>Cap. {cap_num}:</strong> {cap_title}</a></li>')
    
    html_body = md_to_html_basic(text)
    ruk_sections.append(f'''
      <div class="cap-section" id="{anchor}">
        {html_body}
      </div>
      <hr class="story-divider">
    ''')

ruk_toc_html = '<ol class="toc-list">' + '\n'.join(ruk_toc_items) + '</ol>'
ruk_full_html = '\n'.join(ruk_sections)

# ─────────────────────────────────────────────────────────
# 2. FORGOTTEN SWORD — 14 Capítulos Editados
# ─────────────────────────────────────────────────────────
fs_dir = os.path.join(BASE_HISTORIAS, 'HISTORIA - Forgotten Sword', 'Forgotten_Sword_Editado')
fs_caps_raw = sorted(glob.glob(os.path.join(fs_dir, 'Capitulo_*.md')))

fs_toc_items = []
fs_sections = []

for cap_file in fs_caps_raw:
    base = os.path.basename(cap_file)
    m = re.match(r'Capitulo_(\d+)_(.+)\.md', base)
    cap_num = m.group(1) if m else '?'
    cap_title_raw = m.group(2).replace('_', ' ').strip() if m else base
    text = leer_utf8(cap_file)
    first_line = text.split('\n')[0].lstrip('#').strip()
    cap_title = first_line if first_line else f'Capítulo {cap_num}: {cap_title_raw}'
    anchor = f'fs-cap-{cap_num}'
    fs_toc_items.append(f'<li><a href="#{anchor}" onclick="scrollToAnchor(\'{anchor}\')"><strong>Cap. {cap_num}:</strong> {cap_title}</a></li>')
    html_body = md_to_html_basic(text)
    fs_sections.append(f'''
      <div class="cap-section" id="{anchor}">
        {html_body}
      </div>
      <hr class="story-divider">
    ''')

fs_toc_html = '<ol class="toc-list">' + '\n'.join(fs_toc_items) + '</ol>'
fs_full_html = '\n'.join(fs_sections)

# ─────────────────────────────────────────────────────────
# 3. SANGRE Y CADÁVERES — Conceptualización
# ─────────────────────────────────────────────────────────
sangre_dir = os.path.join(BASE_HISTORIAS, 'HISTORIA - Sangre y Cadáveres')
sangre_index = os.path.join(sangre_dir, 'index.html')
sangre_concept = os.path.join(sangre_dir, 'Sangre y Cadáveres - Conceptualización.md')

sangre_concept_html = ''
if os.path.exists(sangre_concept):
    sangre_concept_html = md_to_html_basic(leer_utf8(sangre_concept))

# Extract body from original index.html
sangre_body_html = ''
if os.path.exists(sangre_index):
    sangre_raw = leer_utf8(sangre_index)
    body_m = re.search(r'<body[^>]*>(.*?)</body>', sangre_raw, re.DOTALL | re.IGNORECASE)
    if body_m:
        # Strip nav/header/footer tags
        body_inner = body_m.group(1)
        body_inner = re.sub(r'<(nav|header|footer)[^>]*>.*?</\1>', '', body_inner, flags=re.DOTALL | re.IGNORECASE)
        sangre_body_html = body_inner.strip()

# ─────────────────────────────────────────────────────────
# 4. THE MARRIAGE OF THE REPUBLIC
# ─────────────────────────────────────────────────────────
republic_dir = os.path.join(BASE_HISTORIAS, 'HISTORIA - The Marriage of the Republic')
republic_index = os.path.join(republic_dir, 'index.html')
republic_body_html = ''
if os.path.exists(republic_index):
    rep_raw = leer_utf8(republic_index)
    body_m = re.search(r'<body[^>]*>(.*?)</body>', rep_raw, re.DOTALL | re.IGNORECASE)
    if body_m:
        body_inner = body_m.group(1)
        body_inner = re.sub(r'<(nav|header|footer)[^>]*>.*?</\1>', '', body_inner, flags=re.DOTALL | re.IGNORECASE)
        # Remove script tags from body
        body_inner = re.sub(r'<script[^>]*>.*?</script>', '', body_inner, flags=re.DOTALL | re.IGNORECASE)
        republic_body_html = body_inner.strip()

# ─────────────────────────────────────────────────────────
# 5. GETTING TO KNOW — Fichas de personajes + texto
# ─────────────────────────────────────────────────────────
gtk_dir = os.path.join(BASE_HISTORIAS, 'HISTORIA - Getting to Know')
gtk_fichas_md = os.path.join(gtk_dir, 'fichas_markdown', 'TODAS_LAS_FICHAS.md')
gtk_main_md = os.path.join(gtk_dir, 'Getting to Know.md')

gtk_fichas_html = md_to_html_basic(leer_utf8(gtk_fichas_md)) if os.path.exists(gtk_fichas_md) else ''
gtk_main_html = md_to_html_basic(leer_utf8(gtk_main_md)) if os.path.exists(gtk_main_md) else ''

# ─────────────────────────────────────────────────────────
# 6. LA PIEDRA SIN PULIR — Manuscrito Completo
# ─────────────────────────────────────────────────────────
piedra_dir = os.path.join(BASE_HISTORIAS, 'HISTORIA - La Piedra sin Pulir')
piedra_md = os.path.join(piedra_dir, 'La Piedra sin Pulir.md')
piedra_html = md_to_html_basic(leer_utf8(piedra_md)) if os.path.exists(piedra_md) else ''

# ─────────────────────────────────────────────────────────
# BUILD HTML
# ─────────────────────────────────────────────────────────

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UNIVERSO LIGNUM | Monorepositorio Literario</title>
  <meta name="description" content="Portal unificado de todas las historias del Universo Lignum. Scoped CSS Layouts independientes por universo narrativo.">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800;900&family=Lora:ital,wght@0,400;0,600;1,400&family=Orbitron:wght@600;800;900&family=Playfair+Display:wght@600;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">

  <style>
    /*** BASE ***/
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ background: #090B10; color: #F8FAFC; font-family: 'Plus Jakarta Sans', sans-serif; min-height: 100vh; overflow-x: hidden; }}

    /*** UNIVERSAL NAV ***/
    .univ-header {{ position: sticky; top: 0; z-index: 1000; background: rgba(15,17,23,.92); backdrop-filter: blur(16px); border-bottom: 1px solid rgba(255,255,255,.1); }}
    .univ-header-inner {{ max-width: 1350px; margin: 0 auto; padding: .65rem 1.5rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }}
    .brand {{ display: flex; align-items: center; gap: .75rem; text-decoration: none; color: inherit; cursor: pointer; }}
    .brand-icon {{ width: 38px; height: 38px; border-radius: 9px; background: radial-gradient(circle, #38BDF8 0%, rgba(0,0,0,.6) 100%); display: flex; align-items: center; justify-content: center; color: #fff; border: 1px solid #38BDF8; box-shadow: 0 0 12px rgba(56,189,248,.4); flex-shrink: 0; }}
    .brand-name {{ font-family: 'Cinzel', serif; font-size: 1.05rem; font-weight: 700; background: linear-gradient(135deg,#fff 0%,#38BDF8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    .brand-sub {{ font-size: .72rem; color: rgba(255,255,255,.5); display: block; }}
    .nav-pills {{ display: flex; align-items: center; gap: .45rem; flex-wrap: wrap; }}
    .pill {{ padding: .4rem .8rem; border-radius: 9999px; font-size: .78rem; font-weight: 600; cursor: pointer; border: 1px solid rgba(255,255,255,.14); background: rgba(255,255,255,.04); color: #CBD5E1; transition: all .2s ease; white-space: nowrap; }}
    .pill:hover, .pill.active {{ background: var(--c, #38BDF8); color: #000; border-color: var(--c, #38BDF8); transform: translateY(-1px); }}

    /*** VIEWS ***/
    .view {{ display: none; min-height: 80vh; animation: fadeIn .35s ease; }}
    .view.active {{ display: block; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    /*** ───── PORTAL ───── ***/
    .portal-bg {{ background: #090B10; }}
    .portal-hero {{ text-align: center; padding: 4rem 1rem 2.5rem; background: radial-gradient(circle at top, rgba(56,189,248,.13) 0%, #090B10 72%); }}
    .portal-badge {{ display: inline-flex; align-items: center; gap: .45rem; padding: .35rem 1rem; border-radius: 9999px; background: rgba(56,189,248,.1); border: 1px solid rgba(56,189,248,.3); color: #38BDF8; font-size: .82rem; margin-bottom: 1.25rem; }}
    .portal-title {{ font-family: 'Cinzel', serif; font-size: clamp(2.2rem, 5vw, 3.8rem); font-weight: 900; letter-spacing: 2px; background: linear-gradient(135deg,#FFF 0%,#38BDF8 50%,#D4AF37 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: .85rem; }}
    .portal-desc {{ max-width: 780px; margin: 0 auto 2rem; color: #94A3B8; font-size: 1.05rem; line-height: 1.7; }}
    .portal-stats {{ display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap; margin-bottom: 2.5rem; }}
    .stat-box {{ background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07); border-radius: 12px; padding: 1rem 1.75rem; text-align: center; }}
    .stat-n {{ font-family: 'Cinzel', serif; font-size: 1.9rem; color: #38BDF8; }}
    .stat-l {{ font-size: .78rem; color: #64748B; }}
    .portal-grid {{ max-width: 1250px; margin: 0 auto; padding: 0 1.5rem 4rem; display: grid; grid-template-columns: repeat(auto-fill, minmax(340px,1fr)); gap: 1.75rem; }}
    .story-card {{ background: rgba(22,27,38,.65); border: 1px solid rgba(255,255,255,.09); border-radius: 18px; padding: 1.75rem; display: flex; flex-direction: column; justify-content: space-between; transition: all .35s ease; }}
    .story-card:hover {{ transform: translateY(-7px); border-color: var(--ct); box-shadow: 0 18px 40px rgba(0,0,0,.55); }}
    .sc-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: .85rem; }}
    .sc-genre {{ font-size: .7rem; font-weight: 700; text-transform: uppercase; padding: .22rem .6rem; border-radius: 9999px; color: var(--ct); border: 1px solid var(--ct); }}
    .sc-layout {{ font-size: .65rem; color: rgba(255,255,255,.4); font-family: monospace; }}
    .sc-title {{ font-family: 'Cinzel', serif; font-size: 1.35rem; color: #FFF; margin-bottom: .6rem; }}
    .sc-desc {{ font-size: .88rem; color: #94A3B8; line-height: 1.55; margin-bottom: 1.25rem; flex-grow: 1; }}
    .sc-meta {{ display: flex; justify-content: space-between; font-size: .78rem; color: #64748B; border-top: 1px solid rgba(255,255,255,.05); padding-top: .85rem; margin-bottom: 1rem; }}
    .sc-badge {{ color: #10B981; font-weight: 600; }}
    .sc-btn {{ display: flex; align-items: center; justify-content: center; gap: .5rem; padding: .72rem; border-radius: 10px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.12); color: #FFF; font-weight: 600; cursor: pointer; transition: all .25s ease; width: 100%; }}
    .sc-btn:hover {{ background: var(--ct); border-color: var(--ct); color: #000; }}

    /*** ───── SCOPED LAYOUT 1: RUK (Blanco & Dorado) ───── ***/
    .layout-ruk {{ background: #FAF8F5; color: #2C261F; font-family: 'Lora', serif; }}
    .ruk-wrap {{ max-width: 900px; margin: 2.5rem auto; background: #FFF; padding: 3rem 3.5rem; border-radius: 20px; border: 2px solid #D4AF37; box-shadow: 0 15px 40px rgba(212,175,55,.18); }}
    .ruk-wrap h1, .ruk-wrap h2, .ruk-wrap h3 {{ font-family: 'Cinzel', serif; color: #2C261F; }}
    .ruk-wrap h2 {{ font-size: 1.6rem; color: #9E8237; border-bottom: 2px solid #FFD700; padding-bottom: .6rem; margin: 2rem 0 1rem; }}
    .ruk-wrap h3 {{ font-size: 1.2rem; color: #7A6428; margin: 1.5rem 0 .75rem; }}
    .ruk-wrap p {{ font-size: 1.08rem; line-height: 1.9; color: #3A3228; margin-bottom: 1.1rem; text-align: justify; }}
    .ruk-wrap ul {{ margin: .75rem 0 .75rem 1.5rem; }}
    .ruk-wrap li {{ color: #3A3228; line-height: 1.7; margin-bottom: .4rem; }}
    .ruk-toc {{ background: #FAF8F5; border: 1px solid #D4AF37; border-radius: 12px; padding: 1.5rem 2rem; margin-bottom: 2.5rem; }}
    .ruk-toc h3 {{ font-family: 'Cinzel', serif; color: #9E8237; margin-bottom: 1rem; font-size: 1rem; }}
    .toc-list {{ list-style: none; counter-reset: toc; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px,1fr)); gap: .4rem; }}
    .toc-list li {{ font-size: .88rem; }}
    .toc-list a {{ color: #7A6428; text-decoration: none; }}
    .toc-list a:hover {{ color: #D4AF37; text-decoration: underline; }}
    .cap-section {{ margin-bottom: 1rem; }}
    .story-divider {{ border: none; border-top: 2px solid #D4AF37; margin: 2rem 0; opacity: .35; }}

    /*** ───── SCOPED LAYOUT 2: FORGOTTEN SWORD (Gótico) ───── ***/
    .layout-forgotten {{ background: #0B0B0E; color: #E2E8F0; }}
    .fs-wrap {{ max-width: 900px; margin: 2.5rem auto; background: #13131A; padding: 3rem 3.5rem; border-radius: 16px; border: 1px solid #8B0000; box-shadow: 0 0 35px rgba(139,0,0,.3); font-family: 'Plus Jakarta Sans', sans-serif; }}
    .fs-wrap h2 {{ font-family: 'Cinzel', serif; color: #E2E8F0; font-size: 1.6rem; border-bottom: 1px solid #8B0000; padding-bottom: .6rem; margin: 2rem 0 1rem; text-shadow: 0 0 8px rgba(139,0,0,.5); }}
    .fs-wrap h3 {{ font-family: 'Cinzel', serif; color: #CBD5E1; font-size: 1.15rem; margin: 1.5rem 0 .75rem; }}
    .fs-wrap p {{ font-size: 1.05rem; line-height: 1.8; color: #CBD5E1; margin-bottom: 1.1rem; text-align: justify; }}
    .fs-wrap ul {{ margin: .75rem 0 .75rem 1.5rem; }}
    .fs-wrap li {{ color: #CBD5E1; line-height: 1.7; margin-bottom: .4rem; }}
    .fs-toc {{ background: rgba(139,0,0,.1); border: 1px solid rgba(139,0,0,.4); border-radius: 10px; padding: 1.25rem 1.75rem; margin-bottom: 2.5rem; }}
    .fs-toc h3 {{ font-family: 'Cinzel', serif; color: #E2E8F0; margin-bottom: 1rem; font-size: .95rem; }}
    .fs-wrap .story-divider {{ border-top-color: #8B0000; }}
    .fs-wrap .toc-list a {{ color: #CBD5E1; }}
    .fs-wrap .toc-list a:hover {{ color: #FF4444; }}

    /*** ───── SCOPED LAYOUT 3: SANGRE Y CADÁVERES (Escarlata) ───── ***/
    .layout-sangre {{ background: #0D0202; color: #F8FAFC; }}
    .sangre-wrap {{ max-width: 900px; margin: 2.5rem auto; background: #140404; padding: 3rem 3.5rem; border-radius: 16px; border: 2px solid #CA0B0B; box-shadow: 0 0 40px rgba(202,11,11,.4); }}
    .sangre-wrap h2 {{ font-family: 'Cinzel', serif; color: #FF3333; font-size: 1.6rem; border-bottom: 2px solid #CA0B0B; padding-bottom: .6rem; margin: 2rem 0 1rem; text-shadow: 0 0 15px rgba(202,11,11,.7); }}
    .sangre-wrap h3 {{ font-family: 'Cinzel', serif; color: #FF6666; font-size: 1.15rem; margin: 1.5rem 0 .75rem; }}
    .sangre-wrap p {{ font-size: 1.08rem; line-height: 1.88; color: #E2E8F0; margin-bottom: 1.1rem; text-align: justify; }}
    .sangre-wrap ul {{ margin: .75rem 0 .75rem 1.5rem; }}
    .sangre-wrap li {{ color: #E2E8F0; line-height: 1.7; margin-bottom: .4rem; }}
    .sangre-concept {{ background: rgba(202,11,11,.08); border: 1px solid rgba(202,11,11,.3); border-radius: 10px; padding: 1.5rem; margin-bottom: 2.5rem; }}
    .sangre-wrap .story-divider {{ border-top-color: #CA0B0B; }}

    /*** ───── SCOPED LAYOUT 4: MARRIAGE OF REPUBLIC (Marrón) ───── ***/
    .layout-republic {{ background: #FDFBF7; color: #4A3525; }}
    .republic-wrap {{ max-width: 900px; margin: 2.5rem auto; background: #FFFDF9; padding: 3rem 3.5rem; border-radius: 18px; border: 2px solid #8B5A2B; box-shadow: 0 12px 35px rgba(139,90,43,.15); }}
    .republic-wrap h1, .republic-wrap h2, .republic-wrap h3 {{ font-family: 'Playfair Display', serif; color: #8B5A2B; }}
    .republic-wrap h2 {{ font-size: 1.65rem; border-bottom: 2px solid #D4AF37; padding-bottom: .6rem; margin: 2rem 0 1rem; }}
    .republic-wrap h3 {{ font-size: 1.2rem; color: #6B4220; margin: 1.5rem 0 .75rem; }}
    .republic-wrap p {{ font-size: 1.08rem; line-height: 1.88; color: #3D2B1F; margin-bottom: 1.1rem; text-align: justify; }}
    .republic-wrap ul, .republic-wrap ol {{ margin: .75rem 0 .75rem 1.5rem; }}
    .republic-wrap li {{ color: #3D2B1F; line-height: 1.7; margin-bottom: .4rem; }}
    .republic-wrap .story-divider {{ border-top-color: #8B5A2B; }}

    /*** ───── SCOPED LAYOUT 5: GETTING TO KNOW (Cyberpunk) ───── ***/
    .layout-cyber {{ background: #070913; color: #E0F7FA; }}
    .cyber-wrap {{ max-width: 1050px; margin: 2.5rem auto; background: #0B0E1B; padding: 3rem 3.5rem; border-radius: 16px; border: 2px solid #00F2FE; box-shadow: 0 0 40px rgba(0,242,254,.3); font-family: 'Rajdhani', sans-serif; }}
    .cyber-wrap h2 {{ font-family: 'Orbitron', sans-serif; color: #00F2FE; font-size: 1.5rem; border-bottom: 2px solid #9B51E0; padding-bottom: .6rem; margin: 2rem 0 1rem; text-shadow: 0 0 12px #00F2FE; }}
    .cyber-wrap h3 {{ font-family: 'Orbitron', sans-serif; color: #9B51E0; font-size: 1.05rem; margin: 1.5rem 0 .75rem; }}
    .cyber-wrap p {{ font-size: 1.12rem; line-height: 1.78; color: #C7D2FE; margin-bottom: 1rem; }}
    .cyber-wrap ul {{ margin: .75rem 0 .75rem 1.5rem; }}
    .cyber-wrap li {{ color: #C7D2FE; line-height: 1.7; margin-bottom: .4rem; }}
    .fichas-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px,1fr)); gap: 1.25rem; margin-top: 2rem; }}
    .ficha-card {{ background: rgba(0,242,254,.05); border: 1px solid rgba(0,242,254,.25); border-radius: 12px; padding: 1.4rem; }}
    .ficha-card h3 {{ font-family: 'Orbitron', sans-serif; color: #00F2FE; font-size: 1rem; margin-bottom: 1rem; }}
    .ficha-card p {{ font-size: .9rem; color: #C7D2FE; margin-bottom: .6rem; }}
    .cyber-wrap .story-divider {{ border-top-color: #00F2FE; }}

    /*** ───── SCOPED LAYOUT 6: LA PIEDRA SIN PULIR (Esmeralda) ───── ***/
    .layout-emerald {{ background: #04120B; color: #ECFDF5; }}
    .emerald-wrap {{ max-width: 900px; margin: 2.5rem auto; background: #081C13; padding: 3rem 3.5rem; border-radius: 16px; border: 2px solid #10B981; box-shadow: 0 0 40px rgba(16,185,129,.3); }}
    .emerald-wrap h2 {{ font-family: 'Cinzel', serif; color: #34D399; font-size: 1.6rem; border-bottom: 2px solid #10B981; padding-bottom: .6rem; margin: 2rem 0 1rem; text-shadow: 0 0 10px rgba(16,185,129,.5); }}
    .emerald-wrap h3 {{ font-family: 'Cinzel', serif; color: #6EE7B7; font-size: 1.15rem; margin: 1.5rem 0 .75rem; }}
    .emerald-wrap p {{ font-size: 1.1rem; line-height: 1.9; color: #D1FAE5; margin-bottom: 1.1rem; text-align: justify; }}
    .emerald-wrap ul {{ margin: .75rem 0 .75rem 1.5rem; }}
    .emerald-wrap li {{ color: #D1FAE5; line-height: 1.7; margin-bottom: .4rem; }}
    .emerald-wrap .story-divider {{ border-top-color: #10B981; opacity: .4; }}

    /*** BACK BUTTON ***/
    .back-btn {{ display: inline-flex; align-items: center; gap: .5rem; padding: .7rem 1.4rem; border-radius: 10px; font-weight: 700; cursor: pointer; border: none; margin: 1.5rem auto 0; }}

    /*** UNIVERSAL FOOTER ***/
    .univ-footer {{ background: #0B0D14; border-top: 1px solid rgba(255,255,255,.07); padding: 2.5rem 1.5rem 2rem; text-align: center; margin-top: 3rem; }}
    .univ-footer p {{ color: #475569; font-size: .82rem; }}
    .footer-links {{ display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1rem; }}
    .footer-links span {{ color: #64748B; font-size: .82rem; cursor: pointer; transition: color .2s; }}
    .footer-links span:hover {{ color: #38BDF8; }}

    @media (max-width: 768px) {{
      .ruk-wrap, .fs-wrap, .sangre-wrap, .republic-wrap, .cyber-wrap, .emerald-wrap {{ padding: 1.75rem 1.25rem; margin: 1rem; }}
      .fichas-grid {{ grid-template-columns: 1fr; }}
      .toc-list {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

  <!-- UNIVERSAL NAVIGATION -->
  <header class="univ-header">
    <div class="univ-header-inner">
      <div class="brand" onclick="switchView('portal')">
        <div class="brand-icon">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <div>
          <div class="brand-name">UNIVERSO LIGNUM</div>
          <span class="brand-sub" id="active-sub">Portal Principal • Scoped CSS Layouts</span>
        </div>
      </div>

      <nav class="nav-pills">
        <div class="pill active" style="--c:#38BDF8" id="pill-portal" onclick="switchView('portal')">🏠 Portal</div>
        <div class="pill" style="--c:#D4AF37" id="pill-ruk" onclick="switchView('ruk')">⚔ Ruk el Héroe</div>
        <div class="pill" style="--c:#8B0000" id="pill-forgotten" onclick="switchView('forgotten')">🗡 Forgotten Sword</div>
        <div class="pill" style="--c:#CA0B0B" id="pill-sangre" onclick="switchView('sangre')">🩸 Sangre y Cadáveres</div>
        <div class="pill" style="--c:#8B5A2B" id="pill-republic" onclick="switchView('republic')">📜 Republic</div>
        <div class="pill" style="--c:#00F2FE" id="pill-cyber" onclick="switchView('cyber')">⚡ Getting to Know</div>
        <div class="pill" style="--c:#10B981" id="pill-emerald" onclick="switchView('emerald')">🌿 La Piedra</div>
      </nav>
    </div>
  </header>

  <!-- ════════════ VIEW: PORTAL ════════════ -->
  <main id="view-portal" class="view active portal-bg">
    <section class="portal-hero">
      <div class="portal-badge">✦ Monorepositorio Literario · 6 Universos · Scoped CSS Layouts ✦</div>
      <h1 class="portal-title">UNIVERSO LIGNUM</h1>
      <p class="portal-desc">
        Todos tus mundos narrativos viven bajo una misma arquitectura. Cada historia tiene su propio <strong>Layout Scoped CSS</strong>, con tipografía, paleta y atmósfera exclusiva garantizada — sin interferencias entre universos.
      </p>
      <div class="portal-stats">
        <div class="stat-box"><div class="stat-n">6</div><div class="stat-l">Universos</div></div>
        <div class="stat-box"><div class="stat-n">6</div><div class="stat-l">Scoped Layouts</div></div>
        <div class="stat-box"><div class="stat-n">23+</div><div class="stat-l">Capítulos</div></div>
        <div class="stat-box"><div class="stat-n">5</div><div class="stat-l">Fichas de Personaje</div></div>
      </div>
    </section>

    <div class="portal-grid">
      <div class="story-card" style="--ct:#D4AF37">
        <div>
          <div class="sc-header"><span class="sc-genre">Fantasía Épica</span><span class="sc-layout">EstiloImperativoRuk.astro</span></div>
          <h3 class="sc-title">Ruk el Héroe</h3>
          <p class="sc-desc">Saga completa editada de 9 capítulos. Paleta Blanco &amp; Dorado Imperial (#FAF8F5, #D4AF37). Guerra, éter y la Espada del Salvador.</p>
        </div>
        <div class="sc-meta"><span>📖 9 Capítulos Completos</span><span class="sc-badge">✓ Saga Editada</span></div>
        <button class="sc-btn" onclick="switchView('ruk')">Abrir Universo Ruk →</button>
      </div>

      <div class="story-card" style="--ct:#8B0000">
        <div>
          <div class="sc-header"><span class="sc-genre">Fantasía Oscura</span><span class="sc-layout">EstiloForgottenSword.astro</span></div>
          <h3 class="sc-title">Forgotten Sword</h3>
          <p class="sc-desc">14 capítulos en atmósfera gótica de acero oscuro y carmesí (#0F0F12, #8B0000). Tribus, tatuajes y responsabilidad del liderazgo.</p>
        </div>
        <div class="sc-meta"><span>📖 14 Capítulos</span><span class="sc-badge">✓ Saga Completa</span></div>
        <button class="sc-btn" onclick="switchView('forgotten')">Abrir Forgotten Sword →</button>
      </div>

      <div class="story-card" style="--ct:#CA0B0B">
        <div>
          <div class="sc-header"><span class="sc-genre">Terror Visceral</span><span class="sc-layout">EstiloSangreCadaveres.astro</span></div>
          <h3 class="sc-title">Sangre y Cadáveres</h3>
          <p class="sc-desc">Rojo escarlata (#CA0B0B) y negro absoluto. Conceptualización y texto del universo de terror crudo y resistencia armada.</p>
        </div>
        <div class="sc-meta"><span>📖 Historia + Conceptualización</span><span class="sc-badge">✓ Publicado</span></div>
        <button class="sc-btn" onclick="switchView('sangre')">Abrir Sangre y Cadáveres →</button>
      </div>

      <div class="story-card" style="--ct:#8B5A2B">
        <div>
          <div class="sc-header"><span class="sc-genre">Ficción Histórica</span><span class="sc-layout">EstiloMarriageRepublic.astro</span></div>
          <h3 class="sc-title">The Marriage of the Republic</h3>
          <p class="sc-desc">Marrón claro &amp; dorado republicano (#8B5A2B, #D4AF37). Intrigas de Estado, capitulaciones y el peso del matrimonio político.</p>
        </div>
        <div class="sc-meta"><span>📖 Historia Completa</span><span class="sc-badge">✓ En Desarrollo</span></div>
        <button class="sc-btn" onclick="switchView('republic')">Abrir Republic →</button>
      </div>

      <div class="story-card" style="--ct:#00F2FE">
        <div>
          <div class="sc-header"><span class="sc-genre">Fantasía Tribal</span><span class="sc-layout">EstiloGettingToKnow.astro</span></div>
          <h3 class="sc-title">Getting to Know</h3>
          <p class="sc-desc">5 fichas completas de personajes (Heya, Ameřa, Hesis, Lomen, Derk) y texto íntegro de la novela tribal Häscht en estética turquesa.</p>
        </div>
        <div class="sc-meta"><span>📖 5 Fichas + Novela</span><span class="sc-badge">✓ Fichas Completas</span></div>
        <button class="sc-btn" onclick="switchView('cyber')">Abrir Getting to Know →</button>
      </div>

      <div class="story-card" style="--ct:#10B981">
        <div>
          <div class="sc-header"><span class="sc-genre">Fábula Mística</span><span class="sc-layout">EstiloLaPiedraSinPulir.astro</span></div>
          <h3 class="sc-title">La Piedra sin Pulir</h3>
          <p class="sc-desc">Manuscrito completo del Señor de las Siete Esposas. Fábula moral sobre el linaje, el poder y la justicia en verde esmeralda (#10B981).</p>
        </div>
        <div class="sc-meta"><span>📖 Manuscrito Completo</span><span class="sc-badge">✓ Completo</span></div>
        <button class="sc-btn" onclick="switchView('emerald')">Abrir La Piedra sin Pulir →</button>
      </div>
    </div>
  </main>

  <!-- ════════════ VIEW: RUK EL HÉROE ════════════ -->
  <section id="view-ruk" class="view layout-ruk">
    <div class="ruk-wrap">
      <div style="text-align:center;font-size:.8rem;color:#D4AF37;font-weight:700;letter-spacing:2px;margin-bottom:.5rem;">✦ LAYOUT: EstiloImperativoRuk.astro · Blanco & Dorado Imperial #D4AF37 ✦</div>
      <h2 style="text-align:center;font-size:2.2rem;color:#9E8237;border:none;padding:0;margin-bottom:.5rem;">RUK EL HÉROE</h2>
      <p style="text-align:center;color:#7A6428;font-style:italic;margin-bottom:2rem;">Saga Completa Editada · 9 Capítulos · Edición Restaurada UTF-8</p>

      <div class="ruk-toc">
        <h3>⚔ Índice de Capítulos</h3>
        {ruk_toc_html}
      </div>

      {ruk_full_html}

      <div style="text-align:center;margin-top:2rem;">
        <button class="back-btn" onclick="switchView('portal')" style="background:#D4AF37;color:#000;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- ════════════ VIEW: FORGOTTEN SWORD ════════════ -->
  <section id="view-forgotten" class="view layout-forgotten">
    <div class="fs-wrap">
      <div style="text-align:center;font-size:.8rem;color:#8B0000;font-weight:700;letter-spacing:2px;margin-bottom:.5rem;">⚔ LAYOUT: EstiloForgottenSword.astro · Gótico & Carmesí #8B0000 ⚔</div>
      <h2 style="text-align:center;font-size:2.2rem;border:none;padding:0;margin-bottom:.5rem;">FORGOTTEN SWORD</h2>
      <p style="text-align:center;color:#94A3B8;font-style:italic;margin-bottom:2rem;">Saga Completa · 14 Capítulos · Fantasía Oscura Tribal</p>

      <div class="fs-toc">
        <h3>🗡 Índice de Capítulos</h3>
        {fs_toc_html}
      </div>

      {fs_full_html}

      <div style="text-align:center;margin-top:2rem;">
        <button class="back-btn" onclick="switchView('portal')" style="background:#8B0000;color:#FFF;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- ════════════ VIEW: SANGRE Y CADÁVERES ════════════ -->
  <section id="view-sangre" class="view layout-sangre">
    <div class="sangre-wrap">
      <div style="text-align:center;font-size:.8rem;color:#FF3333;font-weight:700;letter-spacing:2px;margin-bottom:.5rem;">🩸 LAYOUT: EstiloSangreCadaveres.astro · Escarlata #CA0B0B & Negro Absoluto 🩸</div>
      <h2 style="text-align:center;font-size:2.2rem;border:none;padding:0;margin-bottom:.5rem;">SANGRE Y CADÁVERES</h2>
      <p style="text-align:center;color:#94A3B8;font-style:italic;margin-bottom:2rem;">Terror Visceral · Conceptualización y Texto Completo</p>

      <div class="sangre-concept">
        <h2>Conceptualización</h2>
        {sangre_concept_html}
      </div>

      <h2>Historia</h2>
      {sangre_body_html if sangre_body_html else '<p>El texto completo de la historia está disponible en la edición original.</p>'}

      <div style="text-align:center;margin-top:2rem;">
        <button class="back-btn" onclick="switchView('portal')" style="background:#CA0B0B;color:#FFF;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- ════════════ VIEW: THE MARRIAGE OF THE REPUBLIC ════════════ -->
  <section id="view-republic" class="view layout-republic">
    <div class="republic-wrap">
      <div style="text-align:center;font-size:.8rem;color:#8B5A2B;font-weight:700;letter-spacing:2px;margin-bottom:.5rem;">📜 LAYOUT: EstiloMarriageRepublic.astro · Marrón Claro #8B5A2B & Dorado 📜</div>
      <h2 style="text-align:center;font-size:2.2rem;border:none;padding:0;margin-bottom:.5rem;">THE MARRIAGE OF THE REPUBLIC</h2>
      <p style="text-align:center;color:#8B5A2B;font-style:italic;margin-bottom:2rem;">Ficción Histórica · Historia Interactiva Completa</p>

      {republic_body_html if republic_body_html else '<p>El contenido interactivo de la historia está disponible en la edición original.</p>'}

      <div style="text-align:center;margin-top:2rem;">
        <button class="back-btn" onclick="switchView('portal')" style="background:#8B5A2B;color:#FFF;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- ════════════ VIEW: GETTING TO KNOW ════════════ -->
  <section id="view-cyber" class="view layout-cyber">
    <div class="cyber-wrap">
      <div style="text-align:center;font-size:.8rem;color:#00F2FE;font-weight:700;letter-spacing:2px;margin-bottom:.5rem;">⚡ LAYOUT: EstiloGettingToKnow.astro · Turquesa #00F2FE & Tribal ⚡</div>
      <h2 style="text-align:center;font-size:2rem;border:none;padding:0;margin-bottom:.5rem;font-family:'Orbitron',sans-serif;">GETTING TO KNOW</h2>
      <p style="text-align:center;color:#94A3B8;font-style:italic;margin-bottom:2rem;">Era de las Tribus y Reinos · Fichas de Personajes + Novela Completa</p>

      <h2>Fichas de Personajes — Tribu Häscht</h2>
      <div class="fichas-grid">
        <div class="ficha-card">
          <h3>⚔ HEYA</h3>
          <p><strong>Rol:</strong> Ex-guardia de frontera / Agricultor</p>
          <p><strong>Edad:</strong> 23-25 años · Humano</p>
          <p><strong>Tribu:</strong> Häscht (Ex-Gricái)</p>
          <p><strong>Personalidad:</strong> Principista, reflexivo, reservado, leal y compasivo.</p>
          <p><strong>Arco:</strong> De la resignación en la torre del bosque al amor de Ameřa.</p>
        </div>
        <div class="ficha-card">
          <h3>🏹 AMEŘA</h3>
          <p><strong>Rol:</strong> Cazadora tribal</p>
          <p><strong>Edad:</strong> 19-21 años · Humana</p>
          <p><strong>Tribu:</strong> Häscht</p>
          <p><strong>Personalidad:</strong> Enérgica, alegre, ingeniosa, leal y de espíritu libre.</p>
          <p><strong>Arco:</strong> Transforma su decepción en orgullo como la mejor cazadora.</p>
        </div>
        <div class="ficha-card">
          <h3>🌟 HESIS</h3>
          <p><strong>Rol:</strong> Guía espiritual / Recuerdo viviente</p>
          <p><strong>Edad:</strong> ~12 años (en memoria) · Espíritu</p>
          <p><strong>Personalidad:</strong> Dulce, sabia, afectuosa y firme con su hermano.</p>
          <p><strong>Arco:</strong> Actúa como la luz de la conciencia de Heya en sus trances.</p>
        </div>
        <div class="ficha-card">
          <h3>🛡 LOMEN</h3>
          <p><strong>Rol:</strong> Capitán de la guardia Häscht</p>
          <p><strong>Edad:</strong> 24-26 años · Humano</p>
          <p><strong>Personalidad:</strong> Protector, desconfiado de extraños, sensato y fraternal.</p>
          <p><strong>Arco:</strong> Del recelo al respeto por Heya tras comprobar su lealtad.</p>
        </div>
        <div class="ficha-card">
          <h3>👑 DERK</h3>
          <p><strong>Rol:</strong> Patriarca / Líder tribal</p>
          <p><strong>Edad:</strong> 50-54 años · Humano</p>
          <p><strong>Personalidad:</strong> Justo, exigente, tradicional pero sabio y receptivo.</p>
          <p><strong>Arco:</strong> Aplica el lema "salva a quien salva, protege a quien protege".</p>
        </div>
      </div>

      <hr class="story-divider">
      <h2>Texto de la Novela</h2>
      {gtk_main_html if gtk_main_html else '<p>Texto de la historia disponible en la edición original.</p>'}

      <div style="text-align:center;margin-top:2rem;">
        <button class="back-btn" onclick="switchView('portal')" style="background:#00F2FE;color:#000;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- ════════════ VIEW: LA PIEDRA SIN PULIR ════════════ -->
  <section id="view-emerald" class="view layout-emerald">
    <div class="emerald-wrap">
      <div style="text-align:center;font-size:.8rem;color:#34D399;font-weight:700;letter-spacing:2px;margin-bottom:.5rem;">🌿 LAYOUT: EstiloLaPiedraSinPulir.astro · Esmeralda #10B981 & Tierra 🌿</div>
      <h2 style="text-align:center;font-size:2.2rem;border:none;padding:0;margin-bottom:.5rem;">LA PIEDRA SIN PULIR</h2>
      <p style="text-align:center;color:#34D399;font-style:italic;margin-bottom:2rem;">Fábula del Señor de las Siete Esposas · Manuscrito Completo</p>

      {piedra_html}

      <div style="text-align:center;margin-top:2rem;">
        <button class="back-btn" onclick="switchView('portal')" style="background:#10B981;color:#000;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- UNIVERSAL FOOTER -->
  <footer class="univ-footer">
    <div class="footer-links">
      <span onclick="switchView('portal')">🏠 Portal Principal</span>
      <span onclick="switchView('ruk')">⚔ Ruk el Héroe</span>
      <span onclick="switchView('forgotten')">🗡 Forgotten Sword</span>
      <span onclick="switchView('sangre')">🩸 Sangre y Cadáveres</span>
      <span onclick="switchView('republic')">📜 Republic</span>
      <span onclick="switchView('cyber')">⚡ Getting to Know</span>
      <span onclick="switchView('emerald')">🌿 La Piedra sin Pulir</span>
    </div>
    <p>&copy; 2026 UNIVERSO LIGNUM — Monorepositorio Literario con Scoped CSS Layouts. 6 Universos · {len(ruk_caps_raw) + len(fs_caps_raw)}+ Capítulos Integrados.</p>
  </footer>

  <script>
    const META = {{
      portal: {{ sub: 'Portal Principal • 6 Universos • Scoped CSS Layouts', pill: 'pill-portal' }},
      ruk:    {{ sub: 'EstiloImperativoRuk.astro · Blanco & Dorado #D4AF37', pill: 'pill-ruk' }},
      forgotten: {{ sub: 'EstiloForgottenSword.astro · Gótico #8B0000', pill: 'pill-forgotten' }},
      sangre: {{ sub: 'EstiloSangreCadaveres.astro · Escarlata #CA0B0B', pill: 'pill-sangre' }},
      republic: {{ sub: 'EstiloMarriageRepublic.astro · Marrón Claro #8B5A2B', pill: 'pill-republic' }},
      cyber:  {{ sub: 'EstiloGettingToKnow.astro · Turquesa #00F2FE', pill: 'pill-cyber' }},
      emerald: {{ sub: 'EstiloLaPiedraSinPulir.astro · Esmeralda #10B981', pill: 'pill-emerald' }}
    }};

    function switchView(id) {{
      document.querySelectorAll('.view').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.pill').forEach(el => el.classList.remove('active'));
      const v = document.getElementById('view-' + id);
      if (v) v.classList.add('active');
      const m = META[id];
      if (m) {{
        document.getElementById('active-sub').innerText = m.sub;
        const p = document.getElementById(m.pill);
        if (p) p.classList.add('active');
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function scrollToAnchor(anchor) {{
      setTimeout(() => {{
        const el = document.getElementById(anchor);
        if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}, 100);
    }}
  </script>

</body>
</html>'''

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
os.makedirs(os.path.dirname(DIST_PATH), exist_ok=True)

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

with open(DIST_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

ruk_count = len(ruk_caps_raw)
fs_count = len(fs_caps_raw)
print(f'[OK] Portal compilado con:')
print(f'  - Ruk el Héroe: {ruk_count} capítulos')
print(f'  - Forgotten Sword: {fs_count} capítulos')
print(f'  - Sangre y Cadáveres: texto + conceptualización')
print(f'  - The Marriage of the Republic: texto completo')
print(f'  - Getting to Know: 5 fichas + novela')
print(f'  - La Piedra sin Pulir: manuscrito completo')
print(f'')
print(f'[OUT] {OUT_PATH}')
print(f'[OUT] {DIST_PATH}')
