# -*- coding: utf-8 -*-
"""
Generador de compendio canónico estructurado para 'El saber del mundo'.
Extrae cosmología, geografía, facciones, saberes ancestrales, cronología,
glosario y personajes canónicos, omitiendo elementos contemporáneos como Lone Mercenary.
"""

import re
import json
import os

SOURCE_PATH = r"C:\Users\Barra\Documents\03_Escritura_y_Worldbuilding\HISTORIAS Lignum - Escritos\Compendio_actualizado_Universo_Lignum.md"
DEST_PATH = r"c:\Users\Barra\Documents\02_Proyectos_Dev\Página Web - Universo Lignum\public\compendio-canonico.json"

def clean_text(text):
    if not text:
        return ""
    text = text.replace('\r\n', '\n').strip()
    return text

def parse_metadata_fields(block):
    meta = {}
    lines = block.split('\n')
    desc_lines = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('- **') and '**:' in line:
            parts = line[4:].split('**:', 1)
            k = parts[0].strip()
            v = parts[1].strip() if len(parts) > 1 else ""
            meta[k] = v
        elif line.startswith('**') and '**:' in line:
            parts = line[2:].split('**:', 1)
            k = parts[0].strip()
            v = parts[1].strip() if len(parts) > 1 else ""
            meta[k] = v
        else:
            if line:
                desc_lines.append(line)
                
    content = "\n\n".join(desc_lines)
    return meta, content

def build_data():
    with open(SOURCE_PATH, 'r', encoding='utf-8') as f:
        full_text = f.read()

    data = {
        "title": "El saber del mundo — Compendio canónico",
        "description": "Base de conocimiento enciclopédica del Universo Lignum: cosmología, geografía, facciones, cronología, saber arcano y personajes.",
        "categories": {
            "cosmologia": {
                "name": "Cosmología y visión general",
                "icon": "🌌",
                "items": []
            },
            "geografia": {
                "name": "Geografía y enclaves",
                "icon": "🗺️",
                "items": []
            },
            "facciones": {
                "name": "Facciones, órdenes y tribus",
                "icon": "🛡️",
                "items": []
            },
            "saber": {
                "name": "Saber tradicional y disciplinas",
                "icon": "⚔️",
                "items": []
            },
            "cronologia": {
                "name": "Cronología continental",
                "icon": "📜",
                "items": []
            },
            "lengua": {
                "name": "Lengua Märik y calendario",
                "icon": "📖",
                "items": []
            }
        }
    }

    # 1. Cosmología
    data["categories"]["cosmologia"]["items"].append({
        "id": "vision-general",
        "title": "Cosmología del Universo Lignum",
        "summary": "Mundo de fantasía medieval y tensión geopolítica intercontinental.",
        "content": (
            "El Universo Lignum es un vasto tapiz narrativo de fantasía medieval y política donde convergen "
            "reinos centralizados, dinastías forestales, tribus autónomas y los vestigios de una magia antigua "
            "casi extinguida tras el Cataclismo del Año 0 (Calendario Vödhar).\n\n"
            "El bosque colosal Vertaik domina el centro-norte del continente, mientras que al sur se extiende "
            "el desierto de Maumak'lim y la desolación eléctrica de Zorkai Kal. La lengua culta del continente "
            "es el Märik, un idioma estructurado y aglutinante dotado de calendario propio y sistema de doce meses."
        ),
        "tags": ["Cosmología", "Calendario Vödhar", "Vertaik"]
    })

    # 2. Geografía (Sección 5)
    geo_sec = full_text[full_text.find('## 5. Geografía'):full_text.find('## 6. Saber')]
    places_raw = re.findall(r'### 5\.\d+\. [^\n]*?([A-Za-zÁÉÍÓÚáéíóúñÑüÜöÖäÄ\'\s\/\-]+)\n(.*?)(?=\n### 5|\n---|\Z)', geo_sec, re.DOTALL)
    for name, body in places_raw:
        clean_name = name.strip()
        if "asentamiento del sr lorim" in clean_name.lower():
            continue
        meta, text_content = parse_metadata_fields(body)
        data["categories"]["geografia"]["items"].append({
            "id": re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-'),
            "title": clean_name,
            "saga": meta.get("Saga", "Desarrollo Continental"),
            "type": meta.get("Tipo geográfico / Político", "Enclave"),
            "government": meta.get("Soberanía / Gobierno", ""),
            "content": text_content,
            "tags": [clean_name, meta.get("Tipo geográfico / Político", "Lugar")]
        })

    # 3. Facciones (Sección 4)
    factions_sec = full_text[full_text.find('## 4. Facciones'):full_text.find('## 5. Geografía')]
    factions_raw = re.findall(r'### 4\.\d+\. [^\n]*?([A-Za-zÁÉÍÓÚáéíóúñÑüÜöÖäÄ\(\)\s\/\-]+)\n(.*?)(?=\n### 4|\n---|\Z)', factions_sec, re.DOTALL)
    for name, body in factions_raw:
        clean_name = name.strip()
        meta, text_content = parse_metadata_fields(body)
        data["categories"]["facciones"]["items"].append({
            "id": re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-'),
            "title": clean_name,
            "saga": meta.get("Saga", "Lignum World"),
            "type": meta.get("Tipo de organización", "Orden / Facción"),
            "seat": meta.get("Sede / Fortaleza principal", ""),
            "content": text_content,
            "tags": [clean_name, meta.get("Tipo de organización", "Facción")]
        })

    # 4. Saber tradicional (Sección 6)
    lore_sec = full_text[full_text.find('## 6. Saber'):full_text.find('## 7. Cronología')]
    lore_raw = re.findall(r'#### ✨ ([^\n]+)\n(.*?)(?=\n#### ✨|\n### |\n---|\Z)', lore_sec, re.DOTALL)
    for name, body in lore_raw:
        clean_name = name.strip()
        if any(v.lower() in clean_name.lower() for v in ["arkia", "disciplina", "savlik", "thakusk"]):
            meta, text_content = parse_metadata_fields(body)
            data["categories"]["saber"]["items"].append({
                "id": re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-'),
                "title": clean_name,
                "category": meta.get("Campo temático", "Artes y Tradición"),
                "saga": meta.get("Saga vinculada", "Tribu Altari"),
                "content": text_content,
                "tags": [clean_name, meta.get("Campo temático", "Saber")]
            })

    # 5. Cronología (Sección 7)
    chrono_sec = full_text[full_text.find('## 7. Cronología'):full_text.find('## 8. Glosario')]
    events_raw = re.findall(r'### 7\.\d+\. [^\n]*?([A-Za-zÁÉÍÓÚáéíóúñÑüÜöÖäÄ\'\s\/\-\(\)0-9]+)\n(.*?)(?=\n### 7|\n---|\Z)', chrono_sec, re.DOTALL)
    for name, body in events_raw:
        clean_name = name.strip()
        # Omitir notas de tramas o borradores específicos
        if any(w in clean_name.lower() for w in [
            "disputa", 
            "trama en años", 
            "batalla hermanos valle", 
            "cómo waldain obtuvo la espada rota",
            "venganza de dalmerk"
        ]):
            continue
        meta, text_content = parse_metadata_fields(body)
        data["categories"]["cronologia"]["items"].append({
            "id": re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-'),
            "title": clean_name,
            "period": meta.get("Marco temporal / Fecha", "Histórico"),
            "location": meta.get("Escenario / Localización", "Continental"),
            "content": text_content,
            "tags": [clean_name, meta.get("Tipo de acontecimiento", "Hito")]
        })

    # 6. Lengua Märik y Calendario (Sección 8 sin notas sueltas como 'Diccionario' ni 'Diccionario Kavk')
    lang_sec = full_text[full_text.find('## 8. Glosario'):]
    terms_raw = re.findall(r'#### 8\.1\.\d+\.\s+[^\n]*?([^\n]+)\n(.*?)(?=\n#### 8\.|\n### |\n---|\Z)', lang_sec, re.DOTALL)
    for raw_name, body in terms_raw:
        clean_name = re.sub(r'^[^\w\s]+', '', raw_name).strip()
        # Omitir entradas fragmentarias o borradores de diccionario
        if any(w in clean_name.lower() for w in ["diccionario", "adjetivos posesivos"]):
            continue
        meta, text_content = parse_metadata_fields(body)
        data["categories"]["lengua"]["items"].append({
            "id": re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-'),
            "title": clean_name,
            "category": meta.get("Categoría gramatical / Conceptual", "Lengua Märik"),
            "content": text_content,
            "tags": [clean_name, "Lengua Märik"]
        })


    os.makedirs(os.path.dirname(DEST_PATH), exist_ok=True)
    with open(DEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Compendio canónico estructurado generado con éxito en:", DEST_PATH)
    print("Métricas del compendio:")
    for cat_key, cat_val in data["categories"].items():
        print(f" - {cat_val['name']}: {len(cat_val['items'])} elementos")

if __name__ == "__main__":
    build_data()
