#!/usr/bin/env python3
import os
import shutil
import sys
import re
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text

def prompt(question, default=None):
    if default:
        res = input(f"  \033[1m{question}\033[0m [{default}]: ").strip()
        return res if res else default
    return input(f"  \033[1m{question}\033[0m: ").strip()

def check_dependencies():
    if not shutil.which("pdflatex"):
        print("\n\033[93mWarning: 'pdflatex' was not found in your PATH.\033[0m")
        print("You will need a LaTeX distribution (like TeX Live or MiKTeX) to compile your documents.")

def setup_project():
    print("\033[1;34m" + "="*50 + "\033[0m")
    print("\033[1;34m   LaTeX Template: New Project Wizard\033[0m")
    print("\033[1;34m" + "="*50 + "\033[0m\n")

    # 1. Collect Information
    raw_name = prompt("Project Name", "my-academic-work")
    project_slug = slugify(raw_name)
    
    if os.path.exists(project_slug):
        print(f"\n\033[91mError: Directory '{project_slug}' already exists.\033[0m")
        sys.exit(1)

    author_name = prompt("Author Name", "Your Name")
    work_title = prompt("Work Title", "Title of your Work")
    university = prompt("University", "Your University")
    institute = prompt("Institute", "Your Department")
    
    print("\n  \033[1mChoose Template Preset:\033[0m")
    print("  1: Standard Scientific Work")
    print("  2: Lab Report / Protocol")
    preset = prompt("Preset (1 or 2)", "1")
    
    include_abstract = "1" if prompt("Include Abstract? (y/n)", "y").lower() == "y" else "0"

    print(f"\n\033[1;32mCreating project in '{project_slug}'...\033[0m")
    os.makedirs(project_slug)

    # 2. Define source and exclude list
    source_dir = os.path.dirname(os.path.abspath(__file__))
    exclude_items = {
        ".git", "__pycache__", "create-latex.py", "main.pdf", 
        "_minted", "build", project_slug, "cookiecutter", ".DS_Store"
    }

    # 3. Copy files
    for item in os.listdir(source_dir):
        if item in exclude_items:
            continue
        
        s = os.path.join(source_dir, item)
        d = os.path.join(project_slug, item)

        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    # 4. Perform replacements
    def update_file(path, replacements):
        if not os.path.exists(path):
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            for pattern, replacement in replacements.items():
                content = re.sub(pattern, replacement, content)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"\033[91mWarning: Could not update {path}: {e}\033[0m")

    preamble_replacements = {
        r'\\def\\workTitle\{.*?\}': f'\\\\def\\\\workTitle{{{work_title}}}',
        r'\\def\\workAuthor\{.*?\}': f'\\\\def\\\\workAuthor{{{author_name}}}',
        r'\\def\\workUniversity\{.*?\}': f'\\\\def\\\\workUniversity{{{university}}}',
        r'\\def\\workInstitute\{.*?\}': f'\\\\def\\\\workInstitute{{{institute}}}',
    }
    
    main_replacements = {
        r'\\def\\currentPreset\{.*?\}': f'\\\\def\\\\currentPreset{{{preset}}}',
        r'\\def\\includeAbstract\{.*?\}': f'\\\\def\\\\includeAbstract{{{include_abstract}}}',
    }

    update_file(os.path.join(project_slug, "config", "preamble.tex"), preamble_replacements)
    update_file(os.path.join(project_slug, "main.tex"), main_replacements)

    check_dependencies()

    print("\n\033[1;32mSuccess! Your project is ready.\033[0m")
    print(f"\nNext steps:\n  \033[1mcd {project_slug}\033[0m")
    print("  \033[1mmake -C scripts all\033[0m  (or run pdflatex main.tex)\n")

if __name__ == "__main__":
    try:
        setup_project()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        sys.exit(0)
