import os
import re
import shutil

# Root directories
ruk_dir = r"c:\Users\Barra\Documents\Ruk - Historia Completa"
edited_dir = os.path.join(ruk_dir, "Ruk_Editado")
output_html = os.path.join(ruk_dir, "index.html")

chapter_files = [
    ("Capitulo_01_El_peso_de_la_partida.md", "Capítulo 1: El peso de la partida"),
    ("Capitulo_02_Refugio_y_promesa.md", "Capítulo 2: Refugio y promesa"),
    ("Capitulo_03_El_frente_de_Ende.md", "Capítulo 3: El frente de Ende"),
    ("Capitulo_04_Manantial_de_sanacion.md", "Capítulo 4: Manantial de sanación"),
    ("Capitulo_05_La_marea_enemiga.md", "Capítulo 5: La marea enemiga"),
    ("Capitulo_06_Rutas_de_suministros.md", "Capítulo 6: Rutas de suministros"),
    ("Capitulo_07_Forjando_guerreros.md", "Capítulo 7: Forjando guerreros"),
    ("Capitulo_08_La_union_de_las_tribus.md", "Capítulo 8: La unión de las tribus"),
    ("Capitulo_09_Heroes_de_Davir.md", "Capítulo 9: Héroes de Davir"),
]

chapters_html = []
for idx, (filename, title) in enumerate(chapter_files, start=1):
    file_path = os.path.join(edited_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    lines = raw_text.splitlines()
    filtered = [l for l in lines if not re.match(r'^\s*#\s*Capítulo', l) and not re.match(r'^\s*---\s*$', l)]
    clean_text = "\n".join(filtered)

    paragraphs = re.split(r'(\r?\n){2,}', clean_text)
    p_blocks = []
    for p in paragraphs:
        trimmed = p.strip()
        if trimmed:
            p_blocks.append(f"<p>{trimmed}</p>")

    body_content = "\n".join(p_blocks)
    active_class = "active-chapter" if idx == 1 else ""

    prev_btn = f"<button class='btn-nav-ch' onclick='switchChapter({idx - 1})'>← Capítulo Anterior</button>" if idx > 1 else "<span></span>"
    next_btn = f"<button class='btn-nav-ch' onclick='switchChapter({idx + 1})'>Capítulo Siguiente →</button>" if idx < 9 else "<span></span>"

    ch_html = f"""
        <article class="chapter-content {active_class}" id="capitulo-{idx}" data-chapter="{idx}">
            <div class="chapter-header">
                <span class="chapter-badge">✦ CAPÍTULO 0{idx} ✦</span>
                <h2 class="chapter-title">{title}</h2>
            </div>
            <div class="chapter-text-body">
                {body_content}
            </div>
            <div class="chapter-nav-bottom">
                {prev_btn}
                <button class="btn-nav-ch btn-gold-fill" onclick="window.scrollTo({{top:0, behavior:'smooth'}})">↑ Volver Arriba</button>
                {next_btn}
            </div>
        </article>
"""
    chapters_html.append(ch_html)

all_chapters_html = "\n\n".join(chapters_html)

full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruk el Héroe - Saga Fantástica Completa</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Lora:ital,wght@0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #FAF8F5;
            --bg-card: #FFFFFF;
            --bg-secondary: #F3EFE6;
            --text-main: #2C261F;
            --text-muted: #665D52;
            --gold-primary: #D4AF37;
            --gold-light: #F4E8C1;
            --gold-dark: #9E8237;
            --gold-border: #E0C775;
            --gold-shadow: rgba(212, 175, 55, 0.25);
            --card-shadow: 0 10px 30px rgba(158, 130, 55, 0.08);
            --font-reader-size: 1.15rem;
            --radius-md: 14px;
            --radius-lg: 20px;
        }}

        /* Themes */
        body.theme-sepia {{
            --bg-base: #F4EFE0;
            --bg-card: #FDFBF5;
            --bg-secondary: #E8E0CE;
            --text-main: #382D22;
            --text-muted: #6E5F50;
            --gold-primary: #B8860B;
            --gold-light: #EBD9B0;
            --gold-dark: #8B6508;
            --gold-border: #D4B263;
        }}

        body.theme-dark {{
            --bg-base: #12100E;
            --bg-card: #1A1714;
            --bg-secondary: #24201C;
            --text-main: #EFE4CE;
            --text-muted: #A89B88;
            --gold-primary: #FFD700;
            --gold-light: #3D351B;
            --gold-dark: #C5A059;
            --gold-border: #7A6321;
            --gold-shadow: rgba(255, 215, 0, 0.2);
            --card-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }}

        html {{
            scroll-behavior: smooth;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: background-color 0.4s ease, color 0.4s ease;
            position: relative;
        }}

        /* Top Progress Bar */
        .progress-bar-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: rgba(212, 175, 55, 0.15);
            z-index: 1000;
        }}

        .progress-bar-fill {{
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #B8860B, #D4AF37, #FFD700);
            box-shadow: 0 0 10px var(--gold-primary);
            transition: width 0.1s ease-out;
        }}

        /* Header / Navbar */
        .app-header {{
            width: 100%;
            max-width: 1200px;
            padding: 20px 30px;
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
        }}

        .brand-title {{
            font-family: 'Cinzel', serif;
            font-size: 1.6rem;
            font-weight: 900;
            color: var(--text-main);
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
        }}

        .brand-title span {{
            color: var(--gold-primary);
        }}

        .header-actions {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .btn-header-home {{
            background: transparent;
            border: 1.5px solid var(--gold-primary);
            color: var(--gold-dark);
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-header-home:hover {{
            background: var(--gold-primary);
            color: #FFFFFF;
            transform: translateY(-2px);
        }}

        /* Layout Container */
        .page-wrapper {{
            width: 100%;
            max-width: 1100px;
            padding: 40px 20px;
            flex: 1;
        }}

        /* VISTA 1: MENÚ PRINCIPAL / HUB */
        .main-container {{
            width: 100%;
            min-height: 75vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}

        .main-container.hidden {{
            display: none !important;
        }}

        .main-container.closing {{
            animation: fadeOut 0.25s ease-in forwards;
        }}

        .main-container.fadeIn {{
            animation: fadeIn 0.4s ease-out forwards;
        }}

        /* Hero Banner */
        .hero-banner {{
            background: var(--bg-card);
            border: 2px solid var(--gold-border);
            border-radius: var(--radius-lg);
            padding: 50px 35px;
            box-shadow: var(--card-shadow);
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
            width: 100%;
            max-width: 900px;
        }}

        .hero-banner::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, var(--gold-shadow) 0%, transparent 60%);
            pointer-events: none;
            opacity: 0.6;
        }}

        .hero-emblem {{
            font-size: 3rem;
            color: var(--gold-primary);
            margin-bottom: 15px;
        }}

        .hero-title {{
            font-family: 'Cinzel', serif;
            font-size: 2.8rem;
            font-weight: 900;
            color: var(--text-main);
            margin-bottom: 15px;
            letter-spacing: 2px;
        }}

        .hero-subtitle {{
            font-family: 'Lora', serif;
            font-style: italic;
            font-size: 1.25rem;
            color: var(--gold-dark);
            margin-bottom: 25px;
        }}

        .hero-desc {{
            font-size: 1.05rem;
            line-height: 1.7;
            color: var(--text-muted);
            max-width: 750px;
            margin: 0 auto 30px auto;
        }}

        .hero-badges {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
        }}

        .badge-item {{
            background: var(--bg-secondary);
            border: 1px solid var(--gold-border);
            color: var(--text-main);
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }}

        /* Portal Navigation Grid */
        .hub-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 900px;
        }}

        .btn-hub-card {{
            background: var(--bg-card);
            border: 2px solid var(--gold-border);
            border-radius: var(--radius-md);
            padding: 30px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
            box-shadow: var(--card-shadow);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
        }}

        .btn-hub-card:hover {{
            transform: translateY(-6px);
            border-color: var(--gold-primary);
            box-shadow: 0 15px 35px var(--gold-shadow);
            background: var(--bg-card);
        }}

        .hub-icon {{
            font-size: 2.5rem;
            color: var(--gold-primary);
        }}

        .hub-card-title {{
            font-family: 'Cinzel', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .hub-card-desc {{
            font-size: 0.9rem;
            color: var(--text-muted);
            line-height: 1.4;
        }}

        /* VISTAS SECUNDARIAS */
        .seccion-oculta {{
            display: none;
            width: 100%;
            margin: 0 auto;
        }}

        .seccion-oculta.active {{
            display: block;
            animation: fadeIn 0.4s ease-out forwards;
        }}

        .seccion-oculta.closing {{
            animation: fadeOut 0.25s ease-in forwards;
        }}

        /* Header for secondary sections */
        .section-nav-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }}

        .btn-back-main {{
            padding: 10px 24px;
            background: var(--bg-card);
            color: var(--gold-dark);
            border: 1.5px solid var(--gold-primary);
            border-radius: 25px;
            cursor: pointer;
            font-weight: 700;
            font-size: 0.95rem;
            transition: all 0.25s ease;
            box-shadow: var(--card-shadow);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .btn-back-main:hover {{
            background: var(--gold-primary);
            color: #FFFFFF;
            transform: translateX(-4px);
        }}

        .section-header-title {{
            font-family: 'Cinzel', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        /* Reader Controls Bar */
        .reader-controls-bar {{
            background: var(--bg-card);
            border: 1px solid var(--gold-border);
            border-radius: var(--radius-md);
            padding: 15px 25px;
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
            box-shadow: var(--card-shadow);
        }}

        .control-group {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .control-label {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .btn-control-tool {{
            background: var(--bg-secondary);
            border: 1px solid var(--gold-border);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .btn-control-tool:hover {{
            background: var(--gold-primary);
            color: #FFFFFF;
        }}

        .theme-select {{
            background: var(--bg-secondary);
            border: 1px solid var(--gold-border);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            outline: none;
        }}

        /* Reader Layout */
        .reader-layout {{
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 30px;
            align-items: start;
        }}

        @media (max-width: 900px) {{
            .reader-layout {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Chapter Sidebar */
        .chapter-sidebar {{
            background: var(--bg-card);
            border: 1.5px solid var(--gold-border);
            border-radius: var(--radius-md);
            padding: 20px;
            box-shadow: var(--card-shadow);
            position: sticky;
            top: 90px;
        }}

        .sidebar-title {{
            font-family: 'Cinzel', serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--gold-dark);
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--gold-border);
        }}

        .chapter-list-menu {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .btn-ch-item {{
            width: 100%;
            text-align: left;
            padding: 10px 14px;
            background: transparent;
            border: 1px solid transparent;
            border-radius: 8px;
            color: var(--text-muted);
            font-size: 0.92rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .btn-ch-item:hover {{
            background: var(--bg-secondary);
            color: var(--text-main);
            border-color: var(--gold-border);
        }}

        .btn-ch-item.active {{
            background: var(--gold-light);
            color: var(--gold-dark);
            border-color: var(--gold-primary);
            font-weight: 700;
        }}

        /* Chapter Content */
        .chapter-container-main {{
            background: var(--bg-card);
            border: 1.5px solid var(--gold-border);
            border-radius: var(--radius-lg);
            padding: 45px 40px;
            box-shadow: var(--card-shadow);
            min-height: 600px;
        }}

        @media (max-width: 600px) {{
            .chapter-container-main {{
                padding: 25px 20px;
            }}
        }}

        .chapter-content {{
            display: none;
        }}

        .chapter-content.active-chapter {{
            display: block;
            animation: fadeIn 0.35s ease-out forwards;
        }}

        .chapter-header {{
            text-align: center;
            margin-bottom: 35px;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--gold-border);
        }}

        .chapter-badge {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--gold-primary);
            letter-spacing: 1.5px;
        }}

        .chapter-title {{
            font-family: 'Cinzel', serif;
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--text-main);
            margin-top: 8px;
        }}

        .chapter-text-body {{
            font-family: 'Lora', serif;
            font-size: var(--font-reader-size);
            line-height: 1.85;
            color: var(--text-main);
        }}

        /* Sangría de primera línea 0.75em */
        .chapter-text-body p {{
            text-indent: 0.75em;
            margin-bottom: 1.3em;
        }}

        .chapter-nav-bottom {{
            margin-top: 50px;
            padding-top: 25px;
            border-top: 1px solid var(--gold-border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }}

        .btn-nav-ch {{
            padding: 10px 20px;
            background: var(--bg-secondary);
            border: 1px solid var(--gold-border);
            color: var(--text-main);
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.25s ease;
        }}

        .btn-nav-ch:hover {{
            border-color: var(--gold-primary);
            color: var(--gold-dark);
            transform: translateY(-2px);
        }}

        .btn-gold-fill {{
            background: var(--gold-primary);
            color: #FFFFFF;
            border-color: var(--gold-primary);
        }}

        .btn-gold-fill:hover {{
            background: var(--gold-dark);
            color: #FFFFFF;
        }}

        /* Personajes Grid */
        .personajes-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }}

        .card-personaje {{
            background: var(--bg-card);
            border: 1.5px solid var(--gold-border);
            border-radius: var(--radius-md);
            padding: 30px 25px;
            box-shadow: var(--card-shadow);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}

        .card-personaje:hover {{
            transform: translateY(-5px);
            border-color: var(--gold-primary);
            box-shadow: 0 15px 30px var(--gold-shadow);
        }}

        .avatar-emblem {{
            width: 65px;
            height: 65px;
            border-radius: 50%;
            background: var(--bg-secondary);
            border: 2px solid var(--gold-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            color: var(--gold-primary);
            margin-bottom: 20px;
        }}

        .personaje-nombre {{
            font-family: 'Cinzel', serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 6px;
        }}

        .personaje-rol {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--gold-dark);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 15px;
        }}

        .personaje-desc {{
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--text-muted);
        }}

        /* Actos Timeline */
        .actos-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}

        .card-acto {{
            background: var(--bg-card);
            border: 1.5px solid var(--gold-border);
            border-radius: var(--radius-md);
            padding: 35px;
            box-shadow: var(--card-shadow);
            position: relative;
        }}

        .acto-badge {{
            display: inline-block;
            background: var(--gold-primary);
            color: #FFFFFF;
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 15px;
        }}

        .acto-titulo {{
            font-family: 'Cinzel', serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 12px;
        }}

        .acto-desc {{
            font-size: 1.02rem;
            line-height: 1.7;
            color: var(--text-muted);
        }}

        /* Moraleja & Citas */
        .citas-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}

        .quote-card {{
            background: var(--bg-card);
            border: 1.5px dashed var(--gold-primary);
            border-radius: var(--radius-md);
            padding: 30px 25px;
            box-shadow: var(--card-shadow);
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }}

        .quote-card:hover {{
            background: var(--bg-secondary);
            border-style: solid;
            transform: translateY(-4px);
        }}

        .quote-icon {{
            font-size: 2rem;
            color: var(--gold-primary);
            margin-bottom: 10px;
        }}

        .quote-text {{
            font-family: 'Lora', serif;
            font-style: italic;
            font-size: 1.1rem;
            color: var(--text-main);
            line-height: 1.6;
            margin-bottom: 15px;
        }}

        .quote-author {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--gold-dark);
            text-align: right;
        }}

        .copy-hint {{
            position: absolute;
            bottom: 10px;
            left: 20px;
            font-size: 0.75rem;
            color: var(--gold-dark);
            opacity: 0.7;
        }}

        /* Toast Alert */
        .toast-notification {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: var(--gold-primary);
            color: #FFFFFF;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: 700;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            display: none;
            z-index: 2000;
            animation: fadeIn 0.3s ease-out forwards;
        }}

        /* Footer */
        .app-footer {{
            width: 100%;
            padding: 30px 20px;
            text-align: center;
            border-top: 1px solid var(--gold-border);
            background: var(--bg-card);
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-top: 60px;
        }}

        .footer-gold-text {{
            color: var(--gold-primary);
            font-weight: 700;
        }}

        /* Animations */
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(18px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes fadeOut {{
            from {{
                opacity: 1;
                transform: translateY(0);
            }}
            to {{
                opacity: 0;
                transform: translateY(18px);
            }}
        }}
    </style>
</head>
<body>

    <!-- Reading Progress Bar -->
    <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBar"></div>
    </div>

    <!-- Header Navigation -->
    <header class="app-header">
        <div class="brand-title" onclick="regresarAlMenu()">
            🛡️ <span>Ruk</span> el Héroe
        </div>
        <div class="header-actions">
            <button class="btn-header-home" onclick="regresarAlMenu()">
                🏠 Menú Principal
            </button>
        </div>
    </header>

    <!-- Main Wrapper -->
    <div class="page-wrapper">

        <!-- MENÚ PRINCIPAL / HUB (VISTA 1) -->
        <main class="main-container" id="menu-principal">
            <div class="hero-banner">
                <div class="hero-emblem">⚔️</div>
                <h1 class="hero-title">Ruk el Héroe</h1>
                <p class="hero-subtitle">«Una historia de valentía, amistad y la forja de un destino en tiempos de guerra»</p>
                <p class="hero-desc">
                    A los doce años, mientras jugaban a combates imaginarios bajo la sombra de los árboles, Ruk y sus amigos descubrieron que la guerra se aproximaba. Esta es la crónica de su viaje, la resistencia de las tribus y la unión de los valientes frente a la adversidad.
                </p>
                <div class="hero-badges">
                    <span class="badge-item">✨ Edición Completa</span>
                    <span class="badge-item">📖 9 Capítulos</span>
                    <span class="badge-item">👑 Estética Blanco & Dorado</span>
                </div>
            </div>

            <!-- Portal Options Grid -->
            <div class="hub-grid">
                <div class="btn-hub-card" onclick="mostrarSeccion('seccion-lectura', 'lectura')">
                    <div class="hub-icon">📖</div>
                    <h3 class="hub-card-title">Lectura de Capítulos</h3>
                    <p class="hub-card-desc">Explora la saga completa desde el Capítulo 1 hasta el 9 con controles de lectura personalizados.</p>
                </div>

                <div class="btn-hub-card" onclick="mostrarSeccion('seccion-personajes', 'personajes')">
                    <div class="hub-icon">🛡️</div>
                    <h3 class="hub-card-title">Fichas de Personajes</h3>
                    <p class="hub-card-desc">Conoce a Ruk, Kairo, Riav, Ruval, Muvar, Orwin y los valientes defensores.</p>
                </div>

                <div class="btn-hub-card" onclick="mostrarSeccion('seccion-actos', 'actos')">
                    <div class="hub-icon">🏛️</div>
                    <h3 class="hub-card-title">Estructura en Actos</h3>
                    <p class="hub-card-desc">Recorre la cronología escénica del ascenso de los héroes y las batallas decisivas.</p>
                </div>

                <div class="btn-hub-card" onclick="mostrarSeccion('seccion-moraleja', 'citas')">
                    <div class="hub-icon">📜</div>
                    <h3 class="hub-card-title">Citas y Reflexiones</h3>
                    <p class="hub-card-desc">Descubre las frases célebres de la historia y copia tus favoritas con un solo clic.</p>
                </div>
            </div>
        </main>

        <!-- VISTA SECUNDARIA 1: LECTURA DE CAPÍTULOS -->
        <section class="seccion-oculta" id="seccion-lectura">
            <div class="section-nav-bar">
                <button class="btn-back-main" onclick="ocultarSeccion('seccion-lectura')">
                    ← Volver al Menú Principal
                </button>
                <h2 class="section-header-title">📖 Saga Completa</h2>
            </div>

            <!-- Controls Bar -->
            <div class="reader-controls-bar">
                <div class="control-group">
                    <span class="control-label">Tamaño de letra:</span>
                    <button class="btn-control-tool" onclick="adjustFontSize(-0.1)">A-</button>
                    <button class="btn-control-tool" onclick="resetFontSize()">A</button>
                    <button class="btn-control-tool" onclick="adjustFontSize(0.1)">A+</button>
                </div>
                <div class="control-group">
                    <span class="control-label">Tema Visual:</span>
                    <select class="theme-select" id="themeSelect" onchange="changeTheme(this.value)">
                        <option value="default">👑 Blanco Imperial & Dorado</option>
                        <option value="sepia">📜 Pergamino Sepia</option>
                        <option value="dark">🌙 Obsidiana Dorada</option>
                    </select>
                </div>
                <div class="control-group">
                    <span class="control-label" id="readingStats">📊 0% leído (~0 min)</span>
                </div>
            </div>

            <!-- Reader Layout -->
            <div class="reader-layout">
                <!-- Sidebar -->
                <aside class="chapter-sidebar">
                    <h3 class="sidebar-title">Índice de Capítulos</h3>
                    <ul class="chapter-list-menu">
                        <li><button class="btn-ch-item active" id="menu-ch-1" onclick="switchChapter(1)">01. El peso de la partida</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-2" onclick="switchChapter(2)">02. Refugio y promesa</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-3" onclick="switchChapter(3)">03. El frente de Ende</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-4" onclick="switchChapter(4)">04. Manantial de sanación</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-5" onclick="switchChapter(5)">05. La marea enemiga</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-6" onclick="switchChapter(6)">06. Rutas de suministros</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-7" onclick="switchChapter(7)">07. Forjando guerreros</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-8" onclick="switchChapter(8)">08. La unión de las tribus</button></li>
                        <li><button class="btn-ch-item" id="menu-ch-9" onclick="switchChapter(9)">09. Héroes de Davir</button></li>
                    </ul>
                </aside>

                <!-- Main Chapters Container -->
                <div class="chapter-container-main">
                    {all_chapters_html}
                </div>
            </div>
        </section>

        <!-- VISTA SECUNDARIA 2: FICHAS DE PERSONAJES -->
        <section class="seccion-oculta" id="seccion-personajes">
            <div class="section-nav-bar">
                <button class="btn-back-main" onclick="ocultarSeccion('seccion-personajes')">
                    ← Volver al Menú Principal
                </button>
                <h2 class="section-header-title">🛡️ Galería de Héroes</h2>
            </div>

            <div class="personajes-grid">
                <a href="personajes/ficha_ruk.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">🗡️</div>
                        <h3 class="personaje-nombre">Ruk</h3>
                        <div class="personaje-rol">Protagonista / Joven Guerrero</div>
                        <p class="personaje-desc">Muchacho de doce años de corazón noble y espíritu observador. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>

                <a href="personajes/ficha_kairo.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">👑</div>
                        <h3 class="personaje-nombre">Kairo</h3>
                        <div class="personaje-rol">Padre de Ruk / Lider Defensor</div>
                        <p class="personaje-desc">Hombre imponente cuya sola presencia inspira seguridad y serenidad. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>

                <a href="personajes/ficha_riav.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">🏹</div>
                        <h3 class="personaje-nombre">Riav</h3>
                        <div class="personaje-rol">Compañera Pelirroja / Arquera</div>
                        <p class="personaje-desc">Joven decidida de temple inquebrantable. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>

                <a href="personajes/ficha_ruval.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">⚡</div>
                        <h3 class="personaje-nombre">Ruval</h3>
                        <div class="personaje-rol">Amigo Impulsivo / Combatiente</div>
                        <p class="personaje-desc">Lleno de energía y curiosidad sin límites. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>

                <a href="personajes/ficha_muvar.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">🌿</div>
                        <h3 class="personaje-nombre">Muvar</h3>
                        <div class="personaje-rol">Compañero Entusiasta</div>
                        <p class="personaje-desc">Amigo leal que admira el paisaje del valle. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>

                <a href="personajes/ficha_orwin.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">🎯</div>
                        <h3 class="personaje-nombre">Orwin</h3>
                        <div class="personaje-rol">Niño Refugiado / Aliado</div>
                        <p class="personaje-desc">Superviviente del pueblo destruido que crea 'Lanzaditas'. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>

                <a href="personajes/ficha_tehm.html" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="card-personaje">
                        <div class="avatar-emblem">🏛️</div>
                        <h3 class="personaje-nombre">Señor Tehm</h3>
                        <div class="personaje-rol">Líder del Pueblo Hospedante</div>
                        <p class="personaje-desc">Líder sensato y compasivo que acoge a los refugiados. Haz clic para abrir su ficha completa en pergamino.</p>
                    </div>
                </a>
            </div>
        </section>

        <!-- VISTA SECUNDARIA 3: ESTRUCTURA EN ACTOS -->
        <section class="seccion-oculta" id="seccion-actos">
            <div class="section-nav-bar">
                <button class="btn-back-main" onclick="ocultarSeccion('seccion-actos')">
                    ← Volver al Menú Principal
                </button>
                <h2 class="section-header-title">🏛️ Estructura de la Saga</h2>
            </div>

            <div class="actos-container">
                <div class="card-acto">
                    <span class="acto-badge">ACTO I</span>
                    <h3 class="acto-titulo">El Peso de la Partida y la Llegada de los Refugiados</h3>
                    <p class="acto-desc">
                        En los días de tranquilidad previa, Ruk y sus amigos disfrutan de juegos inocentes hasta que la sombra de la guerra contra el Reino Dementi irrumpe en la aldea. Los adultos se preparan para partir al frente, mientras sesenta y ocho refugiados al mando de Dael llegan buscando cobijo.
                    </p>
                </div>

                <div class="card-acto">
                    <span class="acto-badge">ACTO II</span>
                    <h3 class="acto-titulo">Manantiales de Sanación y las Rutas de Suministros</h3>
                    <p class="acto-desc">
                        A medida que el conflicto se intensifica en el frente de Ende, la logística de suministros y el auxilio médico se vuelven vitales. Los jóvenes apoyan en la retaguardia, asegurando que los guerreros tengan víveres y refugio en momentos de angustia.
                    </p>
                </div>

                <div class="card-acto">
                    <span class="acto-badge">ACTO III</span>
                    <h3 class="acto-titulo">La Unión de las Tribus y los Héroes de Davir</h3>
                    <p class="acto-desc">
                        Frente a la marea enemiga, las tribus dispersas deben forjar guerreros y unir sus fuerzas en una sola causa. Ruk asume el peso de su legado, convirtiéndose en el símbolo de esperanza y valentía que unifica a los héroes de Davir.
                    </p>
                </div>
            </div>
        </section>

        <!-- VISTA SECUNDARIA 4: MORALEJA Y CITAS -->
        <section class="seccion-oculta" id="seccion-moraleja">
            <div class="section-nav-bar">
                <button class="btn-back-main" onclick="ocultarSeccion('seccion-moraleja')">
                    ← Volver al Menú Principal
                </button>
                <h2 class="section-header-title">📜 Frases e Inspiración</h2>
            </div>

            <p style="text-align: center; color: var(--text-muted); margin-bottom: 25px;">
                💡 <em>Haz clic en cualquier recuadro de frase para copiarla instantáneamente al portapapeles.</em>
            </p>

            <div class="citas-grid">
                <div class="quote-card" onclick="copyQuote('Mira, Ruk. Son cosas que se deben hacer, es una responsabilidad defender al reino.')">
                    <div class="quote-icon">“</div>
                    <p class="quote-text">«Mira, Ruk. Son cosas que se deben hacer, es una responsabilidad defender al reino.»</p>
                    <div class="quote-author">— Kairo</div>
                    <div class="copy-hint">📋 Clic para copiar</div>
                </div>

                <div class="quote-card" onclick="copyQuote('Aunque a veces no nos gusten las cosas que llegan, uno debe ser firme y continuar.')">
                    <div class="quote-icon">“</div>
                    <p class="quote-text">«Aunque a veces no nos gusten las cosas que llegan, uno debe ser firme y continuar. Tienes un gran potencial.»</p>
                    <div class="quote-author">— Padre de Riav</div>
                    <div class="copy-hint">📋 Clic para copiar</div>
                </div>

                <div class="quote-card" onclick="copyQuote('La guerra es mala, mueren personas. Por eso debemos cuidar a quienes amamos.')">
                    <div class="quote-icon">“</div>
                    <p class="quote-text">«La guerra es mala, mueren personas... por eso debemos ser firmes y proteger nuestro hogar.»</p>
                    <div class="quote-author">— Riav</div>
                    <div class="copy-hint">📋 Clic para copiar</div>
                </div>
            </div>
        </section>

    </div>

    <!-- Notification Toast -->
    <div class="toast-notification" id="toast">✨ ¡Frase copiada al portapapeles!</div>

    <!-- App Footer -->
    <footer class="app-footer">
        ✦ <span class="footer-gold-text">Ruk el Héroe</span> — Edición Completa en Blanco y Dorado ✦
    </footer>

    <!-- View Transition & Interactive Logic -->
    <script>
        function mostrarSeccion(idTarget, hash) {{
            const menu = document.getElementById('menu-principal');
            const target = document.getElementById(idTarget);

            ['seccion-lectura', 'seccion-personajes', 'seccion-actos', 'seccion-moraleja'].forEach(secId => {{
                if (secId !== idTarget) {{
                    const el = document.getElementById(secId);
                    if (el) {{
                        el.classList.remove('active', 'closing');
                        el.style.display = 'none';
                    }}
                }}
            }});

            menu.classList.add('closing');

            setTimeout(() => {{
                menu.classList.add('hidden');
                menu.classList.remove('closing');

                target.style.display = 'block';
                target.classList.remove('closing');
                target.classList.add('active');

                window.location.hash = hash;
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
                updateReadingStats();
            }}, 250);
        }}

        function ocultarSeccion(idTarget) {{
            const target = document.getElementById(idTarget);
            const menu = document.getElementById('menu-principal');

            target.classList.add('closing');

            setTimeout(() => {{
                target.classList.remove('active', 'closing');
                target.style.display = 'none';

                menu.classList.remove('hidden');
                menu.classList.add('fadeIn');

                window.location.hash = '';
                window.scrollTo({{ top: 0, behavior: 'smooth' }});

                setTimeout(() => {{
                    menu.classList.remove('fadeIn');
                }}, 400);
            }}, 250);
        }}

        function regresarAlMenu() {{
            ['seccion-lectura', 'seccion-personajes', 'seccion-actos', 'seccion-moraleja'].forEach(secId => {{
                const el = document.getElementById(secId);
                if (el && el.style.display !== 'none') {{
                    ocultarSeccion(secId);
                }}
            }});
        }}

        function switchChapter(chNum) {{
            document.querySelectorAll('.chapter-content').forEach(el => {{
                el.classList.remove('active-chapter');
            }});
            document.querySelectorAll('.btn-ch-item').forEach(el => {{
                el.classList.remove('active');
            }});

            const targetCh = document.getElementById('capitulo-' + chNum);
            const targetBtn = document.getElementById('menu-ch-' + chNum);

            if (targetCh) {{
                targetCh.classList.add('active-chapter');
            }}
            if (targetBtn) {{
                targetBtn.classList.add('active');
            }}

            window.scrollTo({{ top: 120, behavior: 'smooth' }});
            updateReadingStats();
        }}

        let currentFontSize = 1.15;
        function adjustFontSize(delta) {{
            currentFontSize = Math.max(0.9, Math.min(1.6, currentFontSize + delta));
            document.documentElement.style.setProperty('--font-reader-size', currentFontSize + 'rem');
        }}

        function resetFontSize() {{
            currentFontSize = 1.15;
            document.documentElement.style.setProperty('--font-reader-size', '1.15rem');
        }}

        function changeTheme(theme) {{
            document.body.classList.remove('theme-sepia', 'theme-dark');
            if (theme === 'sepia') {{
                document.body.classList.add('theme-sepia');
            }} else if (theme === 'dark') {{
                document.body.classList.add('theme-dark');
            }}
        }}

        window.addEventListener('scroll', () => {{
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
            document.getElementById('progressBar').style.width = progress + '%';
            updateReadingStats();
        }});

        function updateReadingStats() {{
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const pct = docHeight > 0 ? Math.min(100, Math.round((scrollTop / docHeight) * 100)) : 0;
            const remMin = Math.max(0, Math.ceil((100 - pct) * 0.25));
            
            const statsEl = document.getElementById('readingStats');
            if (statsEl) {{
                statsEl.innerText = '📊 ' + pct + '% leído (~' + remMin + ' min restantes)';
            }}
        }}

        function copyQuote(text) {{
            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('toast');
                toast.style.display = 'block';
                setTimeout(() => {{
                    toast.style.display = 'none';
                }}, 2500);
            }});
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            const hash = window.location.hash.replace('#', '');
            if (hash === 'lectura') mostrarSeccion('seccion-lectura', 'lectura');
            else if (hash === 'personajes') mostrarSeccion('seccion-personajes', 'personajes');
            else if (hash === 'actos') mostrarSeccion('seccion-actos', 'actos');
            else if (hash === 'citas') mostrarSeccion('seccion-moraleja', 'citas');
        }});
    </script>
</body>
</html>
"""

with open(output_html, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Successfully generated clean UTF-8 HTML at: {output_html}")
