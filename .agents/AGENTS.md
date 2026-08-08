# Reglas de Diseño y Clasificación Literaria (UNIVERSO LIGNUM)

## 1. Clasificación Literaria de las Obras
- **Getting to Know**: Es un **CUENTO**, NO una novela. Toda etiqueta, subtítulo, tarjeta o referencia pública debe clasificarlo explícitamente como cuento o relato breve.

## 2. Guía de Diseño Inspirada en «Getting to Know»
Todas las páginas web y componentes visuales del proyecto deben basarse en el patrón estético y funcional de la web de *Getting to Know*:

### 🎨 Paleta de Colores y Fondos
- **Gradientes Radiales Atmosféricos**: Fondos oscuros con resplandores orgánicos en gradiente radial (ej. `radial-gradient(circle at 50% 30%, rgba(82, 183, 136, 0.14) 0%, transparent 65%)`).
- **Paletas Curadas**: Tonos tailoreados (turquesa neón, esmeralda, oro imperial, marrón republicano, carmesí). Evitar colores planos sin matices.

### 🖋️ Tipografía y Estructura
- **Títulos**: Fuentes Serif elegantes como `'Cinzel', serif` con buen espaciado de letras (`letter-spacing: 1.5px a 3px`).
- **Cuerpo del Texto / Narrativa**: Fuentes serif de lectura inmersiva como `'Lora', Georgia, serif` con tamaño cómodo (~18-19px) e interlineado amplio (`line-height: 1.85`).
- **Controles de Interfaz**: Fuentes sans-serif modernas como `'Plus Jakarta Sans'` o `'Outfit'`.

### 🃏 Tarjetas y Componentes (Cards)
- **Esquinas Redondeadas**: Usar bordes curvos (`border-radius: 16px` a `20px`).
- **Glassmorphism y Bordes**: Transparencias con desenfoque de fondo (`backdrop-filter: blur(12px)`) y bordes limpios de 1.5px/2px.
- **Insignias / Badges Superiores**: Badges curvos (`border-radius: 9999px`) en la parte superior de las tarjetas para mantener simetría visual y clasificar el tipo de contenido o estado (ej. *Cuento Completo*, *En proceso de creación*).
- **Micro-interacciones**: Elevaciones suaves al pasar el cursor (`transform: translateY(-4px)`), sombras resplandecientes y transiciones coordinadas (`fadeIn`/`fadeOut`).

### 🧭 Navegación y Responsividad
- **Botón Flotante Navegable**: Botón `Volver a Historias` estilizado con desenfoque glassmorphic y margen suficiente en el encabezado para evitar superposiciones con los títulos.
- **Experiencia de Lectura Despejada**: Transiciones single-page limpias, lectores con control de tamaño de fuente y alternador de temas.
