import os

personajes_dir = r"c:\Users\Barra\Documents\Ruk - Historia Completa\personajes"
os.makedirs(personajes_dir, exist_ok=True)

def build_sheet_html(name, subtitle, image_src, role, age_start, age_end, affiliation, era, weapons, personality, motivation, conflict, family, allies, origin, arc):
    image_html = f'<img src="{image_src}" alt="{name}" class="char-portrait-img">' if image_src else '<div class="char-portrait-placeholder">🛡️</div>'
    
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ficha de Personaje - {name}</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Lora:ital,wght@0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #FAF8F5;
            --bg-card: #FFFFFF;
            --bg-secondary: #F4EFE6;
            --text-main: #2C261F;
            --text-muted: #665D52;
            --gold-primary: #D4AF37;
            --gold-light: #F8F3E3;
            --gold-dark: #9E8237;
            --gold-border: #E0C775;
            --gold-shadow: rgba(212, 175, 55, 0.2);
            --card-shadow: 0 15px 40px rgba(158, 130, 55, 0.12);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: 'Plus Jakarta Sans', sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px 20px;
        }}

        .sheet-container {{
            width: 100%;
            max-width: 960px;
            background: var(--bg-card);
            border: 2px solid var(--gold-border);
            border-radius: 20px;
            box-shadow: var(--card-shadow);
            padding: 40px;
            position: relative;
            overflow: hidden;
        }}

        .sheet-header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1.5px solid var(--gold-border);
            position: relative;
        }}

        .sheet-badge {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--gold-primary);
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 6px;
            display: inline-block;
        }}

        .sheet-title {{
            font-family: 'Cinzel', serif;
            font-size: 2.5rem;
            font-weight: 900;
            color: var(--text-main);
            margin-bottom: 4px;
        }}

        .sheet-subtitle {{
            font-family: 'Lora', serif;
            font-style: italic;
            font-size: 1.15rem;
            color: var(--gold-dark);
        }}

        /* 2-Column Grid Layout */
        .sheet-body-grid {{
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 35px;
            align-items: start;
        }}

        @media (max-width: 820px) {{
            .sheet-body-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Left Column */
        .left-col {{
            display: flex;
            flex-direction: column;
            gap: 25px;
        }}

        .portrait-frame {{
            background: var(--bg-secondary);
            border: 3px solid var(--gold-primary);
            border-radius: 16px;
            padding: 10px;
            box-shadow: 0 10px 25px var(--gold-shadow);
            position: relative;
            overflow: hidden;
        }}

        .char-portrait-img {{
            width: 100%;
            height: 320px;
            object-fit: cover;
            border-radius: 10px;
            display: block;
        }}

        .char-portrait-placeholder {{
            width: 100%;
            height: 280px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            color: var(--gold-primary);
            background: var(--gold-light);
            border-radius: 10px;
        }}

        .data-card {{
            background: var(--bg-secondary);
            border: 1px solid var(--gold-border);
            border-radius: 14px;
            padding: 20px;
        }}

        .data-row {{
            margin-bottom: 12px;
        }}

        .data-row:last-child {{
            margin-bottom: 0;
        }}

        .data-label {{
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--gold-dark);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 2px;
        }}

        .data-val {{
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-main);
        }}

        /* Right Column */
        .right-col {{
            display: flex;
            flex-direction: column;
            gap: 25px;
        }}

        .info-block {{
            background: var(--bg-card);
            border: 1.5px solid var(--gold-border);
            border-radius: 14px;
            padding: 22px 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        }}

        .block-title {{
            font-family: 'Cinzel', serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 1px solid var(--gold-border);
            padding-bottom: 8px;
        }}

        .block-title span {{
            color: var(--gold-primary);
        }}

        .info-text {{
            font-family: 'Lora', serif;
            font-size: 0.98rem;
            line-height: 1.65;
            color: var(--text-main);
        }}

        .relations-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }}

        @media (max-width: 500px) {{
            .relations-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .relation-item {{
            background: var(--bg-secondary);
            border: 1px solid var(--gold-border);
            border-radius: 10px;
            padding: 12px 15px;
        }}

        .nav-footer {{
            margin-top: 35px;
            padding-top: 20px;
            border-top: 1.5px solid var(--gold-border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }}

        .btn-sheet-nav {{
            padding: 10px 22px;
            background: var(--bg-secondary);
            border: 1.5px solid var(--gold-primary);
            color: var(--gold-dark);
            border-radius: 25px;
            font-weight: 700;
            font-size: 0.9rem;
            text-decoration: none;
            transition: all 0.25s ease;
            cursor: pointer;
        }}

        .btn-sheet-nav:hover {{
            background: var(--gold-primary);
            color: #FFFFFF;
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>

    <div class="sheet-container">
        <!-- Header -->
        <header class="sheet-header">
            <span class="sheet-badge">✦ FICHA DE PERSONAJE · RUK EL HÉROE ✦</span>
            <h1 class="sheet-title">{name}</h1>
            <p class="sheet-subtitle">"{subtitle}"</p>
        </header>

        <!-- Main Body Grid -->
        <div class="sheet-body-grid">
            <!-- Left Column -->
            <div class="left-col">
                <div class="portrait-frame">
                    {image_html}
                </div>

                <div class="data-card">
                    <div class="data-row">
                        <div class="data-label">Rol Principal</div>
                        <div class="data-val">{role}</div>
                    </div>
                    <div class="data-row">
                        <div class="data-label">Edad al Inicio</div>
                        <div class="data-val">{age_start}</div>
                    </div>
                    <div class="data-row">
                        <div class="data-label">Edad al Final de la Saga</div>
                        <div class="data-val">{age_end}</div>
                    </div>
                    <div class="data-row">
                        <div class="data-label">Afiliación</div>
                        <div class="data-val">{affiliation}</div>
                    </div>
                    <div class="data-row">
                        <div class="data-label">Época / Frente</div>
                        <div class="data-val">{era}</div>
                    </div>
                    <div class="data-row">
                        <div class="data-label">Armamento / Destreza</div>
                        <div class="data-val">{weapons}</div>
                    </div>
                </div>
            </div>

            <!-- Right Column -->
            <div class="right-col">
                <!-- Personalidad y Motivación -->
                <div class="info-block">
                    <h3 class="block-title"><span>✦</span> Personalidad y Motivación</h3>
                    <p class="info-text"><strong>Personalidad:</strong> {personality}</p>
                    <p class="info-text" style="margin-top: 8px;"><strong>Motivación:</strong> {motivation}</p>
                    {f'<p class="info-text" style="margin-top: 8px;"><strong>Conflicto Clave:</strong> {conflict}</p>' if conflict else ''}
                </div>

                <!-- Relaciones -->
                <div class="info-block">
                    <h3 class="block-title"><span>✦</span> Relaciones Principales</h3>
                    <div class="relations-grid">
                        <div class="relation-item">
                            <div class="data-label">Familia</div>
                            <div class="data-val">{family}</div>
                        </div>
                        <div class="relation-item">
                            <div class="data-label">Aliados & Amigos</div>
                            <div class="data-val">{allies}</div>
                        </div>
                    </div>
                </div>

                <!-- Trasfondo y Arco -->
                <div class="info-block">
                    <h3 class="block-title"><span>✦</span> Trasfondo y Arco Narrativo</h3>
                    <p class="info-text"><strong>Origen:</strong> {origin}</p>
                    <p class="info-text" style="margin-top: 8px;"><strong>Evolución Narrativa:</strong> {arc}</p>
                </div>
            </div>
        </div>

        <!-- Navigation Footer -->
        <footer class="nav-footer">
            <a href="../index.html#personajes" class="btn-sheet-nav">← Volver al Portal de Ruk</a>
            <a href="../index.html#lectura" class="btn-sheet-nav">📖 Ir a la Lectura</a>
        </footer>
    </div>

</body>
</html>
"""

characters_data = [
    {
        "filename": "ficha_ruk.html",
        "name": "Ruk",
        "subtitle": "El Joven Héroe de Davir",
        "image_src": "../fichas_img/ruk.png",
        "role": "Protagonista / Líder Guerrero",
        "age_start": "12 años (Capítulo 1)",
        "age_end": "18 años (Capítulos 8 y 9)",
        "affiliation": "Tribu de la Aldea / Héroes de Davir",
        "era": "Guerra con Reino Dementi (6 años de conflicto)",
        "weapons": "Espada de entrenamiento / acero y estrategia táctica",
        "personality": "Observador, empático y profundamente leal. Mantiene la calma frente al peligro e inspira valor a sus compañeros.",
        "motivation": "Proteger a su familia y su aldea, unificar a las tribus y detener la devastación de la guerra.",
        "conflict": "Ver partir a los adultos al frente a los 12 años y asumir la responsabilidad del liderazgo al cumplir los 18.",
        "family": "Kairo (padre), Madre",
        "allies": "Riav, Ruval, Muvar, Orwin",
        "origin": "Crecido en una tranquila aldea tribal jugando con espadas de madera y pescando en el río.",
        "arc": "Evoluciona de un niño alegre de 12 años a un consagrado guerrero de 18 años que unifica a los héroes de Davir."
    },
    {
        "filename": "ficha_riav.html",
        "name": "Riav",
        "subtitle": "Compañera Pelirroja y Arquera",
        "image_src": "../fichas_img/riav.png",
        "role": "Compañera / Arquera Tribal",
        "age_start": "13 años (Capítulo 1)",
        "age_end": "19 años (Capítulos 8 y 9)",
        "affiliation": "Tribu de la Aldea",
        "era": "Resistencia de la Aldea",
        "weapons": "Tiro con arco, observación perspicaz y auxilio médico",
        "personality": "Directa, sensible ante la tragedia y fuertemente comprometida con el bienestar de sus seres queridos.",
        "motivation": "Demostrar su potencial y mantener unidos a sus amigos en medio de la tempestad de la guerra.",
        "conflict": "Aceptar la marcha de su padre al frente a los 13 años mientras canaliza su dolor en determinación.",
        "family": "Padre (guerrero del frente)",
        "allies": "Ruk (confidente), Ruval, Muvar",
        "origin": "Criada en la aldea alternando entre labores de tejido y aventuras con Ruk y Ruval.",
        "arc": "Se transforma en la fortaleza emocional del grupo a sus 19 años, demostrando que su potencial trasciende cualquier limitación."
    },
    {
        "filename": "ficha_ruval.html",
        "name": "Ruval",
        "subtitle": "El Combatiente Entusiasta",
        "image_src": "",
        "role": "Amigo Impulsivo / Guerrero",
        "age_start": "13 años (Capítulo 1)",
        "age_end": "19 años (Capítulos 8 y 9)",
        "affiliation": "Tribu de la Aldea",
        "era": "Resistencia de la Aldea",
        "weapons": "Combate cuerpo a cuerpo y cacería de montaña",
        "personality": "Energético, curioso y espontáneo. Aporta aliento positivo al grupo en momentos de tensión.",
        "motivation": "Probar su valentía en combate junto a Ruk y proteger el poblado.",
        "conflict": "Controlar su carácter impulsivo para actuar con estrategia en situaciones de peligro.",
        "family": "Padre (pescador del poblado)",
        "allies": "Ruk, Riav, Muvar",
        "origin": "Joven de la aldea entusiasta de los combates imaginarios con espadas de madera.",
        "arc": "Pasa de ser un joven impulsivo de 13 años a un diestro combatiente de vanguardia de 19 años."
    },
    {
        "filename": "ficha_muvar.html",
        "name": "Muvar",
        "subtitle": "El Compañero Entusiasta",
        "image_src": "",
        "role": "Compañero / Pesca y Logística",
        "age_start": "11 años (Capítulo 1)",
        "age_end": "17 años (Capítulos 8 y 9)",
        "affiliation": "Tribu de la Aldea",
        "era": "Resistencia de la Aldea",
        "weapons": "Cacería, pesca en el río y rastreo",
        "personality": "Amigo leal y contemplativo que aprecia la naturaleza del valle y mantiene unido al grupo.",
        "motivation": "Alegrar a su familia y amigos brindando recursos e iniciativas en tiempos difíciles.",
        "conflict": "Afrontar la desolación de los refugiados y mantenerse firme.",
        "family": "Padre (líder de pesca)",
        "allies": "Ruk, Ruval, Riav",
        "origin": "Pescador y explorador de las orillas del río de la aldea.",
        "arc": "Apoya las rutas de suministros a sus 17 años para sostener a la comunidad y a los guerreros."
    },
    {
        "filename": "ficha_orwin.html",
        "name": "Orwin",
        "subtitle": "Niño Refugiado / Creador de Lanzaditas",
        "image_src": "",
        "role": "Refugiado Superviviente / Aliado",
        "age_start": "9 años (Capítulo 1)",
        "age_end": "15 años (Capítulos 8 y 9)",
        "affiliation": "Supervivientes del Pueblo Cercano",
        "era": "Exilio de los Refugiados",
        "weapons": "Ingenio infantil, piedras pulidas y resiliencia",
        "personality": "Tímido pero cálido y agradecido. Mantiene la esperanza viva enseñando juegos a los demás niños.",
        "motivation": "Encontrar paz y seguridad para su madre y reconstruir su hogar.",
        "conflict": "Superar la pérdida de su pueblo natal tras el ataque invasor.",
        "family": "Madre (superviviente)",
        "allies": "Ruk, Dael, Señor Tehm",
        "origin": "Pueblo cercano destruido por el avance del enemigo Dementi.",
        "arc": "Enseña el juego de las 'Lanzaditas' a Ruk, creciendo como el puente de unión entre refugiados y aldeanos a sus 15 años."
    },
    {
        "filename": "ficha_kairo.html",
        "name": "Kairo",
        "subtitle": "Padre de Ruk y Guardián Tribal",
        "image_src": "../fichas_img/kairo.png",
        "role": "Guerrero Defensor / Veterano",
        "age_start": "38 años (Capítulo 1)",
        "age_end": "44 años (Capítulos 8 y 9)",
        "affiliation": "Consejo Tribal de la Aldea / Frente de Ende",
        "era": "Frente Militar de Ende",
        "weapons": "Espada pesada, escudo de roble y defensa táctica",
        "personality": "Hombre de presencia imponente, sereno y reconfortante. Enseña con el ejemplo de la templanza.",
        "motivation": "Cumplir con el deber sagrado de proteger al reino para que los niños puedan vivir en paz.",
        "conflict": "Marcharse al frente de batalla sabiendo la angustia y tristeza que deja en su hijo Ruk.",
        "family": "Ruk (hijo), Esposa",
        "allies": "Señor Tehm, Ancianos del Consejo",
        "origin": "Veterano de la tribu que ha servido al consejo durante años protegiendo las fronteras.",
        "arc": "Inculca en Ruk el valor de la responsabilidad antes de marchar a las batallas decisivas del frente."
    },
    {
        "filename": "ficha_tehm.html",
        "name": "Señor Tehm",
        "subtitle": "Líder Hospitalario del Pueblo",
        "image_src": "",
        "role": "Líder de la Aldea / Gobernador",
        "age_start": "52 años (Capítulo 1)",
        "age_end": "58 años (Capítulos 8 y 9)",
        "affiliation": "Gobierno de la Aldea",
        "era": "Resistencia de Davir",
        "weapons": "Diplomacia, gobierno y estrategia de protección",
        "personality": "Líder sensato, compasivo y previsor que actúa con prisa ante la necesidad del prójimo.",
        "motivation": "Proteger la paz de su aldea y brindar refugio incondicional a los necesitados.",
        "conflict": "Administrar los escasos recursos del pueblo para sostener a 68 nuevos refugiados.",
        "family": "Comunidad de la Aldea",
        "allies": "Dael, Kairo, Ancianos",
        "origin": "Líder histórico respetado por su generosidad y templanza.",
        "arc": "Abre la gran sede de madera para cobijar a los exiliados, sentando las bases de la unión de las tribus."
    }
]

for char in characters_data:
    file_path = os.path.join(personajes_dir, char["filename"])
    html_code = build_sheet_html(
        char["name"], char["subtitle"], char["image_src"], char["role"],
        char["age_start"], char["age_end"], char["affiliation"], char["era"], char["weapons"],
        char["personality"], char["motivation"], char["conflict"],
        char["family"], char["allies"], char["origin"], char["arc"]
    )
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_code)
    print(f"Updated character sheet with varied ages: {file_path}")

print("Varied character ages successfully written!")
