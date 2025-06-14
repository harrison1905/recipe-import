from flask import Flask, request, render_template_string
import openai
import os

# Try to import RateLimitError, fallback falls nicht vorhanden
try:
    from openai.error import RateLimitError
except ImportError:
    # Fallback: definiere RateLimitError als allgemeine Exception
    class RateLimitError(Exception):
        pass

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

REZEPT_TEMPLATE = """
Erstelle ein Rezept mit diesen Feldern:

Titel: {name}
Zutaten: 
- Zutat 1
- Zutat 2

Zubereitung:
1. Schritt 1
2. Schritt 2

Portionen: 4
Zubereitungszeit: 30 Minuten
Schwierigkeitsgrad: Einfach

Gib das Rezept zuerst als JSON aus, danach als HTML zum Anzeigen.
"""

@app.route("/generate_recipe")
def generate_recipe():
    name = request.args.get("name", "Ezme Dip")
    prompt = REZEPT_TEMPLATE.format(name=name)

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        text = response.choices[0].message.content
    except RateLimitError:
        return "API-Rate Limit überschritten. Bitte später erneut versuchen.", 429
    except Exception as e:
        return f"Ein Fehler ist aufgetreten: {e}", 500

    try:
        json_part, html_part = text.split("\n\n", 1)
    except ValueError:
        html_part = text

    return render_template_string(html_part)

@app.route("/")
def home():
    return """
    <h1>LLM Cookidoo Recipe Import</h1>
    <form action="/generate_recipe" method="get">
      <input type="text" name="name" placeholder="Rezeptname" required>
      <button type="submit">Rezept generieren</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  