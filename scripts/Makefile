# Simple Makefile for LaTeX projects
# Uses latexmk for automatic dependency handling

MAIN = main
BUILD_DIR = ../build
SCRIPTS_DIR = .

.PHONY: all clean view help

all:
	@mkdir -p $(BUILD_DIR)
	latexmk -pdf -shell-escape -outdir=$(BUILD_DIR) -cd ../$(MAIN).tex
	@cp $(BUILD_DIR)/$(MAIN).pdf ../$(MAIN).pdf

clean:
	@rm -rf $(BUILD_DIR)
	@rm -f ../$(MAIN).pdf
	@rm -f ../$(MAIN).synctex.gz
	@rm -rf ../_minted-*

view: all
	open ../$(MAIN).pdf

help:
	@echo "Usage:"
	@echo "  make all   - Compile the document"
	@echo "  make clean - Remove build artifacts"
	@echo "  make view  - Compile and open the PDF"
