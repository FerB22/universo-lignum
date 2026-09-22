# Compendio de soluciones técnicas — Universo Lignum

Registro histórico de incidencias, errores, fallos técnicos y sus resoluciones aplicadas en el proyecto web del Universo Lignum.

---

### Entrada: 22 de septiembre de 2026 — Corrección de favicon y nombre de sitio en los resultados de búsqueda de Google

1. **Fecha y contexto / entorno:**
   - **Fecha:** 22 de septiembre de 2026.
   - **Entorno:** Sitio web estático alojado en GitHub Pages (`https://ferb22.github.io/universo-lignum/`), indexado en el motor de búsqueda de Google para dispositivos móviles y de escritorio.

2. **Problema detectado:**
   - En los resultados de búsqueda de Google para consultas sobre «universo lignum», el resultado mostraba un icono genérico de globo terráqueo en lugar del isotipo oficial de la obra.
   - Asimismo, el nombre del sitio aparecía rotulado como «GitHub Pages documentation» en vez de «Universo Lignum».

3. **Causa raíz:**
   - **Favicon externo y no normado:** Las etiquetas de cabecera apuntaban a una imagen alojada en un servicio externo de alojamiento de imágenes (`i.ibb.co`), la cual no cumplía con los múltiplos de 48 píxeles exigidos por el rastreador `Google-Favicon`, impidiendo o retrasando la indexación del icono oficial. Además, no existía un archivo `favicon.ico` en el repositorio local.
   - **Falta de metadatos de identidad de sitio:** No existía la etiqueta `og:site_name` ni un bloque de datos estructurados `schema.org/WebSite` (JSON-LD). En consecuencia, el algoritmo de Google recurrió al título por defecto del subdominio base `ferb22.github.io` (página de bienvenida/404 de GitHub Pages, titulada «GitHub Pages documentation»).

4. **Solución aplicada:**
   - Se procesó el archivo maestro del logo (`Favicon.png`, resolución original de 2048×2048 px) mediante la biblioteca Pillow en Python, generándose versiones optimizadas en la raíz y en el directorio `public/`:
     - `favicon-48x48.png` (múltiplo básico para Googlebot).
     - `favicon-96x96.png`.
     - `favicon-192x192.png` (alta resolución para Android y Google).
     - `favicon-512x512.png` (resolución para PWA y metadatos Open Graph).
     - `apple-touch-icon.png` (180×180 px para iOS).
     - `favicon.ico` (archivo multirresolución con capas de 16, 32, 48 y 64 px).
   - Se actualizaron los 48 archivos HTML del sitio sustituyendo los enlaces externos por las referencias locales y canónicas al favicon.
   - Se añadió el atributo `og:site_name` con el valor `Universo Lignum` en las páginas del proyecto.
   - Se incorporó en `index.html` el esquema JSON-LD formal:
     ```html
     <script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "name": "Universo Lignum",
       "alternateName": ["Biblioteca de Historias", "Lignum"],
       "url": "https://ferb22.github.io/universo-lignum/"
     }
     </script>
     ```

---

### Entrada: 22 de septiembre de 2026 — Corrección visual y responsiva del botón «El saber del mundo» en móviles

1. **Fecha y contexto / entorno:**
   - **Fecha:** 22 de septiembre de 2026.
   - **Entorno:** Dispositivos móviles (pantallas estrechas <= 600 px) en la portada principal `index.html`.

2. **Problema detectado:**
   - En celulares, el botón de acceso al compendio «El saber del mundo» se deformaba convirtiéndose en un óvalo vertical gigante, con su texto apilado en cuatro renglones («EL \n SABER \n DEL \n MUNDO») y aplastando visualmente la cabecera.

3. **Causa raíz:**
   - **Ausencia de `white-space: nowrap` y `flex-shrink: 0`:** Al reducirse el ancho de la pantalla, el contenedor flexible comprimía el botón y quebraba cada palabra de la frase por sus espacios.
   - **Carencia de reglas adaptadas en medios móviles:** El encabezado mantenía los rellenos de escritorio (`padding: 1.1rem 2rem;`), restando más de 64 px útiles y saturando el ancho disponible.

4. **Solución aplicada:**
   - Se añadió `white-space: nowrap;`, `flex-shrink: 0;` y un degradado sutil con efecto táctil a `.header-seal-btn`.
   - Se implementaron puntos de quiebre `@media (max-width: 900px)`, `@media (max-width: 600px)` y `@media (max-width: 380px)` ajustando rellenos, tamaño del isotipo y tipografía.
   - Se introdujo una variante de etiqueta adaptativa: en pantallas grandes se visualiza «El saber del mundo» y en pantallas móviles se compacta elegantemente a «El saber», preservando la estética heráldica y de insignia pulida.
