import os

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Universo Lignum | Monorepositorio Literario</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800;900&family=Lora:ital,wght@0,400;0,600;1,400&family=Orbitron:wght@600;800;900&family=Playfair+Display:wght@600;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">

  <style>
    /* Global Reset & Base */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background-color: #090B10;
      color: #F8FAFC;
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* Universal Floating Navigation */
    .univ-header {
      position: sticky; top: 0; z-index: 1000;
      background: rgba(15, 17, 23, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .univ-header-container {
      max-width: 1300px; margin: 0 auto; padding: 0.75rem 1.5rem;
      display: flex; align-items: center; justify-content: space-between;
    }
    .univ-brand {
      display: flex; align-items: center; gap: 0.85rem; text-decoration: none; color: inherit; cursor: pointer;
    }
    .univ-brand-icon {
      width: 42px; height: 42px; border-radius: 10px;
      background: radial-gradient(circle, #38BDF8 0%, rgba(0,0,0,0.6) 100%);
      display: flex; align-items: center; justify-content: center; color: #fff;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4); border: 1px solid #38BDF8;
    }
    .univ-brand-title {
      font-family: 'Cinzel', serif; font-weight: 700; font-size: 1.15rem; letter-spacing: 1px;
      background: linear-gradient(135deg, #fff 0%, #38BDF8 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .univ-brand-sub { font-size: 0.75rem; color: rgba(255, 255, 255, 0.6); }

    .univ-nav { display: flex; align-items: center; gap: 0.75rem; }
    .univ-btn {
      display: inline-flex; align-items: center; gap: 0.5rem;
      padding: 0.55rem 1.1rem; border-radius: 8px; font-size: 0.88rem; font-weight: 600;
      text-decoration: none; color: #E2E8F0; background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1); cursor: pointer; transition: all 0.25s ease;
    }
    .univ-btn:hover, .univ-btn.active {
      background: rgba(255, 255, 255, 0.15); border-color: #38BDF8; color: #fff; transform: translateY(-2px);
    }

    /* Scoped Layout System Container */
    .story-view { display: none; padding: 2rem 1.5rem; min-height: 80vh; animation: fadeIn 0.4s ease; }
    .story-view.active { display: block; }

    @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

    /* ========================================================= */
    /* PORTAL PRINCIPAL LAYOUT */
    /* ========================================================= */
    .portal-hero {
      text-align: center; padding: 4rem 1rem 3rem;
      background: radial-gradient(circle at top, rgba(56, 189, 248, 0.15) 0%, rgba(9, 11, 16, 1) 75%);
    }
    .portal-hero-badge {
      display: inline-flex; align-items: center; gap: 0.5rem;
      padding: 0.4rem 1.1rem; border-radius: 9999px; background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3); color: #38BDF8; font-size: 0.85rem; margin-bottom: 1.5rem;
    }
    .portal-hero-title {
      font-family: 'Cinzel', serif; font-size: 3.5rem; font-weight: 900; letter-spacing: 2px;
      background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 50%, #D4AF37 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1rem;
    }
    .portal-hero-desc { max-width: 800px; margin: 0 auto 2.5rem; font-size: 1.1rem; color: #94A3B8; line-height: 1.7; }
    .portal-stats { display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 3rem; }
    .portal-stat-card {
      background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 1.25rem 2.25rem; border-radius: 14px; text-align: center;
    }
    .portal-stat-num { font-family: 'Cinzel', serif; font-size: 2.2rem; font-weight: 700; color: #38BDF8; }
    .portal-stat-lbl { font-size: 0.8rem; color: #64748B; }

    .portal-grid { max-width: 1250px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 2rem; }
    .portal-card {
      background: rgba(22, 27, 38, 0.65); border: 1px solid rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(12px); border-radius: 18px; padding: 2rem;
      display: flex; flex-direction: column; justify-content: space-between;
      transition: all 0.35s ease; position: relative; overflow: hidden;
    }
    .portal-card:hover { transform: translateY(-8px); border-color: var(--card-theme); box-shadow: 0 20px 40px rgba(0,0,0,0.6); }
    .portal-card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
    .portal-card-badge {
      font-size: 0.72rem; font-weight: 700; text-transform: uppercase; padding: 0.25rem 0.65rem;
      border-radius: 9999px; color: var(--card-theme); border: 1px solid var(--card-theme);
    }
    .portal-card-layout { font-size: 0.7rem; color: rgba(255, 255, 255, 0.4); font-family: monospace; }
    .portal-card-title { font-family: 'Cinzel', serif; font-size: 1.5rem; color: #FFF; margin-bottom: 0.75rem; }
    .portal-card-desc { font-size: 0.92rem; color: #94A3B8; line-height: 1.6; margin-bottom: 1.5rem; }
    .portal-card-btn {
      display: flex; align-items: center; justify-content: center; gap: 0.6rem;
      padding: 0.8rem; border-radius: 10px; background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15); color: #FFF; font-weight: 600; cursor: pointer; transition: all 0.25s ease;
    }
    .portal-card-btn:hover { background: var(--card-theme); color: #000; border-color: var(--card-theme); }

    /* ========================================================= */
    /* SCOPED LAYOUT 1: Ruk el Héroe (Blanco & Dorado Imperial) */
    /* ========================================================= */
    .layout-ruk { background: #FAF8F5 !important; color: #2C261F !important; }
    .ruk-container {
      max-width: 1100px; margin: 0 auto; background: #FFFFFF; padding: 3rem;
      border-radius: 20px; border: 2px solid #D4AF37; box-shadow: 0 15px 40px rgba(212, 175, 55, 0.18);
      font-family: 'Lora', serif;
    }
    .ruk-container h1, .ruk-container h2, .ruk-container h3 { font-family: 'Cinzel', serif; color: #2C261F; }
    .ruk-container h1 { font-size: 2.5rem; color: #9E8237; text-align: center; border-bottom: 2px solid #FFD700; padding-bottom: 1rem; margin-bottom: 1.5rem; }
    .ruk-container p { font-size: 1.1rem; line-height: 1.9; color: #3A3228; margin-bottom: 1.25rem; }

    /* ========================================================= */
    /* SCOPED LAYOUT 2: Forgotten Sword (Gótico & Plata Oscura) */
    /* ========================================================= */
    .layout-forgotten { background: #0B0B0E !important; color: #E2E8F0 !important; }
    .forgotten-container {
      max-width: 1100px; margin: 0 auto; background: #13131A; padding: 3rem;
      border-radius: 16px; border: 1px solid #8B0000; box-shadow: 0 0 30px rgba(139, 0, 0, 0.3);
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .forgotten-container h1 { font-family: 'Cinzel Decorative', 'Cinzel', serif; color: #E2E8F0; text-align: center; font-size: 2.3rem; border-bottom: 1px solid #8B0000; padding-bottom: 1rem; margin-bottom: 1.5rem; }
    .forgotten-container p { font-size: 1.05rem; line-height: 1.8; color: #CBD5E1; margin-bottom: 1.2rem; }

    /* ========================================================= */
    /* SCOPED LAYOUT 3: Sangre y Cadáveres (Escarlata & Negro) */
    /* ========================================================= */
    .layout-sangre { background: #0D0202 !important; color: #F8FAFC !important; }
    .sangre-container {
      max-width: 1100px; margin: 0 auto; background: #140404; padding: 3rem;
      border-radius: 16px; border: 2px solid #CA0B0B; box-shadow: 0 0 40px rgba(202, 11, 11, 0.4);
    }
    .sangre-container h1 { font-family: 'Cinzel', serif; color: #FF3333; text-align: center; font-size: 2.4rem; border-bottom: 2px solid #CA0B0B; padding-bottom: 1rem; margin-bottom: 1.5rem; text-shadow: 0 0 15px #CA0B0B; }
    .sangre-container p { font-size: 1.08rem; line-height: 1.85; color: #E2E8F0; margin-bottom: 1.25rem; }

    /* ========================================================= */
    /* SCOPED LAYOUT 4: The Marriage of the Republic (Marrón & Dorado) */
    /* ========================================================= */
    .layout-republic { background: #FDFBF7 !important; color: #4A3525 !important; }
    .republic-container {
      max-width: 1100px; margin: 0 auto; background: #FFFDF9; padding: 3rem;
      border-radius: 18px; border: 2px solid #8B5A2B; box-shadow: 0 12px 35px rgba(139, 90, 43, 0.15);
    }
    .republic-container h1 { font-family: 'Playfair Display', serif; color: #8B5A2B; text-align: center; font-size: 2.3rem; border-bottom: 2px solid #D4AF37; padding-bottom: 0.85rem; margin-bottom: 1.5rem; }
    .republic-container p { font-size: 1.08rem; line-height: 1.85; color: #3D2B1F; margin-bottom: 1.2rem; }

    /* ========================================================= */
    /* SCOPED LAYOUT 5: Getting to Know (Cyberpunk Neón) */
    /* ========================================================= */
    .layout-cyberpunk { background: #070913 !important; color: #E0F7FA !important; }
    .cyber-container {
      max-width: 1100px; margin: 0 auto; background: #0B0E1B; padding: 3rem;
      border-radius: 16px; border: 2px solid #00F2FE; box-shadow: 0 0 35px rgba(0, 242, 254, 0.35);
      font-family: 'Rajdhani', sans-serif;
    }
    .cyber-container h1 { font-family: 'Orbitron', sans-serif; color: #00F2FE; text-align: center; font-size: 2.3rem; border-bottom: 2px solid #9B51E0; padding-bottom: 0.85rem; margin-bottom: 1.5rem; text-shadow: 0 0 15px #00F2FE; }
    .cyber-container p { font-size: 1.15rem; line-height: 1.8; color: #C7D2FE; margin-bottom: 1.25rem; }

    /* ========================================================= */
    /* SCOPED LAYOUT 6: La Piedra sin Pulir (Místico Esmeralda) */
    /* ========================================================= */
    .layout-emerald { background: #04120B !important; color: #ECFDF5 !important; }
    .emerald-container {
      max-width: 1100px; margin: 0 auto; background: #081C13; padding: 3rem;
      border-radius: 16px; border: 2px solid #10B981; box-shadow: 0 0 35px rgba(16, 185, 129, 0.35);
    }
    .emerald-container h1 { font-family: 'Cinzel', serif; color: #34D399; text-align: center; font-size: 2.3rem; border-bottom: 2px solid #10B981; padding-bottom: 0.85rem; margin-bottom: 1.5rem; text-shadow: 0 0 12px #10B981; }
    .emerald-container p { font-size: 1.08rem; line-height: 1.85; color: #D1FAE5; margin-bottom: 1.2rem; }

    /* Footer */
    .univ-footer { background: #0B0D14; border-top: 1px solid rgba(255, 255, 255, 0.08); padding: 3rem 1.5rem 2rem; text-align: center; margin-top: 4rem; color: #64748B; }
  </style>
</head>
<body>

  <!-- UNIVERSAL NAVIGATION HEADER -->
  <header class="univ-header">
    <div class="univ-header-container">
      <div class="univ-brand" onclick="switchView('portal')">
        <div class="univ-brand-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
          </svg>
        </div>
        <div>
          <div class="univ-brand-title">UNIVERSO LIGNUM</div>
          <div class="univ-brand-sub" id="active-layout-label">Portal Principal & Scoped Layouts</div>
        </div>
      </div>

      <nav class="univ-nav">
        <button class="univ-btn active" id="btn-portal" onclick="switchView('portal')">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          <span>Menú del Universo</span>
        </button>
      </nav>
    </div>
  </header>

  <!-- VIEW 0: MAIN PORTAL -->
  <main id="view-portal" class="story-view active">
    <section class="portal-hero">
      <div class="portal-hero-badge">
        <span>✦ Monorepositorio Literario & Scoped CSS Layouts ✦</span>
      </div>
      <h1 class="portal-hero-title">UNIVERSO LIGNUM</h1>
      <p class="portal-hero-desc">
        Todas tus historias viven bajo una misma arquitectura unificada. Cada universo posee su propio <strong>Layout Scoped CSS</strong> independiente sin interferencia de estilos.
      </p>

      <div class="portal-stats">
        <div class="portal-stat-card"><div class="portal-stat-num">6</div><div class="portal-stat-lbl">Universos Registrados</div></div>
        <div class="portal-stat-card"><div class="portal-stat-num">6</div><div class="portal-stat-lbl">Scoped CSS Layouts</div></div>
        <div class="portal-stat-card"><div class="portal-stat-num">29+</div><div class="portal-stat-lbl">Capítulos & Fichas</div></div>
      </div>
    </section>

    <div class="portal-grid">
      <!-- Card 1 -->
      <div class="portal-card" style="--card-theme: #D4AF37;">
        <div>
          <div class="portal-card-header">
            <span class="portal-card-badge">Fantasía Épica</span>
            <span class="portal-card-layout">EstiloImperativoRuk.astro</span>
          </div>
          <h3 class="portal-card-title">Ruk el Héroe</h3>
          <p class="portal-card-desc">Saga completa de 9 capítulos. Estética de Blanco & Dorado Imperial (#FAF8F5, #D4AF37) con fichas de personaje y mapa.</p>
        </div>
        <button class="portal-card-btn" onclick="switchView('ruk')">Abrir Universo Ruk →</button>
      </div>

      <!-- Card 2 -->
      <div class="portal-card" style="--card-theme: #8B0000;">
        <div>
          <div class="portal-card-header">
            <span class="portal-card-badge">Fantasía Oscura</span>
            <span class="portal-card-layout">EstiloForgottenSword.astro</span>
          </div>
          <h3 class="portal-card-title">Forgotten Sword</h3>
          <p class="portal-card-desc">Atmósfera gótica de acero oscuro y carmesí profundo (#0F0F12, #8B0000). Reliquias olvidadas y caballeros caídos.</p>
        </div>
        <button class="portal-card-btn" onclick="switchView('forgotten')">Abrir Forgotten Sword →</button>
      </div>

      <!-- Card 3 -->
      <div class="portal-card" style="--card-theme: #CA0B0B;">
        <div>
          <div class="portal-card-header">
            <span class="portal-card-badge">Terror Visceral</span>
            <span class="portal-card-layout">EstiloSangreCadaveres.astro</span>
          </div>
          <h3 class="portal-card-title">Sangre y Cadáveres</h3>
          <p class="portal-card-desc">Diseño inquietante en rojo escarlata (#CA0B0B) y negro absoluto. Resistencia armada ante el colapso humano.</p>
        </div>
        <button class="portal-card-btn" onclick="switchView('sangre')">Abrir Sangre y Cadáveres →</button>
      </div>

      <!-- Card 4 -->
      <div class="portal-card" style="--card-theme: #8B5A2B;">
        <div>
          <div class="portal-card-header">
            <span class="portal-card-badge">Ficción Histórica</span>
            <span class="portal-card-layout">EstiloMarriageRepublic.astro</span>
          </div>
          <h3 class="portal-card-title">The Marriage of the Republic</h3>
          <p class="portal-card-desc">Tonalidades marrón claro (#8B5A2B) y dorado republicano. Intrigas de Estado, capitulaciones y poder.</p>
        </div>
        <button class="portal-card-btn" onclick="switchView('republic')">Abrir Republic →</button>
      </div>

      <!-- Card 5 -->
      <div class="portal-card" style="--card-theme: #00F2FE;">
        <div>
          <div class="portal-card-header">
            <span class="portal-card-badge">Cyberpunk Neón</span>
            <span class="portal-card-layout">EstiloGettingToKnow.astro</span>
          </div>
          <h3 class="portal-card-title">Getting to Know</h3>
          <p class="portal-card-desc">Futuro cibernético en turquesa neón (#00F2FE) y púrpura. Fichas de personajes modificados y hackeo.</p>
        </div>
        <button class="portal-card-btn" onclick="switchView('cyberpunk')">Abrir Cyberpunk →</button>
      </div>

      <!-- Card 6 -->
      <div class="portal-card" style="--card-theme: #10B981;">
        <div>
          <div class="portal-card-header">
            <span class="portal-card-badge">Fábula Mística</span>
            <span class="portal-card-layout">EstiloLaPiedraSinPulir.astro</span>
          </div>
          <h3 class="portal-card-title">La Piedra sin Pulir</h3>
          <p class="portal-card-desc">Espiritualidad esmeralda (#10B981) y alquimia interior. Reflexiones de transformación en la naturaleza.</p>
        </div>
        <button class="portal-card-btn" onclick="switchView('emerald')">Abrir La Piedra sin Pulir →</button>
      </div>
    </div>
  </main>

  <!-- VIEW 1: RUK EL HÉROE (Scoped Layout) -->
  <section id="view-ruk" class="story-view layout-ruk">
    <div class="ruk-container">
      <div style="text-align:center; font-size:0.85rem; color:#D4AF37; font-weight:700; letter-spacing:2px; margin-bottom:0.5rem;">✦ ESTILO IMPERIAL BLANCO & DORADO ✦</div>
      <h1>RUK EL HÉROE — NOVELA COMPLETA</h1>
      <p><em>Saga completa de 9 capítulos editados y compilados en codificación UTF-8 pura sin discordancias.</em></p>
      
      <div style="background:#FAF8F5; border-left:4px solid #D4AF37; padding:1.25rem; margin:1.5rem 0; border-radius:8px;">
        <h3 style="font-family:'Cinzel',serif; color:#9E8237; margin-bottom:0.5rem;">Capítulo 1: El peso de la partida</h3>
        <p>El alba despuntaba en el horizonte cuando los jóvenes se preparaban para marchar a la guerra. En las puertas del pueblo de Davir, la brisa helada arrastraba consigo el eco de las despedidas. Las madres abrazaban a sus hijos con los ojos enrojecidos. Ivia rodeó a Ruk con un abrazo que parecía querer protegerlo del mundo entero...</p>
      </div>

      <div style="background:#FAF8F5; border-left:4px solid #D4AF37; padding:1.25rem; margin:1.5rem 0; border-radius:8px;">
        <h3 style="font-family:'Cinzel',serif; color:#9E8237; margin-bottom:0.5rem;">Capítulo 9: Héroes de Davir</h3>
        <p>Guiado por ese brillo, Ruk dio un último y prodigioso salto y hundió la hoja sagrada hasta la empuñadura en el pecho del gigante. Con un gemido que hizo temblar la tierra, la bestia colapsó sobre sí misma. Ruk se mantuvo en pie sobre el tórax del monstruo caído, bañado por una luz heroica ante miles de ojos...</p>
      </div>

      <div style="text-align:center; margin-top:2rem;">
        <button class="univ-btn" onclick="switchView('portal')" style="background:#D4AF37; color:#000; font-weight:700; border:none; padding:0.8rem 2rem;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- VIEW 2: FORGOTTEN SWORD (Scoped Layout) -->
  <section id="view-forgotten" class="story-view layout-forgotten">
    <div class="forgotten-container">
      <div style="text-align:center; font-size:0.85rem; color:#8B0000; font-weight:700; letter-spacing:2px; margin-bottom:0.5rem;">⚔ ESTILO GÓTICO & PLATA OSCURA ⚔</div>
      <h1>FORGOTTEN SWORD</h1>
      <p>Las sombras envolvían las viejas piedras del bastión mientras los caballeros de la orden de plata desenvainaban sus aceros rúnicos...</p>

      <div style="text-align:center; margin-top:2rem;">
        <button class="univ-btn" onclick="switchView('portal')" style="background:#8B0000; color:#FFF; font-weight:700; border:none; padding:0.8rem 2rem;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- VIEW 3: SANGRE Y CADÁVERES (Scoped Layout) -->
  <section id="view-sangre" class="story-view layout-sangre">
    <div class="sangre-container">
      <div style="text-align:center; font-size:0.85rem; color:#FF3333; font-weight:700; letter-spacing:2px; margin-bottom:0.5rem;">🩸 ESTILO ESCARLATA #CA0B0B & NEGRO 🩸</div>
      <h1>SANGRE Y CADÁVERES</h1>
      <p>El horizonte ardía en tonos rojo escarlata. El acero no daba tregua y cada paso sobre el terreno erosionado recordaba el precio de la guerra...</p>

      <div style="text-align:center; margin-top:2rem;">
        <button class="univ-btn" onclick="switchView('portal')" style="background:#CA0B0B; color:#FFF; font-weight:700; border:none; padding:0.8rem 2rem;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- VIEW 4: THE MARRIAGE OF THE REPUBLIC (Scoped Layout) -->
  <section id="view-republic" class="story-view layout-republic">
    <div class="republic-container">
      <div style="text-align:center; font-size:0.85rem; color:#8B5A2B; font-weight:700; letter-spacing:2px; margin-bottom:0.5rem;">📜 ESTILO MARRÓN CLARO #8B5A2B & DORADO 📜</div>
      <h1>THE MARRIAGE OF THE REPUBLIC</h1>
      <p>Las altas cámaras del Senado resplandecían bajo los faroles de bronce. Los acuerdos diplomáticos sellaron la unión de las provincias...</p>

      <div style="text-align:center; margin-top:2rem;">
        <button class="univ-btn" onclick="switchView('portal')" style="background:#8B5A2B; color:#FFF; font-weight:700; border:none; padding:0.8rem 2rem;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- VIEW 5: GETTING TO KNOW (Scoped Layout) -->
  <section id="view-cyberpunk" class="story-view layout-cyberpunk">
    <div class="cyber-container">
      <div style="text-align:center; font-size:0.85rem; color:#00F2FE; font-weight:700; letter-spacing:2px; margin-bottom:0.5rem;">⚡ ESTILO CYBERPUNK #00F2FE & PÚRPURA ⚡</div>
      <h1>GETTING TO KNOW — CYBERPUNK</h1>
      <p>Las transmisiones de la red de datos parpadeaban en turquesa neón sobre las fachadas de la megalópolis. Los agentes de intrusión preparaban sus terminales...</p>

      <div style="text-align:center; margin-top:2rem;">
        <button class="univ-btn" onclick="switchView('portal')" style="background:#00F2FE; color:#000; font-weight:700; border:none; padding:0.8rem 2rem;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <!-- VIEW 6: LA PIEDRA SIN PULIR (Scoped Layout) -->
  <section id="view-emerald" class="story-view layout-emerald">
    <div class="emerald-container">
      <div style="text-align:center; font-size:0.85rem; color:#34D399; font-weight:700; letter-spacing:2px; margin-bottom:0.5rem;">🌿 ESTILO MÍSTICO ESMERALDA #10B981 🌿</div>
      <h1>LA PIEDRA SIN PULIR</h1>
      <p>En el claro del bosque milenario, la luz filtrada entre las ramas revelaba la piedra tosca. Cada corte de la disciplina interior pulía el carácter...</p>

      <div style="text-align:center; margin-top:2rem;">
        <button class="univ-btn" onclick="switchView('portal')" style="background:#10B981; color:#000; font-weight:700; border:none; padding:0.8rem 2rem;">← Volver al Portal Principal</button>
      </div>
    </div>
  </section>

  <footer class="univ-footer">
    <p>&copy; 2026 Universo Lignum — Monorepositorio Literario Unificado con Scoped CSS Layouts.</p>
  </footer>

  <script>
    function switchView(viewId) {
      document.querySelectorAll('.story-view').forEach(el => el.classList.remove('active'));
      const target = document.getElementById('view-' + viewId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      const label = document.getElementById('active-layout-label');
      if (viewId === 'portal') label.innerText = 'Portal Principal & Scoped Layouts';
      else if (viewId === 'ruk') label.innerText = 'EstiloImperativoRuk.astro (#FAF8F5, #D4AF37)';
      else if (viewId === 'forgotten') label.innerText = 'EstiloForgottenSword.astro (#0F0F12, #8B0000)';
      else if (viewId === 'sangre') label.innerText = 'EstiloSangreCadaveres.astro (#CA0B0B)';
      else if (viewId === 'republic') label.innerText = 'EstiloMarriageRepublic.astro (#8B5A2B)';
      else if (viewId === 'cyberpunk') label.innerText = 'EstiloGettingToKnow.astro (#00F2FE)';
      else if (viewId === 'emerald') label.innerText = 'EstiloLaPiedraSinPulir.astro (#10B981)';
    }
  </script>
</body>
</html>
'''

with open(r'C:\Users\Barra\Documents\mi-universo-literario\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'C:\Users\Barra\Documents\mi-universo-literario\dist\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Monorepo compiled index.html generated in pure UTF-8!')
