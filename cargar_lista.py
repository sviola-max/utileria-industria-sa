"""Carga lista-inicial.json en la colección `utileria` de Firestore.

Se corre una sola vez, después de publicar firestore.rules en la consola.
No pisa nada: si un elemento ya existe en Firestore, lo saltea.
"""
import json, sys, urllib.request, urllib.error
from pathlib import Path

PROYECTO = "somos-industria-be1c5"
API_KEY = "AIzaSyC5DrFCMBC8qb6HlKLVJw9iDdyRBXTLC68"  # identificador público de la web, no es un secreto
BASE = f"https://firestore.googleapis.com/v1/projects/{PROYECTO}/databases/(default)/documents"


def valor(v):
    if isinstance(v, bool): return {"booleanValue": v}
    if isinstance(v, int): return {"integerValue": str(v)}
    if isinstance(v, float): return {"doubleValue": v}
    if isinstance(v, list): return {"arrayValue": {"values": [valor(x) for x in v]}}
    if v is None: return {"nullValue": None}
    return {"stringValue": str(v)}


def main():
    lista = json.loads((Path(__file__).parent / "lista-inicial.json").read_text(encoding="utf-8"))
    nuevos = saltados = 0
    for doc_id, d in lista.items():
        url = f"{BASE}/utileria?documentId={doc_id}&key={API_KEY}"
        body = json.dumps({"fields": {k: valor(v) for k, v in d.items()}}).encode()
        req = urllib.request.Request(url, body, {"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req).read(); nuevos += 1
        except urllib.error.HTTPError as e:
            if e.code == 409: saltados += 1; continue
            sys.exit(f"Error {e.code} en {doc_id}: {e.read().decode()[:300]}")
    print(f"Cargados {nuevos}, ya estaban {saltados}, total {len(lista)}.")


if __name__ == "__main__":
    main()
