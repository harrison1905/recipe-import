# recipe-import
# LLM Cookidoo Recipe Import

Dies ist eine einfache Flask-App, die mit OpenAI GPT-4 Rezepte generiert und als HTML ausgibt.

## Features

- Rezeptname als Parameter
- Ausgabe als HTML, geeignet für Cookidoo-URL-Import
- Einfache Weboberfläche zur Rezeptgenerierung

## Setup

1. Python 3.8+ installieren
2. Abhängigkeiten installieren:

3. OpenAI API Key als Umgebungsvariable setzen:
export OPENAI_API_KEY='DEIN_API_KEY'

4. App starten:
python app.py

5. Im Browser `http://localhost:5000` öffnen und Rezept generieren.

## Nutzung mit Cookidoo

- Die URL eines generierten Rezepts (z.B. `http://localhost:5000/generate_recipe?name=Ezme Dip`) in Cookidoo importieren:
- Cookidoo -> Meine Kreationen -> Bestehendes Rezept importieren -> URL einfügen
