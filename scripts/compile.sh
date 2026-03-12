#!/bin/bash
# Kompilierungs-Skript für LaTeX-Dokument
# Verwendung: cd scripts && ./compile.sh

set -e  # Exit auf Fehler

output=$(mktemp -t latexbuild.XXXXXX)

echo "🔨 Kompiliere LaTeX-Dokument..."
echo "================================"

# Wechsle zum Parent-Verzeichnis (wo main.tex liegt)
cd ..

# Erste Kompilierung mit pdflatex
echo "① Erste pdflatex-Kompilierung..."
pdflatex -interaction=nonstopmode -halt-on-error main.tex > "$output" 2>&1 || {
    echo "❌ Fehler bei der pdflatex-Kompilierung:"
    tail -20 "$output"
    exit 1
}

# BibTeX für Literaturverzeichnis
if [ -f main.aux ]; then
    echo "② Kompiliere Literaturverzeichnis (BibTeX)..."
    bibtex main > "$output" 2>&1 || {
        echo "⚠️  Warnung bei BibTeX (ignoriert)"
    }
fi

# Zweite Kompilierung für Referenzen
echo "③ Zweite pdflatex-Kompilierung..."
pdflatex -interaction=nonstopmode -halt-on-error main.tex > "$output" 2>&1 || {
    echo "❌ Fehler bei zweiter Kompilierung:"
    tail -20 "$output"
    exit 1
}

# Dritte Kompilierung für finale Links
echo "④ Dritte pdflatex-Kompilierung..."
pdflatex -interaction=nonstopmode -halt-on-error main.tex > "$output" 2>&1 || {
    echo "❌ Fehler bei dritter Kompilierung:"
    tail -20 "$output"
    exit 1
}

echo ""
echo "✅ Kompilierung erfolgreich abgeschlossen!"
echo "📄 PDF erstellt: main.pdf"
echo ""

# Aufräumen
rm -f "$output"
rm -f main.out main.log main.aux main.toc main.lof main.lot
rm -f main.blg main.bbl
