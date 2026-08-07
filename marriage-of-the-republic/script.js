/**
 * THE MARRIAGE OF THE REPUBLIC - INTERACTIVE SCRIPT
 * Handles exclusive view transitions, theme switcher, font size adjustments, and clipboard utilities.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const hubMenuSection = document.getElementById('hub-menu-section');
  const viewSections = document.querySelectorAll('.view-section');
  const btnBackList = document.querySelectorAll('.btn-back');
  const hubCards = document.querySelectorAll('.hub-card');
  const themeSelect = document.getElementById('themeSelect');
  const btnFontIncrease = document.getElementById('fontIncrease');
  const btnFontDecrease = document.getElementById('fontDecrease');
  const quoteCards = document.querySelectorAll('.quote-card');
  const toast = document.getElementById('toast');

  let currentFontSize = 1.0; // rem

  // --------------------------------------------------------------------------
  // EXCLUSIVE VIEW TRANSITION SYSTEM (guia_transicion_vistas logic)
  // --------------------------------------------------------------------------
  function hideAllViews(callback) {
    let activeFound = false;

    // Check if Hub is active
    if (hubMenuSection && hubMenuSection.style.display !== 'none' && !hubMenuSection.classList.contains('hidden')) {
      activeFound = true;
      hubMenuSection.style.animation = 'fadeOut 0.25s ease forwards';
      setTimeout(() => {
        hubMenuSection.style.display = 'none';
        hubMenuSection.classList.add('hidden');
        if (callback) callback();
      }, 240);
      return;
    }

    // Check view sections
    viewSections.forEach(sec => {
      if (sec.classList.contains('active')) {
        activeFound = true;
        sec.style.animation = 'fadeOut 0.25s ease forwards';
        setTimeout(() => {
          sec.classList.remove('active');
          sec.style.display = 'none';
          if (callback) callback();
        }, 240);
      }
    });

    if (!activeFound && callback) {
      callback();
    }
  }

  function showView(targetId) {
    if (!targetId || targetId === 'hub' || targetId === '#hub') {
      showHubMenu();
      return;
    }

    const cleanId = targetId.replace('#', '');
    const targetSection = document.getElementById(cleanId);

    if (!targetSection) {
      showHubMenu();
      return;
    }

    hideAllViews(() => {
      targetSection.style.display = 'block';
      targetSection.style.animation = 'fadeIn 0.35s ease forwards';
      targetSection.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  function showHubMenu() {
    hideAllViews(() => {
      if (hubMenuSection) {
        hubMenuSection.style.display = 'block';
        hubMenuSection.classList.remove('hidden');
        hubMenuSection.style.animation = 'fadeIn 0.35s ease forwards';
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  }

  // Event Listeners for Hub Cards
  hubCards.forEach(card => {
    card.addEventListener('click', (e) => {
      e.preventDefault();
      const targetView = card.getAttribute('data-target');
      if (targetView) {
        window.location.hash = targetView;
        showView(targetView);
      }
    });
  });

  // Event Listeners for Back Buttons
  btnBackList.forEach(btn => {
    btn.addEventListener('click', () => {
      window.location.hash = '';
      showHubMenu();
    });
  });

  // Hash Navigation Handler
  function handleHashChange() {
    const hash = window.location.hash;
    if (hash) {
      showView(hash);
    } else {
      showHubMenu();
    }
  }

  window.addEventListener('hashchange', handleHashChange);
  
  // Initial Load Check
  if (window.location.hash) {
    handleHashChange();
  }

  // --------------------------------------------------------------------------
  // THEME SWITCHER
  // --------------------------------------------------------------------------
  if (themeSelect) {
    themeSelect.addEventListener('change', (e) => {
      const theme = e.target.value;
      if (theme === 'default') {
        document.body.removeAttribute('data-theme');
      } else {
        document.body.setAttribute('data-theme', theme);
      }
      showToast(`Tema cambiado: ${e.target.options[e.target.selectedIndex].text}`);
    });
  }

  // --------------------------------------------------------------------------
  // FONT SIZE CONTROLS
  // --------------------------------------------------------------------------
  if (btnFontIncrease) {
    btnFontIncrease.addEventListener('click', () => {
      if (currentFontSize < 1.35) {
        currentFontSize += 0.05;
        document.documentElement.style.setProperty('--font-scale', `${currentFontSize}rem`);
        showToast(`Tamaño de letra: ${Math.round(currentFontSize * 100)}%`);
      }
    });
  }

  if (btnFontDecrease) {
    btnFontDecrease.addEventListener('click', () => {
      if (currentFontSize > 0.85) {
        currentFontSize -= 0.05;
        document.documentElement.style.setProperty('--font-scale', `${currentFontSize}rem`);
        showToast(`Tamaño de letra: ${Math.round(currentFontSize * 100)}%`);
      }
    });
  }

  // --------------------------------------------------------------------------
  // CLICK-TO-COPY QUOTES & TOAST UTILITY
  // --------------------------------------------------------------------------
  quoteCards.forEach(card => {
    card.addEventListener('click', () => {
      const textToCopy = card.querySelector('p') ? card.querySelector('p').innerText : card.innerText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('📋 Frase copiada al portapapeles');
      }).catch(err => {
        console.error('Error al copiar:', err);
      });
    });
  });

  function showToast(message) {
    if (!toast) return;
    toast.innerText = message;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  }
});
