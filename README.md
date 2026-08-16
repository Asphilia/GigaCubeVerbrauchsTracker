# GigaCube Verbrauchs Tracker

Ich habe mich immer gefragt, wie mein aktueller Verbrauch ist und ob ich diesen in meinem Verbrauchszeitraum einhalten werde.  
Genau dafür ist diese App da.

## Aktuelle Version
Version 0.1  
Es handelt sich hierbei um eine Testversion! Einzig der Backend-Test funktioniert und schreibt einmalig bei Ausführung den aktuellen Verbrauch in eine CSV.  

## Geplante Features
- [ ] Eingabe von Aktualisierungshäufigkeit
- [x] Lokale Speicherung der Verbrauchsdaten
- [ ] Anzeige des aktuellen Verbrauchs
- [ ] Anzeige des aktuell noch verfügbaren Datenvolumens
- [ ] Grafische Ansicht vom Datenvolumenverbrauch
- [ ] Grafische Ansicht der Veränderung des Durchschnittsverbrauchs
- [ ] Einstellung für Berechnung des Durchschnittsverbrauchs
- [ ] Prognose auf Basis des Durchschnittsverbrauchs
- [ ] Analyse des Durchschnittsverbrauchs
- [ ] Prognose auf Basis der Analyse des Durchschnittsverbrauchs
- [ ] Weitere Datenspeicherungsmöglichkeiten und Einstellungen

## Voraussetzung
Damit diese App funktioniert, muss sie auf einem Gerät laufen, dass im Netzwerk des GigaCubes ist.  
Über http://center.vodafone.de werden die Verbrauchsdaten extrahiert und gespeichert.  

## Installation
Bisher nur als Python-Skript.

## Code-Qualität
Komplett selbst gecoded, ohne Vibe-Coding.

## Nutzung
Clone dieses Repo
```
git clone https://github.com/Asphilia/GigaCubeVerbrauchsTracker.git
cd GigaCubeVerbrauchsTracker
```
Empfohlen, aber optional: Erstelle eine Venv
```
python3 -m venv .venv
source .venv/bin/activate
```
Installiere die Requirements
```
pip install -r requirements.txt
```
Ändere in `app/settings.yaml` den `saving_directory` Pfad. Mindestens die `~` muss aufgelöst sein.  
Führe Backend aus. Dies führt die Tests aus und schreibt deinen aktuellen Verbrauch in eine CSV Datei im `saving_directory`.
```
cd app
python backend.py
```

## Autoren
Asphilia  