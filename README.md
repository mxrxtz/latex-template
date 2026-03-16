# 🎓 Professional LaTeX Template

A modular, clean, and ready-to-use LaTeX template for scientific papers, theses, and lab reports. Optimized for ease of use and professional results.

## 🚀 Quick Start (Recommended)

The easiest way to start a new project is to run the setup wizard directly from GitHub. You don't even need to clone this repo!

Using **bun**:
```bash
bun x github:mxrxtz/latex-template
```

Using **npx**:
```bash
npx github:mxrxtz/latex-template
```

Follow the prompts to enter your name, work title, university, and choose between a **Standard Paper** or a **Lab Report**.

---

## 🛠 For Local Development
If you have already cloned the repository:
```bash
./create-latex.py
```

## ✨ Features

- **Modular Structure**: Organized folders for chapters, figures, and configuration.
- **Two Presets**:
  - `Preset 1`: Classic scientific work (Thesis, Paper).
  - `Preset 2`: Lab report/Protocol style with a custom title page.
- **Pre-configured**: Includes packages for math, graphics, tables, units (SI), and code highlighting (`minted` & `listings`).
- **Automation**: Includes a `Makefile` and `compile.sh` for easy PDF generation.
- **Bilingual Support**: Configured for German (ngerman) by default, easily adjustable.

---

## 📁 Project Structure

```text
.
├── main.tex           # Main document entry point
├── create-latex.py    # ✨ Interactive setup wizard
├── config/            # Packages and global settings
├── chapters/          # Your main content (Introduction, Results, etc.)
├── presets/           # Different title page styles
├── figures/           # Images and PDFs
├── scripts/           # Build tools (Makefile, scripts)
└── references.bib     # Bibliography (BibTeX)
```

## 🛠 Manual Setup

If you prefer not to use the wizard:
1. Clone this repository.
2. Edit `config/preamble.tex` to set your name and university.
3. Edit `main.tex` to choose your preset (`\def\currentPreset{1}`).
4. Add your content in `chapters/`.
5. Compile with `pdflatex main.tex`.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
