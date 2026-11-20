/**
 * Visor modal compartido para el Mapamundi oficial de Universo Lignum.
 * Sigue el patrón nativo <dialog> con closedby="any", contención de scroll y zoom simple.
 */
(function initWorldMapModal() {
  const triggerBtn = document.getElementById('openMapBtn');
  if (!triggerBtn) return;

  const mapSrc = triggerBtn.dataset.mapSrc || './public/mapa-lignum-oficial.webp';
  const mapFallback = triggerBtn.dataset.mapFallback || './public/mapa-lignum-oficial.jpg';

  const style = document.createElement('style');
  style.textContent = `
    dialog.map-dialog {
      margin: auto;
      width: min(94vw, 1120px);
      max-height: 92vh;
      padding: 0;
      border: 1.5px solid rgba(212, 175, 55, 0.35);
      border-radius: 16px;
      background: rgba(14, 18, 27, 0.96);
      color: #F8F6F0;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.78);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }

    dialog.map-dialog[open] {
      display: flex;
      flex-direction: column;
    }

    dialog.map-dialog:modal {
      overscroll-behavior: contain;
    }

    dialog.map-dialog::backdrop {
      overflow: hidden;
      overscroll-behavior: contain;
      background: rgba(4, 6, 10, 0.84);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }

    .map-dialog-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 14px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      flex-shrink: 0;
      flex-wrap: wrap;
    }

    .map-dialog-titles h2 {
      font-family: var(--fonts-heading, 'Cinzel', Georgia, serif);
      font-size: clamp(1rem, 2.2vw, 1.3rem);
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #F3E5AB;
      margin: 0;
    }

    .map-dialog-sub {
      font-family: var(--fonts-body, 'Lora', Georgia, serif);
      font-style: italic;
      font-size: 0.82rem;
      color: #94A3B8;
      margin-top: 2px;
    }

    .map-dialog-controls {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-left: auto;
    }

    .map-ctrl-btn {
      min-width: 34px;
      height: 34px;
      padding: 0 10px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: rgba(255, 255, 255, 0.05);
      color: #F8F6F0;
      font-family: var(--fonts-ui, 'Plus Jakarta Sans', sans-serif);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .map-ctrl-btn:hover:not(:disabled) {
      background: rgba(212, 175, 55, 0.16);
      border-color: rgba(212, 175, 55, 0.45);
      color: #F3E5AB;
    }

    .map-ctrl-btn:disabled {
      opacity: 0.4;
      cursor: default;
    }

    .map-close-btn {
      width: 34px;
      height: 34px;
      margin-left: 6px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.16);
      background: rgba(255, 255, 255, 0.06);
      color: #F8F6F0;
      font-size: 1rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .map-close-btn:hover {
      background: rgba(239, 68, 68, 0.2);
      border-color: rgba(239, 68, 68, 0.5);
      color: #FCA5A5;
    }

    .map-dialog-viewport {
      display: block;
      flex: 1;
      min-height: 0;
      overflow: auto;
      overscroll-behavior: contain;
      padding: 16px;
      text-align: center;
      background: #07090D;
      border-bottom-left-radius: 16px;
      border-bottom-right-radius: 16px;
    }

    .map-dialog-img {
      display: block;
      width: 100%;
      max-width: 100%;
      height: auto;
      margin: 0 auto;
      border-radius: 10px;
      border: 1px solid rgba(212, 175, 55, 0.25);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.65);
      transition: width 0.2s ease;
    }

    @media (max-width: 600px) {
      dialog.map-dialog {
        width: 96vw;
        max-height: 90vh;
      }
      .map-dialog-header {
        padding: 12px 14px;
      }
      .map-dialog-viewport {
        padding: 10px;
      }
    }
  `;
  document.head.appendChild(style);

  const dialog = document.createElement('dialog');
  dialog.id = 'worldMapDialog';
  dialog.className = 'map-dialog';
  dialog.setAttribute('closedby', 'any');
  dialog.setAttribute('aria-labelledby', 'worldMapTitle');
  dialog.innerHTML = `
    <div class="map-dialog-header">
      <div class="map-dialog-titles">
        <h2 id="worldMapTitle">Mapamundi de Lignum</h2>
        <p class="map-dialog-sub">Los tres continentes, reinos y territorios del mundo</p>
      </div>
      <div class="map-dialog-controls">
        <button type="button" class="map-ctrl-btn" id="mapZoomOutBtn" aria-label="Reducir ampliación del mapa" title="Alejar">−</button>
        <button type="button" class="map-ctrl-btn" id="mapZoomResetBtn" aria-label="Restablecer ampliación al 100 %" title="Tamaño original">100 %</button>
        <button type="button" class="map-ctrl-btn" id="mapZoomInBtn" aria-label="Ampliar mapa" title="Acercar">+</button>
        <button type="button" class="map-close-btn" id="closeMapBtn" aria-label="Cerrar mapamundi" title="Cerrar (Esc)">✕</button>
      </div>
    </div>
    <div class="map-dialog-viewport" id="mapViewport">
      <img src="${mapSrc}" alt="Mapamundi oficial de los tres continentes de Lignum" class="map-dialog-img" id="worldMapImg" width="1024" height="571" loading="lazy">
    </div>
  `;
  document.body.appendChild(dialog);

  const img = document.getElementById('worldMapImg');
  img.addEventListener('error', () => {
    if (!img.dataset.fallbackApplied) {
      img.dataset.fallbackApplied = '1';
      img.src = mapFallback;
    }
  });

  const zoomOutBtn = document.getElementById('mapZoomOutBtn');
  const zoomResetBtn = document.getElementById('mapZoomResetBtn');
  const zoomInBtn = document.getElementById('mapZoomInBtn');
  const closeBtn = document.getElementById('closeMapBtn');
  const viewport = document.getElementById('mapViewport');

  let zoomPct = 100;
  const MIN_ZOOM = 100;
  const MAX_ZOOM = 250;
  const STEP_ZOOM = 25;

  function applyZoom(nextPct) {
    zoomPct = Math.max(MIN_ZOOM, Math.min(MAX_ZOOM, nextPct));
    img.style.width = `${zoomPct}%`;
    img.style.maxWidth = zoomPct === 100 ? '100%' : 'none';
    img.style.margin = zoomPct === 100 ? '0 auto' : '0';
    zoomResetBtn.textContent = `${zoomPct} %`;
    zoomOutBtn.disabled = zoomPct <= MIN_ZOOM;
    zoomInBtn.disabled = zoomPct >= MAX_ZOOM;
  }

  triggerBtn.addEventListener('click', () => {
    applyZoom(100);
    dialog.showModal();
  });

  closeBtn.addEventListener('click', () => dialog.close());
  zoomOutBtn.addEventListener('click', () => applyZoom(zoomPct - STEP_ZOOM));
  zoomResetBtn.addEventListener('click', () => applyZoom(100));
  zoomInBtn.addEventListener('click', () => applyZoom(zoomPct + STEP_ZOOM));

  // Respaldo de light-dismiss para navegadores sin soporte nativo de closedby="any"
  if (!('closedBy' in HTMLDialogElement.prototype)) {
    const isOutside = (e) => {
      const r = dialog.getBoundingClientRect();
      return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
    };
    let pressedOutside = false;
    dialog.addEventListener('pointerdown', (e) => { pressedOutside = isOutside(e); });
    dialog.addEventListener('pointerup', (e) => {
      if (pressedOutside && isOutside(e)) dialog.close();
      pressedOutside = false;
    });
  }
})();
