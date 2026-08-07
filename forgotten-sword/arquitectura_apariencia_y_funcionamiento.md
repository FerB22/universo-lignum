# 🏛️ Arquitectura de Apariencia y Funcionamiento Web - Forgotten Sword

Este documento detalla la **estructura de apariencia visual (maquetación y geometría sin incluir paletas de color)** y el **funcionamiento técnico e interactivo** de todo el portal web del proyecto *Forgotten Sword*.

---

## 1. 📐 Estructura de Apariencia y Maquetación Visual (Layout & Wireframe)
*Nota: Esta sección se enfoca exclusivamente en la disposición espacial, rejillas, proporciones, jerarquía tipográfica y comportamiento responsivo, independientemente de los colores o temas aplicados.*

```
+-----------------------------------------------------------------------+
|                             PÁGINA WEB                                |
|                                                                       |
|  +-----------------------------------------------------------------+  |
|  |             CONTENEDOR PRINCIPAL / MENU DE PORTADA              |  |
|  |                      (max-width: 620px)                         |  |
|  |                                                                 |  |
|  |                      [ Título Saga: h1 ]                        |  |
|  |                    [ Subtítulo / Etiqueta ]                     |  |
|  |                         [ Divisor ❖ ]                           |  |
|  |                                                                 |  |
|  |      +---------------------------------------------------+      |  |
|  |      |   [ Botón 1: Fichas de Personajes (Flex 100%) ]  |      |  |
|  |      +---------------------------------------------------+      |  |
|  |      |   [ Botón 2: Lista de Capítulos (Flex 100%) ]     |      |  |
|  |      +---------------------------------------------------+      |  |
|  +-----------------------------------------------------------------+  |
|                                                                       |
|  +-----------------------------------------------------------------+  |
|  |              SECCIÓN SECUNDARIA (max-width: 1080px)             |  |
|  |               (Oculta por defecto / display: none)              |  |
|  |                                                                 |  |
|  |               [ ← Botón Volver a Menú Principal ]               |  |
|  |               [ Encabezado de Sección: h2 + Intro ]             |  |
|  |                                                                 |  |
|  |   GRIDA DE ELEMENTOS (auto-fit / auto-fill minmax 240-280px):    |  |
|  |   +-----------------+ +-----------------+ +-----------------+   |  |
|  |   | Tarjeta Item 1  | | Tarjeta Item 2  | | Tarjeta Item 3  |   |  |
|  |   +-----------------+ +-----------------+ +-----------------+   |  |
|  +-----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

---

### 1.1 Sistema de Contenedores y Disposición Espacial

1. **Contenedor Principal / Menú de Entrada (`.main-container`)**:
   - **Disposición**: Flexbox vertical (`display: flex; flex-direction: column; align-items: center; justify-content: center`).
   - **Limitación Horizontal**: Ancho máximo restringido a `620px` para mantener un enfoque compacto tipo tarjeta en el centro de la pantalla.
   - **Altura Mínima**: Ocupa el `80vh` del alto de la pantalla, logrando un centrado vertical equilibrado.

2. **Secciones de Contenido Extendido (`.seccion-oculta`)**:
   - **Disposición**: Bloque centrado (`margin: 0 auto`).
   - **Limitación Horizontal**: Ampliada a `1080px` para permitir grillas multicolumna de personajes o capítulos.
   - **Visibilidad**: Ocultas inicialmente (`display: none`). Se activan dinámicamente.

3. **Lector de Capítulos (`.page-layout`)**:
   - **Disposición de Rejilla (`CSS Grid`)**: Estructura de 2 columnas en pantalla grande (`1fr 260px`):
     - **Columna Principal (`.main-col`)**: Ocupa el espacio flexible restante (`1fr`) con el texto del capítulo.
     - **Barra Lateral (`aside.sidebar`)**: Columna fija de `260px` anclada mediante `position: sticky; top: 20px;` para navegación directa entre capítulos.

---

### 1.2 Jerarquía Tipográfica y Geometría de Componentes

1. **Jerarquía Tipográfica**:
   - **Tipografía de Títulos e Interfaz (`Cinzel`)**:
     - Utilizada en encabezados (`h1`, `h2`, `h3`), botones de menú, nombres de personajes y etiquetas de navegación.
     - Variación de pesos: `900` para el título principal, `700` para títulos de capítulos y `600` para elementos secundarios.
   - **Tipografía de Lectura (`Lora`)**:
     - Utilizada en descripciones y en el cuerpo narrativo de los capítulos (`article.prose`).
     - Interlineado holgado (`line-height: 1.85`) y tamaño base configurable por el usuario (`--font-size-base`).
     - Diálogos destacados con sangría e indicador lateral (`border-left: 2px`).

2. **Geometría de Tarjetas y Botones**:
   - **Tarjetas de Personajes (`.tarjeta-item`)**:
     - Grilla responsiva mediante `repeat(auto-fit, minmax(280px, 1fr))`.
     - Esquinas redondeadas (`border-radius: 8px`).
     - Microinteracción de elevación vertical (`transform: translateY(-4px)`) al pasar el cursor.
   - **Tarjetas de Capítulos (`.tarjeta-capitulo`)**:
     - Grilla densa mediante `repeat(auto-fill, minmax(240px, 1fr))`.
     - Formato de enlace de bloque interactivo con esquinas suavemente curvadas.
   - **Marco del Lector (`.reader-container`)**:
     - Contenedor con padding generoso (`44px 50px`).
     - Marco interno simulado mediante un pseudo-elemento `::before` separado 8px de los bordes.

---

### 1.3 Adaptabilidad Responsiva (Breakpoints)

- **Escritorio (> 900px)**:
  - Vista completa del lector con panel lateral de capítulos persistente (`sidebar`).
  - Disposición de grillas en 3 o 4 columnas.
- **Tablets y Pantallas Medianas (600px - 900px)**:
  - El panel lateral del lector se oculta (`display: none`) y se convierte en un panel desplegable (`drawer`) mediante el botón interactivo `☰ Lista`.
- **Móviles (< 600px)**:
  - El título principal reduce su tamaño proporcionalmente (`46px -> 34px`).
  - Los botones de opción ajustan su padding interno (`18px 20px`).
  - Las grillas se ajustan automáticamente a 1 sola columna.
  - El padding del lector de capítulos se reduce (`50px -> 16px`) para optimizar el espacio de lectura.

---

## 2. ⚡ Funcionamiento Técnico e Interacción de la Página Web

```
                        +----------------------------+
                        |  Carga Inicial de Página   |
                        +----------------------------+
                                      |
                                      v
                        +----------------------------+
                        | ¿Existe Hash en la URL?    |
                        +----------------------------+
                         /                          \
             Sí (#fichas / #capitulos)               No
                       /                              \
                      v                                v
       +------------------------------+   +------------------------------+
       | Abrir Sección Directa        |   | Mostrar Menú Principal       |
       | (mostrarSeccion)             |   | (Vista Inicial #menu-principal)|
       +------------------------------+   +------------------------------+
                      \                                /
                       +--------------+---------------+
                                      |
                                      v
                        +----------------------------+
                        |   Interacción del Usuario  |
                        +----------------------------+
                                      |
                +---------------------+---------------------+
                |                                           |
                v                                           v
  [ Clic en Opción del Menú ]               [ Clic en "Volver al Menú" ]
                |                                           |
                v                                           v
  1. Animar menú: .closing (fadeOut 0.3s)   1. Animar sección: .closing (fadeOut 0.3s)
  2. setTimeout(250ms):                     2. setTimeout(250ms):
     - Menú -> display: none                   - Sección -> display: none
     - Target -> display: block                - Menú -> display: flex (+ fadeIn)
     - Hash URL -> #fichas/#capitulos          - Hash URL -> '' (limpiar)
     - Scroll -> top 0 (smooth)                - Scroll -> top 0 (smooth)
```

---

### 2.1 Motor de Transición de Vistas Exclusivas (Single Page Experience)

El sitio utiliza una arquitectura de **Vistas Exclusivas**. Esto significa que solo un contenedor principal está visible a la vez en el viewport, evitando solapamientos o desplazamientos incómodos.

1. **Estado de Transición de Salida (`fadeOut`)**:
   - Al hacer clic en un botón, JavaScript añade la clase `.closing` a la vista activa.
   - La regla CSS `@keyframes fadeOut` desvanece la opacidad (`1 -> 0`) y desplaza ligeramente el elemento hacia abajo (`translateY(20px)`).

2. **Orquestación Temporal con JS (`setTimeout`)**:
   - JavaScript espera exactamente **250ms** para permitir que la animación CSS complete su ciclo visual.
   - Transcurridos los 250ms, la vista saliente recibe `display: none !important`.

3. **Estado de Transición de Entrada (`fadeIn`)**:
   - La nueva vista objetivo se establece en `display: block` y recibe la clase `.active`.
   - La regla CSS `@keyframes fadeIn` eleva suavemente el contenido (`translateY(20px -> 0)`) mientras restablece la opacidad (`0 -> 1`).
   - El navegador ejecuta un desplazamiento automático hacia el origen superior de la página (`window.scrollTo({ top: 0, behavior: 'smooth' })`).

---

### 2.2 Sistema de Enrutamiento Dinámico por Hash de URL

La aplicación incluye un sistema de navegación por Hash (`#fichas`, `#capitulos`) que permite compartir enlaces directos o recargar la página manteniendo la ubicación actual:

- **Listener de Carga (`DOMContentLoaded`)**:
  ```javascript
  window.addEventListener('DOMContentLoaded', () => {
      if (window.location.hash === '#fichas') {
          mostrarSeccion('seccion-fichas', 'fichas');
      } else if (window.location.hash === '#capitulos') {
          mostrarSeccion('seccion-capitulos', 'capitulos');
      }
  });
  ```
- **Sincronización en Tiempo Real**: Al navegar, el script actualiza la propiedad `window.location.hash`, permitiendo el uso nativo del historial del navegador.

---

### 2.3 Modulo de Controles Interactivos de Lectura (`chapter_template.html`)

En las páginas individuales de lectura de capítulos, el usuario dispone de controles dinámicos de interfaz:

1. **Ajuste Progresivo de Tamaño de Fuente (`changeFontSize(delta)`)**:
   - Modifica la variable CSS `:root { --font-size-base }` entre un rango seguro de `14px` a `26px`.
   - Reajusta todo el texto de la lectura sin alterar la maquetación.

2. **Cambiador de Temas de Lectura (`toggleTheme()`)**:
   - Alterna iterativamente entre el tema por defecto, `theme-sepia` y `theme-dark` aplicando clases al contenedor `body`.
   - Modifica de forma centralizada todas las variables de contraste.

3. **Barra Lateral Conmutable para Dispositivos Móviles (`toggleSidebar()`)**:
   - En pantallas móviles, conmuta la clase `.open` del contenedor `aside.sidebar` para desplegar la lista completa de capítulos sobre el contenido.

---

### 2.4 Automatización de Generación de Capítulos (`generate_chapters.ps1`)

El portal cuenta con un pipeline automatizado para la publicación de nuevos capítulos:

1. **Archivos Fuente**: Los capítulos se redactan en archivos Markdown `.md`.
2. **Plantilla Maestra (`chapter_template.html`)**: Define la estructura geométrica, botones de navegación y scripts de lectura.
3. **Compilación en PowerShell**: El script `generate_chapters.ps1` lee los Markdown, convierte la sintaxis a HTML semántico y reemplaza las etiquetas de la plantilla (`{{TITLE}}`, `{{PROSE}}`, `{{SIDEBAR}}`, `{{PREV_LINK}}`, `{{NEXT_LINK}}`), generando archivos `.html` estáticos e independientes en la carpeta `capitulos/`.

---

## 3. 📋 Resumen Sintético de Clases y Selectores Clave

| Clase / Elemento | Función Visual (Apariencia) | Función Técnica (Funcionamiento) |
| :--- | :--- | :--- |
| `.main-container` | Contenedor centrado max `620px` | Vista del menú principal de la web. |
| `.seccion-oculta` | Bloque extendido max `1080px` | Vista secundaria (Fichas o Capítulos). |
| `.seccion-oculta.active` | Visibilidad activa con `fadeIn` | Estado abierto de la vista objetivo. |
| `.closing` | Desvanecimiento de salida (`fadeOut`) | Estado transitorio durante `setTimeout(250ms)`. |
| `.page-layout` | Rejilla CSS Grid 2 columnas (`1fr 260px`) | Maquetación del lector de capítulos. |
| `.sidebar` | Panel lateral sticky de `260px` | Índice interactivo con enlaces a capítulos. |
| `.btn-ctrl` | Botones compactos de interfaz | Disparadores JS de zoom, tema y barra lateral. |

---
*Forgotten Sword © 2026 · Documentación técnica de apariencia y funcionamiento del portal web.*
