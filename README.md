# Utilería de Industria S.A.

Lista compartida de escenografía, props, vestuario, pistas y lo que falta ensayar de la obra de Somos Industria 2026 (libreto v3.3).

- `index.html`: la página que publica GitHub Pages. Cada estado y nota se guarda en Firestore (proyecto `somos-industria-be1c5`, colección `utileria`) y se ve en vivo en todos los teléfonos.
- `firestore.rules`: reglas del proyecto, con el bloque `utileria` agregado.
- `lista-inicial.json` y `cargar_lista.py`: la lista tal como estaba en el artifact de claude.ai el 2026-10-19. Se carga una sola vez con `python cargar_lista.py`; no pisa lo que ya exista.
- `sonido-y-ensayo.json`: pistas de ensayo, sonidos de la obra y la sección «Falta ensayar» (2026-11-11). Se carga con `python cargar_lista.py sonido-y-ensayo.json`, después de publicar las reglas con los tipos `pista` y `ensayo`.
