# Utilería de Industria S.A.

Lista compartida de escenografía, props y vestuario de la obra de Somos Industria 2026 (libreto v3.3).

- `index.html`: la página que publica GitHub Pages. Cada estado y nota se guarda en Firestore (proyecto `somos-industria-be1c5`, colección `utileria`) y se ve en vivo en todos los teléfonos.
- `firestore.rules`: reglas del proyecto, con el bloque `utileria` agregado.
- `lista-inicial.json` y `cargar_lista.py`: la lista tal como estaba en el artifact de claude.ai el 2026-10-19. Se carga una sola vez con `python cargar_lista.py`; no pisa lo que ya exista.
