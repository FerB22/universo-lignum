# Master Hub Generator Script
<!DOCTYPE html>
<html lang="es">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6NPEX2N2DC"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FWTZLRCX09"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-6NPEX2N2DC');
  gtag('config', 'G-FWTZLRCX09');
</script>


<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-6NPEX2N2DC');
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W2VVWR64');</script>
<!-- End Google Tag Manager -->
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
      color: #94A3B8;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 1rem;
      margin-bottom: 1.25rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .feat-tag {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 0.25rem 0.6rem;
      border-radius: 8px;
      color: #CBD5E1;
      font-size: 0.78rem;
      font-weight: 500;
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
  
    /* Social Media Icons Styling */
    .social-links {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin-top: 15px;
    }

    .social-icon-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.25);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
      text-decoration: none;
    }

    .social-icon-btn img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 50%;
      transition: transform 0.3s ease;
    }

    .social-icon-btn:hover {
      transform: translateY(-4px) scale(1.12);
      border-color: #00F2FE;
      box-shadow: 0 6px 20px rgba(0, 242, 254, 0.45);
    }

    .social-floating-bar {
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 999999;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 7px 14px;
      background: rgba(15, 20, 30, 0.90);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      border-radius: 30px;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
    }

    @media (max-width: 600px) {
      .social-floating-bar {
        bottom: 12px;
        right: 12px;
        padding: 5px 10px;
        gap: 8px;
      }
      .social-icon-btn {
        width: 34px;
        height: 34px;
      }
    }

</style>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W2VVWR64"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

  <header>
    <div class="header-container">
      <a href="#" class="brand">
        <img src="https://i.ibb.co/Vc9BJn4r/Logo-Lignum.png" alt="Logo Universo Lignum" class="brand-logo-img">
        <div>
          <span class="brand-title">UNIVERSO LIGNUM</span>
          <span class="brand-sub">Portal Literario Oficial</span>
        </div>
      </a>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="hero-badge">✦ Obras Literarias & Sagas Interactivas ✦</div>
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
          <span class="card-badge">Fábula Moral</span>
          <h2 class="card-title">La Piedra sin Pulir</h2>
          <p class="card-desc">Un poderoso señor engendra más de veinte hijos a los que concede poder sin disciplina. Cuando la soberbia desencadena la tragedia, el padre enfrentará una sentencia implacable para restaurar la justicia.</p>
          <div class="card-features">
            <span class="feat-tag">Señor de las 7 Esposas</span>
            <span class="feat-tag">Justicia & Disciplina</span>
            <span class="feat-tag">Estructura en 4 Actos</span>
            <span class="feat-tag">Fábula de Linaje</span>
          </div>
        </div>
        <a href="./la-piedra-sin-pulir/index.html" class="card-btn">Explorar la Historia →</a>
      </div>

      <!-- Forgotten Sword -->
      <div class="card" style="--card-color: #FF4444;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/5hfYDKFT/Portada-de-Forgotten-Sword.png" alt="Portada de Forgotten Sword" class="cover-img">
          </div>
          <span class="card-badge">Fantasía Oscura Tribal</span>
          <h2 class="card-title">Forgotten Sword</h2>
          <p class="card-desc">Saga épica de 14 capítulos. Entre guerras tribales, pactos diplomáticos y el peso del liderazgo, guerreros y caudillos luchan por proteger a su pueblo y sobrevivir a la marea enemiga de Gricái.</p>
          <div class="card-features">
            <span class="feat-tag">Saga de 14 Capítulos</span>
            <span class="feat-tag">Guerras Tribales</span>
            <span class="feat-tag">Responsabilidad del Mando</span>
            <span class="feat-tag">Prólogo & Fichas</span>
          </div>
        </div>
        <a href="./forgotten-sword/index.html" class="card-btn">Explorar la Historia →</a>
      </div>

      <!-- Ruk el Héroe -->
      <div class="card" style="--card-color: #D4AF37;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/jvP88cKJ/Portada-en-Creaci-n.png" alt="Portada de Ruk el Héroe" class="cover-img">
          </div>
          <span class="card-badge" style="color: #D4AF37; border-color: #D4AF37;">En Creación · Fantasía Épica</span>
          <h2 class="card-title">Ruk el Héroe</h2>
          <p class="card-desc">Novela épica de 9 capítulos editados. Acompaña a Ruk y sus compañeros en la travesía hacia el frente de Ende, forjando guerreros y uniendo tribus para resistir la embestida enemiga.</p>
          <div class="card-features">
            <span class="feat-tag">9 Capítulos Editados</span>
            <span class="feat-tag">Espada del Salvador</span>
            <span class="feat-tag">Unión de Tribus</span>
            <span class="feat-tag">Éter & Sanación</span>
          </div>
        </div>
        <a href="./ruk-el-heroe/index.html" class="card-btn">Explorar la Historia →</a>
      </div>

      <!-- Sangre y Cadáveres -->
      <div class="card" style="--card-color: #CA0B0B;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/MQxMcc6/Portada-de-Sangre-y-Cad-veres.png" alt="Portada de Sangre y Cadáveres" class="cover-img">
          </div>
          <span class="card-badge">Venganza</span>
          <h2 class="card-title">Sangre y Cadáveres</h2>
          <p class="card-desc">Un relato crudo e intenso sobre el renacimiento tras la devastación. Explora la resistencia armada, la venganza implacable y el análisis conceptual del universo escarlata.</p>
          <div class="card-features">
            <span class="feat-tag">Venganza & Renacimiento</span>
            <span class="feat-tag">Resistencia Armada</span>
            <span class="feat-tag">Conflicto Escarlata</span>
            <span class="feat-tag">Conceptualización</span>
          </div>
        </div>
        <a href="./sangre-y-cadaveres/index.html" class="card-btn">Explorar la Historia →</a>
      </div>

      <!-- The Marriage of the Republic -->
      <div class="card" style="--card-color: #8B5A2B;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/SXNrFc51/Portada-de-The-Marriage-of-the-Republic.png" alt="Portada de The Marriage of the Republic" class="cover-img">
          </div>
          <span class="card-badge">Ficción Histórica</span>
          <h2 class="card-title">The Marriage of the Republic</h2>
          <p class="card-desc">Dramas de Estado, alianzas de gobierno y las encrucijadas morales del matrimonio político en una república al borde de la capitulación.</p>
          <div class="card-features">
            <span class="feat-tag">Intrigas de Estado</span>
            <span class="feat-tag">Matrimonio Político</span>
            <span class="feat-tag">Capitulaciones & Honor</span>
            <span class="feat-tag">Dilemas Políticos</span>
          </div>
        </div>
        <a href="./marriage-of-the-republic/index.html" class="card-btn">Explorar la Historia →</a>
      </div>

      <!-- Getting to Know -->
      <div class="card" style="--card-color: #00F2FE;">
        <div>
          <div class="card-cover">
            <img src="https://i.ibb.co/TM63LgTZ/Portada-de-Getting-to-Know.png" alt="Portada de Getting to Know" class="cover-img">
          </div>
          <span class="card-badge">Fantasía Tribal & Supervivencia</span>
          <h2 class="card-title">Getting to Know</h2>
          <p class="card-desc">En el monte del suroeste, un ex-guardia de frontera huye de la desolación y encuentra una nueva razón para vivir al proteger a Ameřa, enfrentando la desconfianza de la tribu Häscht.</p>
          <div class="card-features">
            <span class="feat-tag">Tribu Häscht</span>
            <span class="feat-tag">5 Personajes Principales</span>
            <span class="feat-tag">Cazadores & Guardias</span>
            <span class="feat-tag">Amor & Redención</span>
          </div>
        </div>
        <a href="./getting-to-know/index.html" class="card-btn">Explorar la Historia →</a>
      </div>

    </div>
  </main>

    <footer>
    <p>&copy; 2026 UNIVERSO LIGNUM — Creado por Fernando Barra. Obras literarias e historias independientes.</p>
    <div class="social-links">
      <a href="https://www.instagram.com/herr_ferb?igsh=MTE3ZXV4bmpzODIzNg==" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="Instagram">
        <img src="./public/instagram.jpg" alt="Instagram">
      </a>
      <a href="https://www.facebook.com/fernando.barra.942/" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="Facebook">
        <img src="./public/facebook.jpg" alt="Facebook">
      </a>
      <a href="https://www.linkedin.com/in/fernando-barra-920ab0379/" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="LinkedIn">
        <img src="./public/linkedin.webp" alt="LinkedIn">
      </a>
    </div>
  </footer>


  <!-- Floating Social Media Bar -->
  <div class="social-floating-bar">
    <span style="font-size: 11px; color: #94A3B8; font-weight: 700; font-family: 'Plus Jakarta Sans', sans-serif; letter-spacing: 0.5px;">Redes:</span>
    <a href="https://www.instagram.com/herr_ferb?igsh=MTE3ZXV4bmpzODIzNg==" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="Instagram">
      <img src="./public/instagram.jpg" alt="Instagram">
    </a>
    <a href="https://www.facebook.com/fernando.barra.942/" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="Facebook">
      <img src="./public/facebook.jpg" alt="Facebook">
    </a>
    <a href="https://www.linkedin.com/in/fernando-barra-920ab0379/" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="LinkedIn">
      <img src="./public/linkedin.webp" alt="LinkedIn">
    </a>
  </div>

</body>
</html>
