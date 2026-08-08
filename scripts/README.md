# 🛠️ Scripts Útiles de Mantenimiento — Universo Lignum

Esta carpeta contiene los scripts en Python reutilizables para el mantenimiento y actualización del portal:

### 1. `generar_portal_hub.py`
 Reconstruye y actualiza la página principal `index.html` con todas las tarjetas de las historias, portadas oficiales, insignias y enlaces independientes.
- **Uso**: `python scripts/generar_portal_hub.py`

### 2. `inyectar_boton_volver.py`
 Inyecta o verifica el botón flotante `Volver a Historias` en todas las páginas HTML de cada historia.
- **Uso**: `python scripts/inyectar_boton_volver.py`

### 3. `limpiar_emojis.py`
 Escanea todos los archivos HTML y elimina emojis o símbolos decorativos para mantener una estética sobria y limpia.
- **Uso**: `python scripts/limpiar_emojis.py`

### 4. `auditar_portal.py`
 Revisa títulos de pestaña, metadatos y enlaces de todas las historias buscando inconsistencias.
- **Uso**: `python scripts/auditar_portal.py`
