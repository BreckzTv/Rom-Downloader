import json
import os
import myrient_api
import requests
from tqdm import tqdm

session = requests.Session()

def download_file(url: str, out_dir: str):
    """Lädt eine einzelne Datei mit Fortschrittsanzeige herunter"""
    local_filename = os.path.join(out_dir, os.path.basename(url))
    os.makedirs(out_dir, exist_ok=True)

    with session.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        with open(local_filename, "wb") as f, tqdm(
            desc=os.path.basename(url),
            total=total,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    return local_filename


def main():
    print("=== Myrient Konsolen Browser ===\n")

    # Konsolen anzeigen
    consoles = myrient_api.data
    for i, c in enumerate(consoles, 1):
        print(f"{i}: {c['name']}")

    # Konsole wählen
    wahl = int(input("\nWähle eine Konsole (Nummer): ")) - 1
    if not (0 <= wahl < len(consoles)):
        print("Ungültige Auswahl.")
        return

    console = consoles[wahl]
    print(f"\nLade Spieleliste für: {console['name']} ...")

    # Spiele abrufen
    games = myrient_api.fetch_games(console["url"])
    if not games:
        print("Keine Spiele gefunden.")
        return

    for i, g in enumerate(games, 1):
        print(f"{i}: {g['name']}")

    # Spiel auswählen
    choice = input("\nWelche Spiele herunterladen? (Nummer oder mehrere mit Komma, 'all' für alle): ")

    if choice.lower() == "all":
        selected_games = games
    else:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(",")]
            selected_games = [games[i] for i in indices if 0 <= i < len(games)]
        except Exception:
            print("Ungültige Eingabe.")
            return

    if not selected_games:
        print("Keine gültigen Spiele ausgewählt.")
        return

    # Download-Verzeichnis
    out_dir = f"downloads/{console['name']}"
    os.makedirs(out_dir, exist_ok=True)

    # Dateien laden
    for game in selected_games:
        print(f"\nStarte Download: {game['name']}")
        try:
            path = download_file(game["url"], out_dir)
            print(f"✅ Fertig: {path}")
        except Exception as e:
            print(f"❌ Fehler beim Download: {e}")


if __name__ == "__main__":
    main()
