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

---

### Entrada: 22 de septiembre de 2026 — Visibilidad y fijación del botón «Abrir archivo completo» en el menú lateral móvil

1. **Fecha y contexto / entorno:**
   - **Fecha:** 22 de septiembre de 2026.
   - **Entorno:** Menú lateral desplegable (*drawer*) de la enciclopedia «El saber del mundo» en navegadores móviles (Chrome, Brave, Safari en Android e iOS).

2. **Problema detectado:**
   - Al abrir el panel lateral en celulares, el botón inferior «Abrir archivo completo» quedaba oculto o cortado debajo de la barra de navegación del navegador móvil, impidiendo al usuario pulsar el botón para acceder al compendio completo.

3. **Causa raíz:**
   - **Uso estricto de `100vh`:** En navegadores móviles, `100vh` calcula la altura ignorando la barra dinámica de navegación y herramientas inferior del navegador, empujando los últimos 60 a 80 px de contenido fuera del área visible de la pantalla.
   - **Falta de contención flexible (`min-height: 0` y `flex-shrink: 0`):** El cuerpo con la lista de entradas (`.drawer-body`) expandía la altura del panel flexible, mientras que el pie (`.drawer-footer`) carecía de anclaje estático (`margin-top: auto; flex-shrink: 0`).

4. **Solución aplicada:**
   - Se actualizó `.drawer-panel` empleando unidades de visualización dinámica moderna (`height: 100dvh; max-height: 100dvh; bottom: 0;`).
   - Se configuró `.drawer-body` con `flex: 1 1 0%; min-height: 0; overflow-y: auto;`, garantizando que únicamente la lista intermedia se desplace con *scroll*.
   - Se fijó `.drawer-footer` con `flex-shrink: 0; margin-top: auto;` y relleno compensatorio para áreas seguras (`env(safe-area-inset-bottom)`), asegurando que el botón permanezca visible y anclado al pie del panel en todo momento.

---

### Entrada: 22 de septiembre de 2026 — Supresión integral de emojis y migración a iconos vectoriales SVG

1. **Fecha y contexto / entorno:**
   - **Fecha:** 22 de septiembre de 2026.
   - **Entorno:** Sitio web completo del Universo Lignum (portada `index.html`, compendio `saber-del-mundo/index.html`, base de datos JSON `public/compendio-canonico.json` y utilidades interactivas `marriage-of-the-republic/script.js`).

2. **Problema detectado:**
   - Presencia de emojis gráficos policromáticos del sistema operativo en botones de pestañas, barras de búsqueda, botones de llamada a la acción y datos de texto canónico. Dichos emojis provocaban inconsistencias visuales según el dispositivo (Android, iOS, Windows, macOS) y rompían la atmósfera medieval sobria y elegante de la obra literaria.

3. **Causa raíz:**
   - Uso histórico de glifos emoji como solución rápida para representar conceptos iconográficos (lupa, libro, mapa, escudo, espadas, pergamino) en lugar de gráficos vectoriales integrados al sistema de diseño.

4. **Solución aplicada:**
   - **Sustitución en interfaz:** Se reemplazaron todos los emojis de navegación, búsqueda y botones por iconos vectoriales SVG limpios (`stroke: currentColor`, `width: 16-18 px`), dotados de coherencia estilística.
   - **Modernización de la base canónica:** En `public/compendio-canonico.json`, los iconos de categoría se migraron a identificadores semánticos (`cosmologia`, `geografia`, `facciones`, `saber`, `cronologia`, `lengua`), mapeados en JavaScript hacia sus respectivos SVG.
   - **Estructuración del texto narrativo:** En las fichas con emojis como divisores (`tribu-koralenn` y `tribu-zomina`), se sustituyeron los glifos por marcadores de encabezado textuales (`[NOMBRE]:`, `[UBICACIÓN Y TERRITORIO]:`, `[CULTURA]:`), actualizando el analizador sintáctico `formatContent()` para estructurarlas en cajas visuales sin depender de expresiones regulares sobre rangos Unicode de emojis.
   - **Símbolos tipográficos:** Se conservaron únicamente los caracteres tipográficos clásicos (`✦`, `✤`, `✕`), cuyo renderizado es estrictamente monocromático y heráldico.

---

### Entrada: 23 de septiembre de 2026 — Desincronización de portada en el carrusel de historias y migración a almacenamiento local canónico

1. **Fecha y contexto / entorno:**
   - **Fecha:** 23 de septiembre de 2026.
   - **Entorno:** Carrusel principal de crónicas en la portada (`index.html`) y páginas de inicio de cada historia. Navegadores modernos (Chromium, Brave, Safari, Firefox).

2. **Problema detectado:**
   - Al navegar entre historias en el escaparate del carrusel (por ejemplo, al cambiar de *Getting to Know* a *The Marriage of the Republic*), el título, género, sinopsis y botón de lectura se actualizaban de forma correcta, pero la imagen de la portada a la izquierda permanecía congelada mostrando la portada anterior (*Getting to Know*).

3. **Causa raíz:**
   - **Dependencia de proveedor externo no canónico (`i.ibb.co`):** Las portadas se solicitaban dinámicamente desde un servicio gratuito de alojamiento externo (`i.ibb.co`), cuyos enlaces presentaban latencias severas (más de 60 segundos por petición), límites de tasa (*rate limiting*) o bloqueos directos por parte de protectores de privacidad y bloqueadores de publicidad (como Brave Shields o listas de filtros de seguimiento).
   - **Comportamiento del motor de renderizado del navegador ante fallas de red:** Cuando a un elemento `<img>` con una imagen previamente decodificada en memoria se le asigna un nuevo valor en su atributo `src` y dicha petición externa queda demorada o es bloqueada, el navegador retiene y continúa dibujando el mapa de bits anterior sin limpiarlo.
   - **Ausencia de precarga y manejo de contingencia (*fallback*):** No existía precarga anticipada de las imágenes en memoria caché ni captura del evento `onerror` para conmutar a un estado visual seguro en caso de falla de descarga.

4. **Solución aplicada:**
   - **Alojamiento local optimizado:** Se descargaron y optimizaron todas las portadas en formato WebP de alto rendimiento (reduciendo el peso total en un 97 %, de ~7 MB a ~365 KB para el conjunto total) y se alojaron en el directorio canónico `public/portadas/` del propio repositorio de GitHub Pages, garantizando disponibilidad inmediata y sin bloqueos de terceros.
   - **Precarga en memoria (`preloadCovers`):** Se introdujo una rutina en `initCarousel()` que instancia objetos `Image` para precargar todas las portadas en la memoria caché del navegador tras la carga inicial del DOM.
   - **Transición visual y manejo resiliente de errores:** En la función `updateCarousel()`, se añadió una transición sutil de opacidad al cambiar de obra y se implementó un controlador `onerror` que, ante cualquier fallo de red, conmuta a la versión PNG local o despliega el panel decorativo con el título correspondiente, impidiendo que vuelva a mostrarse la portada de otra historia.
   - **Actualización en páginas secundarias:** Se actualizaron las referencias de portada e imágenes de metadatos `og:image` y `twitter:image` en las páginas de las 6 historias del universo.
