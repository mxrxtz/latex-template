# LaTeX-Template für wissenschaftliche Arbeiten

Ein professionelles, modulares und wiederverwendbares LaTeX-Template zum Erstellen von wissenschaftlichen Arbeiten (Bachelor-, Master- oder Doktorarbeiten, Forschungspapiere, etc.).

## 📋 Features

- **Modulare Struktur**: Jedes Kapitel in einer seperaten Datei
- **Professionelle Formatierung**: Vordefinierte Seitenlayouts, Schriftarten und Abstände
- **Mathematische Unterstützung**: Vollständige LaTeX-Umgebungen für Formeln und Gleichungen
- **Grafiken & Diagramme**: Integration von pgfplots, tikz und benutzerdefinierten Abbildungen
- **Tabellen**: Umfangreiche Tabellen-Formatierung mit booktabs
- **Literaturverwaltung**: BibTeX-Integration für einfache Literaturverwaltung
- **Code-Highlighting**: Syntax-Highlighting für Code-Blöcke
- **Hyperlinks**: Navigierbare PDF mit Hyperlinks und Bookmarks
- **Deutsche Sprache**: Vollständig auf Deutsch mit deutschen Trennmustern

## 📁 Verzeichnisstruktur

```
latex/
├── main.tex                    # Hauptdatei - hier wird alles zusammengefügt
├── references.bib              # Literaturverzeichnis (BibTeX)
├── .gitignore                  # Git-Ignores
│
├── config/
│   └── preamble.tex            # Konfiguration: Pakete, Befehle, Einstellungen
│
├── chapters/                   # Kapitel-Dateien
│   ├── 01_introduction.tex     # Kapitel 1: Einleitung
│   ├── 02_methodology.tex      # Kapitel 2: Methodik
│   ├── 03_results.tex          # Kapitel 3: Ergebnisse
│   ├── 04_discussion.tex       # Kapitel 4: Diskussion
│   └── 05_conclusion.tex       # Kapitel 5: Schlussfolgerung
│
├── sections/                   # Weitere Abschnitte
│   └── appendix.tex            # Anhang
│
├── figures/                    # Ordner für Abbildungen
│   └── (Platzhalter)
│
├── data/                       # Ordner für Rohdaten/Datensätze
│   └── (Platzhalter)
│
├── docs/                       # Dokumentation
│   ├── README.md               # Diese Datei
│   ├── QUICKSTART.txt          # Schnellanleitung
│   └── ADVANCED_TIPS.txt       # Fortgeschrittene Tipps
│
├── scripts/                    # Hilfsskripte
│   ├── compile.sh              # Bash-Kompilierungs-Skript
│   └── Makefile                # Make-Datei für Kompilierung
│
└── build/                      # Kompilierungs-Output (wird generiert)
    └── (Platzhalter)
```

## 🚀 Erste Schritte

### Anforderungen

- **LaTeX-Distribution**: TeX Live (Linux/Mac) oder MiKTeX (Windows)
- **Editor**: VS Code mit LaTeX Workshop Extension, Overleaf, oder TeXShop
- **BibTeX/Biber**: Zum Generieren des Literaturverzeichnisses

### Installation

#### 1. **Linux/Mac**
```bash
# Mit Homebrew auf Mac:
brew install --cask basictex

# Mit apt auf Ubuntu:
sudo apt-get install texlive-full
```

#### 2. **Windows**
Lade MiKTeX herunter: https://miktex.org/

#### 3. **VS Code Setup** (empfohlen)
Installiere die Extension "LaTeX Workshop":
- Öffne VS Code
- Gehe zu Extensions (Ctrl+Shift+X / Cmd+Shift+X)
- Suche nach "LaTeX Workshop"
- Klicke Install

### 📝 Anwendung

1. **Personalisierung**: Öffne `config/preamble.tex` und fülle diese Variablen aus:
   ```latex
   \def\workTitle{Mein Titel}
   \def\workAuthor{Mein Name}
   \def\workUniversity{Meine Universität}
   ```

2. **Inhalte bearbeiten**: Öffne die Dateien in `chapters/` und füge deinen Inhalt ein

3. **Literatur hinzufügen**: Füge Einträge in `references.bib` ein

4. **Abbildungen einfügen**:
   - Platziere deine Bilder im `figures/` Ordner (PNG, JPG, PDF)
   - Nutze in deinen Dokumenten:
     ```latex
     \includegraphics[width=0.8\textwidth]{figures/meinbild.png}
     ```

5. **Kompilieren**: 
   - **VS Code**: Drücke `Ctrl+Shift+B` (oder `Cmd+Shift+B` auf Mac)
   - **Kommandozeile mit Make**: `cd scripts && make all`
   - **Mit Bash-Skript**: `cd scripts && chmod +x compile.sh && ./compile.sh`

## 🎨 Anpassung und Konfiguration

### Seitenformat ändern
In `config/preamble.tex`:
```latex
\usepackage[left=2.5cm, right=2cm, top=2.5cm, bottom=2.5cm]{geometry}
```

### Zeilenabstand anpassen
```latex
\onehalfspacing        % 1.5-facher Abstand (aktuell)
% oder
\doublespacing        % Doppelter Abstand
% oder
\singlespacing        % Einfacher Abstand
```

### Farben für Links ändern
```latex
\hypersetup{
    colorlinks=true,
    linkcolor=blue,      % Ändere Farbe hier
    citecolor=blue,
    urlcolor=blue
}
```

## 📚 Beispiele

### Zitat einfügen
```latex
Nach Smith et al. \cite{Smith2020} gibt es ...
```

### Abbildung einfügen
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/beispiel.png}
    \caption{Beschreibung der Abbildung}
    \label{fig:beispiel}
\end{figure}

Siehe \figref{fig:beispiel} ...
```

### Tabelle einfügen
```latex
\begin{table}[h]
    \centering
    \caption{Titel der Tabelle}
    \label{tab:beispiel}
    \begin{tabular}{lcc}
        \toprule
        \textbf{Spalte 1} & \textbf{Spalte 2} & \textbf{Spalte 3} \\
        \midrule
        Daten & 123 & 45.6 \\
        Daten & 789 & 10.2 \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Mathematische Gleichung
```latex
\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}

Siehe Gleichung \ref{eq:einstein} ...
```

### Code-Block
```latex
\begin{lstlisting}[language=Python]
def hallo():
    print("Welt")
\end{lstlisting}
```

## 🐛 Häufige Fehler

### "Extra alignment tab has been changed to \\cr"
**Problem**: Zu viele `&` in einer Tabelle
**Lösung**: Überprüfe die Spaltenanzahl in `\begin{tabular}{...}`

```latex
% FALSCH:
\begin{tabular}{cc}  % 2 Spalten deklariert
    A & B & C \\     % aber 3 Spalten verwendet
\end{tabular}

% RICHTIG:
\begin{tabular}{ccc} % 3 Spalten
    A & B & C \\
\end{tabular}
```

### "Undefined control sequence"
**Problem**: Paket nicht geladen oder Tippfehler
**Lösung**: Überprüfe `config/preamble.tex` und stelle sicher, dass das notwendige Paket geladen ist

### "Runaway argument"
**Problem**: Fehlende oder falsche geschweifte Klammer
**Lösung**: Suche nach `{` ohne zugehörendes `}`

## 📖 Ressourcen

- [Official LaTeX Documentation](https://www.latex-project.org)
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [TikZ Manual](https://pgf-tikz.github.io/)
- [BibTeX Guide](http://www.ctan.org/pkg/bibtex)

## 💡 Tipps

1. **Regelmäßiges Speichern**: LaTeX kann große Dateien verarbeiten, speichere häufig
2. **Inkrementelles Schreiben**: Schreibe schrittweise, um Fehler früh zu erkennen
3. **Versionskontrolle**: Nutze Git zum Verfolgen von Änderungen
4. **Backup**: Sichere deine Arbeiten regelmäßig
5. **Konsistenz**: Halte dich an die vordefinierten Formate für Überschriften, Tabellen, etc.

## 📝 Lizenz

Dieses Template steht unter der MIT-Lizenz zur Verfügung.

## ✨ Viel Erfolg bei deiner wissenschaftlichen Arbeit!
