# Presets für LaTeX Template

Dieses Verzeichnis enthält verschiedene Presets (Vorlagen) für verschiedene Dokumenttypen.

## Presets verwenden

In `main.tex` kannst du das aktuelle Preset mit dieser Zeile einstellen:

```latex
\def\currentPreset{1}  % oder 2 für Preset 2
```

## Verfügbare Presets

### Preset 1: Standard wissenschaftliche Arbeit
- Einfache Standard-Titelseite mit LaTeX `\maketitle`
- Ideal für: Bachelor-, Masterarbeiten, wissenschaftliche Paper

### Preset 2: Laborberichterstattung
- Spezielles Deckblatt für Laborberichte
- Zeigt Universität und Institut
- Ideal für: Experimentelle Arbeiten, Praktikumsberichte

## Eigene Presets erstellen

1. Neuen Ordner erstellen: `presets/preset3/`
2. `titlepage.tex` in den neuen Ordner kopieren und anpassen
3. In `main.tex` die Preset-Definition aktualisieren (`currentPreset`)
4. Optional: `titlepage.tex` um ein Deckblatt (`coverpage.tex`) erweitern
