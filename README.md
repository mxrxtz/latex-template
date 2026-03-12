# LaTeX-Template für wissenschaftliche Arbeiten

Ein professionelles, modulares und wiederverwendbares LaTeX-Template mit sauberer Ordnerstruktur.

## 🚀 Schnelleinstieg

1. **Dokumentation lesen**: Öffne [docs/QUICKSTART.txt](docs/QUICKSTART.txt)
2. **Konfiguration anpassen**: Bearbeite [config/preamble.tex](config/preamble.tex)
3. **Kapitel schreiben**: Öffne die Dateien in [chapters/](chapters/)
4. **Kompilieren**: 
   - **VS Code**: `Ctrl+Shift+B` 
   - **Terminal**: `cd scripts && make all`

## 📁 Ordnerstruktur

```
.
├── main.tex                    # Hauptdatei (kompiliere diese)
├── references.bib              # Deine Literaturquellen
├── .gitignore
│
├── config/
│   └── preamble.tex            # LaTeX-Konfiguration
│
├── chapters/                   # Deine Kapitel
│   ├── 01_introduction.tex
│   ├── 02_methodology.tex
│   ├── 03_results.tex
│   ├── 04_discussion.tex
│   └── 05_conclusion.tex
│
├── sections/
│   └── appendix.tex            # Anhang
│
├── figures/                    # Deine Bilder hier
├── data/                       # Rohdaten (optional)
│
├── docs/                       # Dokumentation
│   ├── README.md               # Ausführliche Doku
│   ├── QUICKSTART.txt          # Erste Schritte
│   └── ADVANCED_TIPS.txt       # Fortgeschrittene Tipps
│
├── scripts/                    # Build-Tools
│   ├── Makefile
│   └── compile.sh
│
└── build/                      # Kompilierungs-Output
```

## 📖 Dokumentation

- **[docs/QUICKSTART.txt](docs/QUICKSTART.txt)** – Schnelleinstieg (empfohlen!)
- **[docs/README.md](docs/README.md)** – Ausführliche Dokumentation
- **[docs/ADVANCED_TIPS.txt](docs/ADVANCED_TIPS.txt)** – Tipps & Tricks

## ✨ Features

✅ Professionelle deutsche LaTeX-Vorlage  
✅ Modulare Struktur (einfach zu erweitern)  
✅ Pre-konfiguriert: Mathe, Grafiken, Tabellen, Code-Highlighting  
✅ BibTeX-Integration für Literaturverwaltung  
✅ Automatisierte Kompilierung (Make/Bash-Skript)  
✅ Saubere Git-Ignores  

## 💡 Hilfreiche Tipps

- **Schnelle Kompilierung**: `make -C scripts all`
- **PDF anschauen**: `make -C scripts view`
- **Aufräumen**: `make -C scripts clean`
- **Zitieren**: `\cite{Autor2023}` im Text verwenden
- **Abbildungen**: In `figures/` ablegen, dann `\includegraphics{figures/...}` nutzen

---

**Viel Erfolg bei deiner wissenschaftlichen Arbeit! Lese zuerst [QUICKSTART](docs/QUICKSTART.txt)** 📚✨
