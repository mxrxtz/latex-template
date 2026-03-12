# Makefile für LaTeX-Projekt
# Verwendung: make, make clean, make view, etc.
# Hinweis: Dieses Makefile sollte aus dem scripts/ Ordner aufgerufen werden

MAIN = ../main
LATEX = pdflatex
BIBTEX = bibtex
VIEWER = open  # Mac: 'open', Linux: 'xdg-open' oder 'evince'
RM = rm -f

.PHONY: all clean view edit help

# Standardziel
all: $(MAIN).pdf

# PDF erzeugen
$(MAIN).pdf: $(MAIN).tex
	@echo "🔨 Kompiliere LaTeX..."
	cd .. && $(LATEX) -interaction=nonstopmode -halt-on-error main.tex
	@echo "② BibTeX..."
	cd .. && $(BIBTEX) main || true
	@echo "③ Zweite Kompilierung..."
	cd .. && $(LATEX) -interaction=nonstopmode -halt-on-error main.tex
	@echo "④ Dritte Kompilierung..."
	cd .. && $(LATEX) -interaction=nonstopmode -halt-on-error main.tex
	@echo "✅ Fertig: ../main.pdf"

# PDF anschauen
view: $(MAIN).pdf
	$(VIEWER) $(MAIN).pdf &

# Editor öffnen
edit:
	code ..

# Aufräumen (temporäre Dateien)
clean:
	cd .. && \
	$(RM) main.aux main.log main.out main.toc \
	$(RM) main.lof main.lot main.bbl main.blg \
	$(RM) main.fls main.fdb_latexmk \
	$(RM) *~
	@echo "🧹 Temporäre Dateien gelöscht"

# Tiefe Reinigung (löscht auch PDF)
distclean: clean
	$(RM) $(MAIN).pdf
	@echo "🗑️  PDF gelöscht"

# Nur BibTeX neu kompilieren
bibtex:
	cd .. && \
	$(BIBTEX) main && \
	$(LATEX) -interaction=nonstopmode -halt-on-error main.tex && \
	$(LATEX) -interaction=nonstopmode -halt-on-error main.tex

# Watch-Modus (benötigt entr oder inotify-tools)
watch:
	@echo "👁️  Überwache Dateiänderungen..."
	@cd .. && while true; do \
		inotifywait -e modify chapters/*.tex sections/*.tex config/*.tex references.bib; \
		$(MAKE) -C scripts all; \
	done

# Hilfe
help:
	@echo "📖 LaTeX-Makefile Befehle:"
	@echo "  make all       - Kompiliere die PDF (Standard)"
	@echo "  make view      - Öffne die PDF"
	@echo "  make edit      - Öffne Projekt in VS Code"
	@echo "  make clean     - Lösche temporäre Dateien"
	@echo "  make distclean - Lösche alles inklusive PDF"
	@echo "  make bibtex    - Nur Literaturverzeichnis neu kompilieren"
	@echo "  make watch     - Überwache Dateien und kompiliere automatisch"
	@echo "  make help      - Zeige diese Hilfe"
