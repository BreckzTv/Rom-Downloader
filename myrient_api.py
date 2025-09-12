import requests
from bs4 import BeautifulSoup
import urllib.parse

BASE_URL = "https://myrient.erista.me/files/Redump/"

session = requests.Session()

def fetch_data():
    """Holt nur Konsolen-Ordner von Myrient (keine Menülinks)"""
    resp = session.get(BASE_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    consoles = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if not href:
            continue
        # Nur Ordner (endend auf /), aber keine internen Menüpunkte oder externen Links
        if href.endswith("/") and not href.startswith("http") and not href.startswith("?") and ".." not in href:
            console_name = urllib.parse.unquote(href.strip("/"))
            consoles.append({
                "name": console_name,
                "url": BASE_URL + href
            })
    return consoles


def fetch_games(console_url: str):
    """Holt alle Spiele-Dateien (.zip) für eine bestimmte Konsole"""
    resp = session.get(console_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    games = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if not href:
            continue
        if href.endswith(".zip"):
            game_name = urllib.parse.unquote(href)
            games.append({
                "name": game_name,
                "url": console_url + href
            })
    return games


# Globale Liste aller Konsolen
data = [
  {
    "name": "Home",
    "url": "https://myrient.erista.me/files/Redump//"
  },
  {
    "name": "Files",
    "url": "https://myrient.erista.me/files/Redump//files/"
  },
  {
    "name": "Donate",
    "url": "https://myrient.erista.me/files/Redump//donate/"
  },
  {
    "name": "Upload",
    "url": "https://myrient.erista.me/files/Redump//upload/"
  },
  {
    "name": "FAQ",
    "url": "https://myrient.erista.me/files/Redump//faq/"
  },
  {
    "name": "Discord",
    "url": "https://myrient.erista.me/files/Redump/https://discord.gg/4kVP9AuQ24"
  },
  {
    "name": "Telegram",
    "url": "https://myrient.erista.me/files/Redump/https://t.me/s/myrient"
  },
  {
    "name": "Contact Us",
    "url": "https://myrient.erista.me/files/Redump//contact/"
  },
  {
    "name": "hShop",
    "url": "https://myrient.erista.me/files/Redump/https://hshop.erista.me"
  },
  {
    "name": "donate today!",
    "url": "https://myrient.erista.me/files/Redump//donate/"
  },
  {
    "name": "File Name",
    "url": "https://myrient.erista.me/files/Redump/?C=N&O=A"
  },
  {
    "name": "\u00a0\u2193\u00a0",
    "url": "https://myrient.erista.me/files/Redump/?C=N&O=D"
  },
  {
    "name": "File Size",
    "url": "https://myrient.erista.me/files/Redump/?C=S&O=A"
  },
  {
    "name": "\u00a0\u2193\u00a0",
    "url": "https://myrient.erista.me/files/Redump/?C=S&O=D"
  },
  {
    "name": "Date",
    "url": "https://myrient.erista.me/files/Redump/?C=M&O=A"
  },
  {
    "name": "\u00a0\u2193\u00a0",
    "url": "https://myrient.erista.me/files/Redump/?C=M&O=D"
  },
  {
    "name": "Parent directory/",
    "url": "https://myrient.erista.me/files/Redump/../"
  },
  {
    "name": "Acorn - Archimedes/",
    "url": "https://myrient.erista.me/files/Redump/Acorn%20-%20Archimedes/"
  },
  {
    "name": "Apple - Macintosh/",
    "url": "https://myrient.erista.me/files/Redump/Apple%20-%20Macintosh/"
  },
  {
    "name": "Apple - Macintosh - SBI Subchannels/",
    "url": "https://myrient.erista.me/files/Redump/Apple%20-%20Macintosh%20-%20SBI%20Subchannels/"
  },
  {
    "name": "Arcade - Hasbro - VideoNow/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Hasbro%20-%20VideoNow/"
  },
  {
    "name": "Arcade - Hasbro - VideoNow Color/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Hasbro%20-%20VideoNow%20Color/"
  },
  {
    "name": "Arcade - Hasbro - VideoNow Jr/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Hasbro%20-%20VideoNow%20Jr/"
  },
  {
    "name": "Arcade - Hasbro - VideoNow XP/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Hasbro%20-%20VideoNow%20XP/"
  },
  {
    "name": "Arcade - Konami - FireBeat/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Konami%20-%20FireBeat/"
  },
  {
    "name": "Arcade - Konami - M2/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Konami%20-%20M2/"
  },
  {
    "name": "Arcade - Konami - System 573/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Konami%20-%20System%20573/"
  },
  {
    "name": "Arcade - Konami - System GV/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Konami%20-%20System%20GV/"
  },
  {
    "name": "Arcade - Konami - e-Amusement/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Konami%20-%20e-Amusement/"
  },
  {
    "name": "Arcade - Namco - Sega - Nintendo - Triforce/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Namco%20-%20Sega%20-%20Nintendo%20-%20Triforce/"
  },
  {
    "name": "Arcade - Namco - Sega - Nintendo - Triforce - GDI Files/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Namco%20-%20Sega%20-%20Nintendo%20-%20Triforce%20-%20GDI%20Files/"
  },
  {
    "name": "Arcade - Namco - System 246/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Namco%20-%20System%20246/"
  },
  {
    "name": "Arcade - Sega - Chihiro/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Chihiro/"
  },
  {
    "name": "Arcade - Sega - Chihiro - GDI Files/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Chihiro%20-%20GDI%20Files/"
  },
  {
    "name": "Arcade - Sega - Lindbergh/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Lindbergh/"
  },
  {
    "name": "Arcade - Sega - Naomi/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Naomi/"
  },
  {
    "name": "Arcade - Sega - Naomi - GDI Files/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Naomi%20-%20GDI%20Files/"
  },
  {
    "name": "Arcade - Sega - Naomi 2/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Naomi%202/"
  },
  {
    "name": "Arcade - Sega - Naomi 2 - GDI Files/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Naomi%202%20-%20GDI%20Files/"
  },
  {
    "name": "Arcade - Sega - RingEdge/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20RingEdge/"
  },
  {
    "name": "Arcade - Sega - RingEdge 2/",
    "url": "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20RingEdge%202/"
  },
  {
    "name": "Atari - Jaguar CD Interactive Multimedia System/",
    "url": "https://myrient.erista.me/files/Redump/Atari%20-%20Jaguar%20CD%20Interactive%20Multimedia%20System/"
  },
  {
    "name": "Audio CD/",
    "url": "https://myrient.erista.me/files/Redump/Audio%20CD/"
  },
  {
    "name": "Audio CD - Spillover Tracks/",
    "url": "https://myrient.erista.me/files/Redump/Audio%20CD%20-%20Spillover%20Tracks/"
  },
  {
    "name": "BD-Video/",
    "url": "https://myrient.erista.me/files/Redump/BD-Video/"
  },
  {
    "name": "Bandai - Pippin/",
    "url": "https://myrient.erista.me/files/Redump/Bandai%20-%20Pippin/"
  },
  {
    "name": "Bandai - Playdia Quick Interactive System/",
    "url": "https://myrient.erista.me/files/Redump/Bandai%20-%20Playdia%20Quick%20Interactive%20System/"
  },
  {
    "name": "Commodore - Amiga CD/",
    "url": "https://myrient.erista.me/files/Redump/Commodore%20-%20Amiga%20CD/"
  },
  {
    "name": "Commodore - Amiga CD32/",
    "url": "https://myrient.erista.me/files/Redump/Commodore%20-%20Amiga%20CD32/"
  },
  {
    "name": "Commodore - Amiga CDTV/",
    "url": "https://myrient.erista.me/files/Redump/Commodore%20-%20Amiga%20CDTV/"
  },
  {
    "name": "DVD-Video/",
    "url": "https://myrient.erista.me/files/Redump/DVD-Video/"
  },
  {
    "name": "Fujitsu - FM-Towns/",
    "url": "https://myrient.erista.me/files/Redump/Fujitsu%20-%20FM-Towns/"
  },
  {
    "name": "HD DVD-Video/",
    "url": "https://myrient.erista.me/files/Redump/HD%20DVD-Video/"
  },
  {
    "name": "IBM - PC compatible/",
    "url": "https://myrient.erista.me/files/Redump/IBM%20-%20PC%20compatible/"
  },
  {
    "name": "IBM - PC compatible - SBI Subchannels/",
    "url": "https://myrient.erista.me/files/Redump/IBM%20-%20PC%20compatible%20-%20SBI%20Subchannels/"
  },
  {
    "name": "Incredible Technologies - Eagle/",
    "url": "https://myrient.erista.me/files/Redump/Incredible%20Technologies%20-%20Eagle/"
  },
  {
    "name": "Mattel - Fisher-Price iXL/",
    "url": "https://myrient.erista.me/files/Redump/Mattel%20-%20Fisher-Price%20iXL/"
  },
  {
    "name": "Mattel - HyperScan/",
    "url": "https://myrient.erista.me/files/Redump/Mattel%20-%20HyperScan/"
  },
  {
    "name": "Memorex - Visual Information System/",
    "url": "https://myrient.erista.me/files/Redump/Memorex%20-%20Visual%20Information%20System/"
  },
  {
    "name": "Microsoft - Xbox/",
    "url": "https://myrient.erista.me/files/Redump/Microsoft%20-%20Xbox/"
  },
  {
    "name": "Microsoft - Xbox - BIOS Images (DoM Version)/",
    "url": "https://myrient.erista.me/files/Redump/Microsoft%20-%20Xbox%20-%20BIOS%20Images%20%28DoM%20Version%29/"
  },
  {
    "name": "Microsoft - Xbox 360/",
    "url": "https://myrient.erista.me/files/Redump/Microsoft%20-%20Xbox%20360/"
  },
  {
    "name": "NEC - PC Engine CD & TurboGrafx CD/",
    "url": "https://myrient.erista.me/files/Redump/NEC%20-%20PC%20Engine%20CD%20%26%20TurboGrafx%20CD/"
  },
  {
    "name": "NEC - PC-88 series/",
    "url": "https://myrient.erista.me/files/Redump/NEC%20-%20PC-88%20series/"
  },
  {
    "name": "NEC - PC-98 series/",
    "url": "https://myrient.erista.me/files/Redump/NEC%20-%20PC-98%20series/"
  },
  {
    "name": "NEC - PC-FX & PC-FXGA/",
    "url": "https://myrient.erista.me/files/Redump/NEC%20-%20PC-FX%20%26%20PC-FXGA/"
  },
  {
    "name": "Navisoft - Naviken 2.1/",
    "url": "https://myrient.erista.me/files/Redump/Navisoft%20-%20Naviken%202.1/"
  },
  {
    "name": "Nintendo - GameCube - BIOS Images (DoM Version)/",
    "url": "https://myrient.erista.me/files/Redump/Nintendo%20-%20GameCube%20-%20BIOS%20Images%20%28DoM%20Version%29/"
  },
  {
    "name": "Nintendo - GameCube - NKit RVZ [zstd-19-128k]/",
    "url": "https://myrient.erista.me/files/Redump/Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/"
  },
  {
    "name": "Nintendo - Wii - NKit RVZ [zstd-19-128k]/",
    "url": "https://myrient.erista.me/files/Redump/Nintendo%20-%20Wii%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/"
  },
  {
    "name": "Nintendo - Wii U - Disc Keys/",
    "url": "https://myrient.erista.me/files/Redump/Nintendo%20-%20Wii%20U%20-%20Disc%20Keys/"
  },
  {
    "name": "Nintendo - Wii U - WUX/",
    "url": "https://myrient.erista.me/files/Redump/Nintendo%20-%20Wii%20U%20-%20WUX/"
  },
  {
    "name": "Palm/",
    "url": "https://myrient.erista.me/files/Redump/Palm/"
  },
  {
    "name": "Panasonic - 3DO Interactive Multiplayer/",
    "url": "https://myrient.erista.me/files/Redump/Panasonic%20-%203DO%20Interactive%20Multiplayer/"
  },
  {
    "name": "Panasonic - M2/",
    "url": "https://myrient.erista.me/files/Redump/Panasonic%20-%20M2/"
  },
  {
    "name": "Philips - CD-i/",
    "url": "https://myrient.erista.me/files/Redump/Philips%20-%20CD-i/"
  },
  {
    "name": "Photo CD/",
    "url": "https://myrient.erista.me/files/Redump/Photo%20CD/"
  },
  {
    "name": "PlayStation GameShark Updates/",
    "url": "https://myrient.erista.me/files/Redump/PlayStation%20GameShark%20Updates/"
  },
  {
    "name": "Pocket PC/",
    "url": "https://myrient.erista.me/files/Redump/Pocket%20PC/"
  },
  {
    "name": "SNK - Neo Geo CD/",
    "url": "https://myrient.erista.me/files/Redump/SNK%20-%20Neo%20Geo%20CD/"
  },
  {
    "name": "Sega - Dreamcast/",
    "url": "https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast/"
  },
  {
    "name": "Sega - Dreamcast - GDI Files/",
    "url": "https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast%20-%20GDI%20Files/"
  },
  {
    "name": "Sega - Mega CD & Sega CD/",
    "url": "https://myrient.erista.me/files/Redump/Sega%20-%20Mega%20CD%20%26%20Sega%20CD/"
  },
  {
    "name": "Sega - Prologue 21/",
    "url": "https://myrient.erista.me/files/Redump/Sega%20-%20Prologue%2021/"
  },
  {
    "name": "Sega - Saturn/",
    "url": "https://myrient.erista.me/files/Redump/Sega%20-%20Saturn/"
  },
  {
    "name": "Sharp - X68000/",
    "url": "https://myrient.erista.me/files/Redump/Sharp%20-%20X68000/"
  },
  {
    "name": "Sony - PlayStation/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/"
  },
  {
    "name": "Sony - PlayStation - BIOS Images (DoM Version)/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20-%20BIOS%20Images%20%28DoM%20Version%29/"
  },
  {
    "name": "Sony - PlayStation - SBI Subchannels/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20-%20SBI%20Subchannels/"
  },
  {
    "name": "Sony - PlayStation 2/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%202/"
  },
  {
    "name": "Sony - PlayStation 2 - BIOS Images (DoM Version)/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%202%20-%20BIOS%20Images%20%28DoM%20Version%29/"
  },
  {
    "name": "Sony - PlayStation 3/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%203/"
  },
  {
    "name": "Sony - PlayStation 3 - Disc Keys/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%203%20-%20Disc%20Keys/"
  },
  {
    "name": "Sony - PlayStation 3 - Disc Keys TXT/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%203%20-%20Disc%20Keys%20TXT/"
  },
  {
    "name": "Sony - PlayStation Portable/",
    "url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20Portable/"
  },
  {
    "name": "TAB-Austria - Quizard/",
    "url": "https://myrient.erista.me/files/Redump/TAB-Austria%20-%20Quizard/"
  },
  {
    "name": "Tomy - Kiss-Site/",
    "url": "https://myrient.erista.me/files/Redump/Tomy%20-%20Kiss-Site/"
  },
  {
    "name": "VM Labs - NUON/",
    "url": "https://myrient.erista.me/files/Redump/VM%20Labs%20-%20NUON/"
  },
  {
    "name": "VTech - V.Flash & V.Smile Pro/",
    "url": "https://myrient.erista.me/files/Redump/VTech%20-%20V.Flash%20%26%20V.Smile%20Pro/"
  },
  {
    "name": "Video CD/",
    "url": "https://myrient.erista.me/files/Redump/Video%20CD/"
  },
  {
    "name": "ZAPiT Games - Game Wave Family Entertainment System/",
    "url": "https://myrient.erista.me/files/Redump/ZAPiT%20Games%20-%20Game%20Wave%20Family%20Entertainment%20System/"
  },
  {
    "name": "funworld - Photo Play/",
    "url": "https://myrient.erista.me/files/Redump/funworld%20-%20Photo%20Play/"
  },
  {
    "name": "Erista",
    "url": "https://myrient.erista.me/files/Redump/https://erista.me/"
  },
  {
    "name": "Non-Affiliation Disclaimer",
    "url": "https://myrient.erista.me/files/Redump//non-affiliation-disclaimer/"
  },
  {
    "name": "DMCA",
    "url": "https://myrient.erista.me/files/Redump//dmca/"
  }
]
