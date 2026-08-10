/**
 * Configuración de Tokens de Diseño para Universo Lignum (Stitches)
 * Define la paleta de colores, tipografías, radios de borde y sombras del universo.
 */

export const theme = {
  colors: {
    bgDark: '#0F172A',
    surface: '#1E293B',
    surfaceSecondary: '#140D07',
    emerald: '#52B788',
    gold: '#D4AF37',
    goldLight: '#F8F3E3',
    goldDark: '#9E8237',
    crimson: '#FF4444',
    cyan: '#00F2FE',
    textPrimary: '#F8FAFC',
    textMuted: '#94A3B8',
    borderGold: '#E0C775',
  },
  fonts: {
    heading: "'Cinzel', serif",
    body: "'Lora', Georgia, serif",
    ui: "'Plus Jakarta Sans', sans-serif",
  },
  radii: {
    card: '16px',
    badge: '9999px',
    button: '25px',
  },
  shadows: {
    card: '0 15px 40px rgba(0, 0, 0, 0.3)',
    goldGlow: '0 6px 20px rgba(212, 175, 55, 0.25)',
  },
};

export const config = {
  theme,
};
