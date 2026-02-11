#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from lxml import html


INPUT_HTML = Path("guardado.html")  # cambia si tu guardado.html está en otra ruta
OUT_JSON = Path("housing_ads.json")
OUT_CSV = Path("housing_ads.csv")


def decode_js_jsonparse_string(s: str) -> Optional[str]:

    try:
        return json.loads(f'"{s}"')
    except Exception:
        return None


def find_initialsearch_block(doc: html.HtmlElement) -> Optional[Dict[str, Any]]:
    """
    Busca en los <script> un JSON.parse("...") que, una vez decodificado, contenga initialSearch/result/realEstates.
    Devuelve el dict ya parseado.
    """
    scripts_text = doc.xpath("//script/text()")
    for script in scripts_text:
        if "JSON.parse" not in script:
            continue

        # Extrae todos los JSON.parse("...") del script
        for m in re.finditer(r'JSON\.parse\("(.+?)"\)', script, flags=re.S):
            raw_inside_quotes = m.group(1)
            decoded = decode_js_jsonparse_string(raw_inside_quotes)
            if not decoded:
                continue

            # Pequeño filtro rápido antes de json.loads
            if "initialSearch" not in decoded or "realEstates" not in decoded:
                continue

            try:
                data = json.loads(decoded)
            except Exception:
                continue

            # Validación de estructura esperada
            if (
                isinstance(data, dict)
                and isinstance(data.get("initialSearch"), dict)
                and isinstance(data["initialSearch"].get("result"), dict)
                and isinstance(data["initialSearch"]["result"].get("realEstates"), list)
            ):
                return data

    return None


def flatten_for_csv(ad: Dict[str, Any]) -> Dict[str, Any]:
    price = ad.get("price") if isinstance(ad.get("price"), dict) else {}
    features = ad.get("features") if isinstance(ad.get("features"), dict) else {}
    location = ad.get("location") if isinstance(ad.get("location"), dict) else {}
    coords = ad.get("coordinates") if isinstance(ad.get("coordinates"), dict) else {}
    address = ad.get("address") if isinstance(ad.get("address"), dict) else {}

    # URLs suelen venir en "detail" (por idioma) o "detailWithParams"
    detail = ad.get("detail") if isinstance(ad.get("detail"), dict) else {}
    detail_url = (
        ad.get("detailWithParams")
        or detail.get("es-ES")
        or detail.get("es")
        or ad.get("clientUrl")
    )

    return {
        "propertyId": ad.get("propertyId") or ad.get("id"),
        "realEstateAdId": ad.get("realEstateAdId"),
        "detailUrl": detail_url,
        "rawPrice": ad.get("rawPrice"),
        "price_amount": price.get("amount") if isinstance(price, dict) else None,
        "price_drop": price.get("amountDrop") if isinstance(price, dict) else ad.get("reducedPrice"),
        "rooms": features.get("rooms"),
        "bathrooms": features.get("bathrooms"),
        "surface": features.get("surface"),
        "floor": features.get("floor"),
        "antiquity": features.get("antiquity"),
        "transactionTypeId": ad.get("transactionTypeId"),
        "typeId": ad.get("typeId"),
        "subtypeId": ad.get("subtypeId"),
        "buildingType": ad.get("buildingType"),
        "buildingSubtype": ad.get("buildingSubtype"),
        "isNew": ad.get("isNew"),
        "isNewConstruction": ad.get("isNewConstruction"),
        "publisherId": ad.get("publisherId"),
        "clientAlias": ad.get("clientAlias"),
        "clientType": ad.get("clientType"),
        "phone": ad.get("phone"),
        "location_address": location.get("address") or address.get("upperLevel"),
        "location_zone": location.get("zone") or address.get("county"),
        "location_municipality": location.get("municipality") or address.get("district"),
        "location_locality": location.get("locality") or address.get("city"),
        "latitude": coords.get("latitude"),
        "longitude": coords.get("longitude"),
    }


def main() -> None:
    raw = INPUT_HTML.read_text(encoding="utf-8", errors="ignore")
    doc = html.fromstring(raw)

    block = find_initialsearch_block(doc)
    if not block:
        print("No se encontró un bloque initialSearch.result.realEstates dentro de JSON.parse(...)")
        OUT_JSON.write_text("[]", encoding="utf-8")
        OUT_CSV.write_text("", encoding="utf-8")
        return

    real_estates = block["initialSearch"]["result"]["realEstates"]

    # Guarda JSON completo (todos los campos del anuncio)
    OUT_JSON.write_text(json.dumps(real_estates, ensure_ascii=False, indent=2), encoding="utf-8")

    # Guarda CSV “plano” resumen
    rows = [flatten_for_csv(ad) for ad in real_estates]
    fieldnames = sorted({k for r in rows for k in r.keys()})
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Extracted ads: {len(real_estates)}")
    print(f"Wrote: {OUT_JSON.resolve()}")
    print(f"Wrote: {OUT_CSV.resolve()}")


if __name__ == "__main__":
    main()
