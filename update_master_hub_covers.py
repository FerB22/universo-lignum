import os

hub_html = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UNIVERSO LIGNUM | Biblioteca de Historias</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: #090B10;
      color: #F8FAFC;
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background: rgba(15, 17, 23, 0.95);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 1rem 2rem;
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 1000;
    }
    .header-container {
      max-width: 1300px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: #FFF;
    }
    .brand-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: radial-gradient(circle, #38BDF8 0%, rgba(0,0,0,0.6) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #38BDF8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }
    .brand-title {
      font-family: 'Cinzel', serif;
      font-weight: 800;
      font-size: 1.2rem;
      letter-spacing: 1.5px;
      background: linear-gradient(135deg, #FFF 0%, #38BDF8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .brand-sub {
      font-size: 0.75rem;
      color: #64748B;
      display: block;
    }

    main {
      flex: 1;
      max-width: 1300px;
      width: 100%;
      margin: 0 auto;
      padding: 3rem 1.5rem;
    }

    .hero {
      text-align: center;
      margin-bottom: 3.5rem;
    }
    .hero-badge {
      display: inline-block;
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38BDF8;
      font-size: 0.82rem;
      margin-bottom: 1rem;
    }
    .hero h1 {
      font-family: 'Cinzel', serif;
      font-size: clamp(2.2rem, 5vw, 3.5rem);
      font-weight: 900;
      letter-spacing: 2px;
      background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 50%, #D4AF37 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
    }
    .hero p {
      max-width: 750px;
      margin: 0 auto;
      color: #94A3B8;
      font-size: 1.05rem;
      line-height: 1.6;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 2.2rem;
      align-items: start;
    }

    .card {
      background: rgba(22, 27, 38, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 22px;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.35s ease;
      position: relative;
      overflow: hidden;
    }
    .card:hover {
      transform: translateY(-8px);
      border-color: var(--card-color);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(255, 255, 255, 0.05);
    }

    .card-cover {
      width: 100%;
      border-radius: 14px;
      overflow: hidden;
      margin-bottom: 1.25rem;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      background: #0B0E17;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .cover-img {
      width: 100%;
      height: auto;
      display: block;
      object-fit: contain;
      transition: transform 0.4s ease;
    }
    .card:hover .cover-img {
      transform: scale(1.03);
    }

    .card-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      color: var(--card-color);
      border: 1px solid var(--card-color);
      margin-bottom: 0.85rem;
    }
    .card-title {
      font-family: 'Cinzel', serif;
      font-size: 1.5rem;
      color: #FFF;
      margin-bottom: 0.65rem;
    }
    .card-desc {
      font-size: 0.92rem;
      color: #94A3B8;
      line-height: 1.6;
      margin-bottom: 1.25rem;
      flex-grow: 1;
    }
    .card-features {
      font-size: 0.8rem;
      color: #64748B;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 1rem;
      margin-bottom: 1.25rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .feat-tag {
      background: rgba(255, 255, 255, 0.05);
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
    }
    .card-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      padding: 0.85rem;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #FFF;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.25s ease;
    }
    .card-btn:hover {
      background: var(--card-color);
      border-color: var(--card-color);
      color: #000;
    }

    footer {
      background: #06080C;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 2rem;
      text-align: center;
      color: #475569;
      font-size: 0.85rem;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <a href="#" class="brand">
        <div class="brand-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <div>
          <span class="brand-title">UNIVERSO LIGNUM</span>
          <span class="brand-sub">Portal de Historias Autónomas</span>
        </div>
      </a>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="hero-badge">✦ Repositorio de Historias Independientes ✦</div>
      <h1>UNIVERSO LIGNUM</h1>
      <p>
        Bienvenido a Universo Lignum, el espacio donde convergen mis sagas y relatos de fantasía e historia. Explora cada mundo a través de su propia experiencia interactiva, acompañando a sus personajes en sus batallas, reflexiones y destinos.
      </p>
    </section>

    <div class="grid">

      <!-- La Piedra sin Pulir -->
      <div class="card" style="--card-color: #FFCC33;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/NdxnWgmS/Portada-de-La-Piedra-sin-Pulir.png" alt="Portada de La Piedra sin Pulir" class="cover-img">
          </div>
          <span class="card-badge">Fábula Mística</span>
          <h2 class="card-title">La Piedra sin Pulir</h2>
          <p class="card-desc">Fábula del Señor de las Siete Esposas. Diseño en Oro Imperial (#FFCC33) con 4 Actos escénicos, copiado de frases interactivas y barra de progreso.</p>
          <div class="card-features">
            <span class="feat-tag">Transición de Vistas</span>
            <span class="feat-tag">Copiador de Frases</span>
            <span class="feat-tag">4 Temas</span>
            <span class="feat-tag">Control A-/A+</span>
          </div>
        </div>
        <a href="./la-piedra-sin-pulir/index.html" class="card-btn">Abrir Sitio Web de la Historia →</a>
      </div>

      <!-- Forgotten Sword -->
      <div class="card" style="--card-color: #FF4444;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/5hfYDKFT/Portada-de-Forgotten-Sword.png" alt="Portada de Forgotten Sword" class="cover-img">
          </div>
          <span class="card-badge">Fantasía Oscura</span>
          <h2 class="card-title">Forgotten Sword</h2>
          <p class="card-desc">Saga de 15 capítulos en estética gótica. Incluye portal con doble botón (Fichas vs Lista de Capítulos), Prólogo y lector con barra lateral derecha.</p>
          <div class="card-features">
            <span class="feat-tag">15 Capítulos HTML</span>
            <span class="feat-tag">Sidebar Lateral</span>
            <span class="feat-tag">Fichas de Personajes</span>
            <span class="feat-tag">Prólogo</span>
          </div>
        </div>
        <a href="./forgotten-sword/index.html" class="card-btn">Abrir Sitio Web de la Historia →</a>
      </div>

      <!-- Ruk el Héroe -->
      <div class="card" style="--card-color: #D4AF37;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/jvP88cKJ/Portada-en-Creaci-n.png" alt="Portada de Ruk el Héroe (En Creación)" class="cover-img">
          </div>
          <span class="card-badge" style="color: #D4AF37; border-color: #D4AF37;">En Creación</span>
          <h2 class="card-title">Ruk el Héroe</h2>
          <p class="card-desc">Saga fantástica imperial en desarrollo. 9 capítulos editados, diseño Blanco & Dorado Imperial con fichas de personajes ilustradas.</p>
          <div class="card-features">
            <span class="feat-tag">9 Capítulos Editados</span>
            <span class="feat-tag">Blanco & Dorado</span>
            <span class="feat-tag">En Creación</span>
          </div>
        </div>
        <a href="./ruk-el-heroe/index.html" class="card-btn">Abrir Sitio Web de la Historia →</a>
      </div>

      <!-- Sangre y Cadáveres -->
      <div class="card" style="--card-color: #CA0B0B;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/MQxMcc6/Portada-de-Sangre-y-Cad-veres.png" alt="Portada de Sangre y Cadáveres" class="cover-img">
          </div>
          <span class="card-badge">Terror Visceral</span>
          <h2 class="card-title">Sangre y Cadáveres</h2>
          <p class="card-desc">Atmósfera escarlata (#CA0B0B) y negro profundo. Lectura fluida y sección de investigación conceptual del universo.</p>
          <div class="card-features">
            <span class="feat-tag">Escarlata #CA0B0B</span>
            <span class="feat-tag">Conceptualización</span>
            <span class="feat-tag">Diseño Terror</span>
          </div>
        </div>
        <a href="./sangre-y-cadaveres/index.html" class="card-btn">Abrir Sitio Web de la Historia →</a>
      </div>

      <!-- The Marriage of the Republic -->
      <div class="card" style="--card-color: #8B5A2B;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/SXNrFc51/Portada-de-The-Marriage-of-the-Republic.png" alt="Portada de The Marriage of the Republic" class="cover-img">
          </div>
          <span class="card-badge">Ficción Histórica</span>
          <h2 class="card-title">The Marriage of the Republic</h2>
          <p class="card-desc">Marrón claro (#8B5A2B) y dorado republicano. Lector de ficción histórica con sistema de scripts e interfaz dedicada.</p>
          <div class="card-features">
            <span class="feat-tag">Marrón #8B5A2B</span>
            <span class="feat-tag">Interfaz Histórica</span>
            <span class="feat-tag">script.js & styles.css</span>
          </div>
        </div>
        <a href="./marriage-of-the-republic/index.html" class="card-btn">Abrir Sitio Web de la Historia →</a>
      </div>

      <!-- Getting to Know -->
      <div class="card" style="--card-color: #00F2FE;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/TM63LgTZ/Portada-de-Getting-to-Know.png" alt="Portada de Getting to Know" class="cover-img">
          </div>
          <span class="card-badge">Fantasía Tribal</span>
          <h2 class="card-title">Getting to Know</h2>
          <p class="card-desc">Turquesa neón (#00F2FE) y púrpura. Fichas de personajes de la Tribu Häscht (Amera, Derk, Hesis, Heya, Lomen) y lector de la novela.</p>
          <div class="card-features">
            <span class="feat-tag">5 Fichas Ilustradas</span>
            <span class="feat-tag">Turquesa #00F2FE</span>
            <span class="feat-tag">Transición de Vistas</span>
          </div>
        </div>
        <a href="./getting-to-know/index.html" class="card-btn">Abrir Sitio Web de la Historia →</a>
      </div>

    </div>
  </main>

  <footer>
    <p>&copy; 2026 UNIVERSO LIGNUM — Creado por Fernando Barra. Todos los sitios web son independientes y autónomos.</p>
  </footer>

</body>
</html>
'''

with open(r'C:\Users\Barra\Documents\UNIVERSO LIGNUM\index.html', 'w', encoding='utf-8') as f:
    f.write(hub_html)

print('Master hub updated with Ruk el Héroe "En Creación" cover!')
