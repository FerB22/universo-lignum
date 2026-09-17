/**
 * Configuración de Tokens de Diseño para Universo Lignum (Stitches)
 * Define la paleta de colores, tipografías, radios de borde y sombras del universo.
 */

export const theme = {
  colors: {
    bgDark: '#0A0C10',
    bgBase: '#07090D',
    surface: '#11151F',
    surfaceCard: 'rgba(16, 20, 30, 0.88)',
    surfaceSecondary: '#15100B',
    emerald: '#2D6A4F',
    emeraldLight: '#52B788',
    gold: '#D4AF37',
    goldLight: '#F5EBE0',
    goldDark: '#8C6D3B',
    crimson: '#9E2A2B',
    crimsonLight: '#C1121F',
    sapphire: '#1D3557',
    textPrimary: '#F8F6F0',
    textMuted: '#9B9FA9',
    borderGold: 'rgba(212, 175, 55, 0.35)',
    borderSubtle: 'rgba(255, 255, 255, 0.08)',
  },
  fonts: {
    heading: "'Cinzel', Georgia, serif",
    body: "'Lora', Georgia, serif",
    ui: "'Plus Jakarta Sans', sans-serif",
  },
  radii: {
    card: '18px',
    badge: '9999px',
    button: '12px',
  },
  shadows: {
    card: '0 16px 36px rgba(0, 0, 0, 0.55)',
    goldGlow: '0 4px 25px rgba(212, 175, 55, 0.22)',
    tomeHover: '0 20px 40px rgba(0, 0, 0, 0.7), 0 0 20px rgba(212, 175, 55, 0.15)',
  },
};

export const config = {
  theme,
};
