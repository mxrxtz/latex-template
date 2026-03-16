#!/usr/bin/env python3
import os
import shutil
import sys
import re
import subprocess
import argparse
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

def run_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def setup_project():
    parser = argparse.ArgumentParser(description="Professional LaTeX Template Wizard")
    parser.add_argument("--name", help="Project folder name")
    parser.add_argument("--author", help="Author name")
    parser.add_argument("--title", help="Work title")
    parser.add_argument("--uni", help="University name")
    parser.add_argument("--inst", help="Institute/Department name")
    parser.add_argument("--preset", choices=["standard", "labreport"], help="Template preset (standard or labreport)")
    parser.add_argument("--abstract", choices=["y", "n"], help="Include abstract (y/n)")
    parser.add_argument("-y", "--yes", action="store_true", help="Skip prompts and use defaults")
    
    args = parser.parse_args()

    print("\033[1;34m" + "="*50 + "\033[0m")
    print("\033[1;34m   LaTeX Template: New Project Wizard\033[0m")
    print("\033[1;34m" + "="*50 + "\033[0m\n")

    # 1. Collect Information
    if args.yes:
        project_name = args.name or "my-academic-work"
        author_name = args.author or "Your Name"
        work_title = args.title or "Title of your Work"
        university = args.uni or "Your University"
        institute = args.inst or "Your Department"
        preset = args.preset or "standard"
        include_abstract = "1" if (args.abstract or "y") == "y" else "0"
    else:
        project_name = args.name or prompt("Project Name", "my-academic-work")
        author_name = args.author or prompt("Author Name", "Your Name")
        work_title = args.title or prompt("Work Title", "Title of your Work")
        university = args.uni or prompt("University", "Your University")
        institute = args.inst or prompt("Institute", "Your Department")
        
        if not args.preset:
            print("\n  \033[1mChoose Template Preset:\033[0m")
            print("  - standard:   Standard Scientific Work")
            print("  - labreport:  Lab Report / Protocol")
            preset = prompt("Preset (standard or labreport)", "standard")
        else:
            preset = args.preset
            
        if not args.abstract:
            include_abstract = "1" if prompt("Include Abstract? (y/n)", "y").lower() == "y" else "0"
        else:
            include_abstract = "1" if args.abstract == "y" else "0"

    project_slug = slugify(project_name)
    
    if os.path.exists(project_slug):
        print(f"\n\033[91mError: Directory '{project_slug}' already exists.\033[0m")
        sys.exit(1)

    # 2. Clone the repository
    print(f"\n\033[93mFetching template from GitHub...\033[0m")
    repo_urls = [
        "https://github.com/mxrxtz/latex-template.git",
        "git@github.com:mxrxtz/latex-template.git"
    ]
    
    success = False
    for url in repo_urls:
        if run_command(f"git clone --depth 1 {url} {project_slug}"):
            success = True
            break
    
    if not success:
        print(f"\033[91mError: Could not download the template. Please check your internet connection and Git access.\033[0m")
        sys.exit(1)

    # 3. Clean up the cloned directory
    print(f"\033[1;32mConfiguring your project...\033[0m")
    
    to_remove = [
        os.path.join(project_slug, ".git"),
        os.path.join(project_slug, "create-latex.py"),
        os.path.join(project_slug, "package.json"),
        os.path.join(project_slug, "package-lock.json"),
        os.path.join(project_slug, "node_modules"),
        os.path.join(project_slug, "main.pdf"),
    ]
    
    for path in to_remove:
        if os.path.exists(path):
            if os.path.isdir(path): shutil.rmtree(path)
            else: os.remove(path)

    # 4. Perform replacements
    def update_file(path, replacements):
        full_path = os.path.join(project_slug, path)
        if not os.path.exists(full_path):
            return
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
            for pattern, replacement in replacements.items():
                content = re.sub(pattern, replacement, content)
            with open(full_path, "w", encoding="utf-8") as f:
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

    update_file(os.path.join("config", "commands.tex"), preamble_replacements)
    update_file("main.tex", main_replacements)

    # 5. Final message
    if not shutil.which("pdflatex"):
        print("\n\033[93mNote: 'pdflatex' not found. Install TeX Live or MacTeX to compile.\033[0m")

    print("\n\033[1;32mSuccess! Your project is ready.\033[0m")
    print(f"\nNext steps:\n  \033[1mcd {project_slug}\033[0m")
    print("  \033[1mpdflatex main.tex\033[0m\n")

if __name__ == "__main__":
    try:
        setup_project()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        sys.exit(0)
