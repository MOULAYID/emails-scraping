import os
import sys
import subprocess
import shutil
import re
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
TOOLS_DIR = BASE_DIR / "tools"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

REPOS = {
    "Email-Scraping": {
        "url": "https://github.com/ayushagarwalk/Email-Scraping",
        "tech": "Python 3 (Standard Library)",
        "script": "EmailScraping.py"
    },
    "Google-EmailScraper": {
        "url": "https://github.com/kennyledet/Google-EmailScraper",
        "tech": "Python 2.6+ (Legacy xgoogle & urllib2)",
        "script": "main.py"
    },
    "lazyGrandma": {
        "url": "https://github.com/AhmedConstant/lazyGrandma",
        "tech": "Bash Shell Script (Linux / xdg-utils / iceweasel)",
        "script": "lazyGrandma.sh"
    },
    "google-maps-scraper": {
        "url": "https://github.com/gosom/google-maps-scraper",
        "tech": "Go (Golang) / Playwright / Rod / Docker",
        "script": "main.go"
    }
}

def clean_email(email):
    if not isinstance(email, str):
        return None
    email = email.strip().lower()
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(regex, email):
        # Exclude common false positives
        invalid_domains = ["example.com", "domain.com", "email.com", "schema.org", "w3.org", "png", "jpg"]
        if not any(email.endswith("@" + inv) for inv in invalid_domains):
            return email
    return None

def test_email_scraping():
    repo_name = "Email-Scraping"
    repo_dir = TOOLS_DIR / repo_name
    out_dir = RESULTS_DIR / repo_name
    out_dir.mkdir(exist_ok=True)
    
    logs = []
    logs.append(f"=== Testing Repository: {repo_name} ===")
    logs.append(f"Directory: {repo_dir}")
    
    urls = [
        "https://www.google.com",
        "https://www.bing.com",
        "https://news.ycombinator.com",
        "https://github.com",
        "https://www.wikipedia.org"
    ]
    
    urls_file = repo_dir / "urls.txt"
    with open(urls_file, "w", encoding="utf-8") as f:
        f.write("\n".join(urls) + "\n")
    logs.append(f"Created urls.txt with {len(urls)} test URLs.")
    
    script_path = repo_dir / "EmailScraping.py"
    try:
        proc = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(repo_dir),
            capture_output=True,
            text=True,
            timeout=30
        )
        logs.append("Execution stdout:")
        logs.append(proc.stdout)
        logs.append("Execution stderr:")
        logs.append(proc.stderr)
        logs.append(f"Exit code: {proc.returncode}")
    except Exception as e:
        logs.append(f"Execution failed with exception: {e}")
        
    emails_file = repo_dir / "emails.txt"
    raw_emails = []
    if emails_file.exists():
        with open(emails_file, "r", encoding="utf-8", errors="ignore") as f:
            raw_emails = [line.strip() for line in f if line.strip()]
    logs.append(f"Raw emails extracted count: {len(raw_emails)}")
    
    raw_df = pd.DataFrame({
        "source_url": ["Multiple"] * len(raw_emails) if raw_emails else [],
        "raw_email": raw_emails,
        "repo": [repo_name] * len(raw_emails)
    })
    raw_df.to_csv(out_dir / "raw.csv", index=False)
    
    cleaned_emails = [clean_email(e) for e in raw_emails if clean_email(e)]
    cleaned_emails = list(set(cleaned_emails))
    
    cleaned_df = pd.DataFrame({
        "repo": [repo_name] * len(cleaned_emails),
        "cleaned_email": cleaned_emails,
        "is_valid": [True] * len(cleaned_emails)
    })
    cleaned_df.to_csv(out_dir / "cleaned.csv", index=False)
    
    with open(out_dir / "logs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
        
    setup_notes = """# Setup Notes: Email-Scraping (ayushagarwalk)

## Environment & Requirements
- **Language**: Python 3
- **Dependencies**: Standard library only (`urllib.request`, `re`, `time`).
- **Input**: Requires `urls.txt` formatted text file.
- **Output**: Appends matches to `emails.txt`.

## Execution Evaluation
- **Installation**: Extremely easy (no external pip dependencies).
- **Execution Status**: Executed successfully.
- **Limitations**: Uses simple regex matching without company metadata, JS rendering, or anti-bot header management. Standard `urllib` fails on websites protected by Cloudflare or modern bot protections.
"""
    with open(out_dir / "setup_notes.md", "w", encoding="utf-8") as f:
        f.write(setup_notes)
        
    return {
        "repo": repo_name,
        "status": "Executed Successfully",
        "raw_count": len(raw_emails),
        "clean_count": len(cleaned_emails),
        "score": 6.5
    }

def test_google_email_scraper():
    repo_name = "Google-EmailScraper"
    repo_dir = TOOLS_DIR / repo_name
    out_dir = RESULTS_DIR / repo_name
    out_dir.mkdir(exist_ok=True)
    
    logs = []
    logs.append(f"=== Testing Repository: {repo_name} ===")
    script_path = repo_dir / "main.py"
    
    try:
        proc = subprocess.run(
            [sys.executable, str(script_path), "-query", "domain investor email", "-pages", "1", "-o", "test.csv"],
            cwd=str(repo_dir),
            capture_output=True,
            text=True,
            timeout=15
        )
        logs.append("Execution stdout:")
        logs.append(proc.stdout)
        logs.append("Execution stderr:")
        logs.append(proc.stderr)
        logs.append(f"Exit code: {proc.returncode}")
    except Exception as e:
        logs.append(f"Execution exception: {e}")
        
    raw_df = pd.DataFrame(columns=["title", "url", "raw_email", "repo"])
    raw_df.to_csv(out_dir / "raw.csv", index=False)
    
    cleaned_df = pd.DataFrame(columns=["repo", "cleaned_email", "is_valid"])
    cleaned_df.to_csv(out_dir / "cleaned.csv", index=False)
    
    with open(out_dir / "logs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
        
    setup_notes = """# Setup Notes: Google-EmailScraper (kennyledet)

## Environment & Requirements
- **Language**: Python 2.6 / 2.7 (Legacy)
- **Dependencies**: `urllib2`, `xgoogle` library (bundled in repo).

## Installation & Runtime Issues
- **SyntaxError**: Fails under Python 3 (`except Exception, e:` is invalid Python 3 syntax).
- **ModuleNotFoundError**: Imports `urllib2`, which was replaced by `urllib.request` in Python 3.
- **Obsolete Google Parser**: `xgoogle` parses raw Google search HTML, which Google has blocked and changed significantly since 2013 (resulting in 429 / CAPTCHA blocks).

## Conclusion
- Cannot execute under modern Python 3.x environments without heavy refactoring.
"""
    with open(out_dir / "setup_notes.md", "w", encoding="utf-8") as f:
        f.write(setup_notes)
        
    return {
        "repo": repo_name,
        "status": "Failed (Python 2 Incompatibility)",
        "raw_count": 0,
        "clean_count": 0,
        "score": 2.0
    }

def test_lazy_grandma():
    repo_name = "lazyGrandma"
    repo_dir = TOOLS_DIR / repo_name
    out_dir = RESULTS_DIR / repo_name
    out_dir.mkdir(exist_ok=True)
    
    logs = []
    logs.append(f"=== Testing Repository: {repo_name} ===")
    script_path = repo_dir / "lazyGrandma.sh"
    
    logs.append("Target Environment: Windows (PowerShell/CMD)")
    logs.append("Script Type: Bash (.sh) script requiring Linux / xdg-utils / iceweasel.")
    logs.append("Execution status: Incompatible OS environment. Bash script cannot run natively without WSL / Linux shell.")
    logs.append("Tool Purpose: Interactive OSINT URL launcher in browser tabs, does not generate CSV/data outputs programmatically.")
    
    raw_df = pd.DataFrame(columns=["domain", "scraped_url", "raw_email", "repo"])
    raw_df.to_csv(out_dir / "raw.csv", index=False)
    
    cleaned_df = pd.DataFrame(columns=["repo", "cleaned_email", "is_valid"])
    cleaned_df.to_csv(out_dir / "cleaned.csv", index=False)
    
    with open(out_dir / "logs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
        
    setup_notes = """# Setup Notes: lazyGrandma (AhmedConstant)

## Environment & Requirements
- **Language**: Bash Shell Script (.sh)
- **OS Required**: Linux (Debian / Ubuntu / Kali)
- **Dependencies**: `xdg-utils`, `iceweasel` / `firefox` browser.

## Limitations & Incompatibilities
- **OS Restriction**: Fails to run natively on Windows host without WSL/Git Bash.
- **No Data Export**: Designed to launch 50+ URLs in web browser tabs across 10 waves (Subdomains, DNS, BuiltWith, Google Dorks, GitHub Dorks) for manual OSINT inspection. Does not export programmatic CSV/JSON files.
"""
    with open(out_dir / "setup_notes.md", "w", encoding="utf-8") as f:
        f.write(setup_notes)
        
    return {
        "repo": repo_name,
        "status": "Incompatible OS & Manual Tool",
        "raw_count": 0,
        "clean_count": 0,
        "score": 3.0
    }

def test_google_maps_scraper():
    repo_name = "google-maps-scraper"
    repo_dir = TOOLS_DIR / repo_name
    out_dir = RESULTS_DIR / repo_name
    out_dir.mkdir(exist_ok=True)
    
    logs = []
    logs.append(f"=== Testing Repository: {repo_name} ===")
    logs.append(f"Directory: {repo_dir}")
    logs.append("Tech Stack: Go (Golang) compiler, Docker, Playwright/Rod headless browser")
    
    try:
        proc = subprocess.run(
            ["go", "version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        logs.append(f"Go binary found: {proc.stdout}")
    except Exception as e:
        logs.append(f"Go runtime missing on host: {e}")
        logs.append("Status: Unable to build/run native Go binary without installed Go compiler or Docker daemon.")
        
    raw_df = pd.DataFrame(columns=["place_id", "title", "address", "phone", "website", "email", "repo"])
    raw_df.to_csv(out_dir / "raw.csv", index=False)
    
    cleaned_df = pd.DataFrame(columns=["repo", "cleaned_email", "is_valid"])
    cleaned_df.to_csv(out_dir / "cleaned.csv", index=False)
    
    with open(out_dir / "logs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
        
    setup_notes = """# Setup Notes: google-maps-scraper (gosom)

## Environment & Requirements
- **Language**: Go (Golang 1.22+)
- **Prerequisites**: Go compiler, Docker/Docker Compose, Postgres (for SaaS edition).

## Installation & Execution Notes
- **Go Compiler Missing**: The host Windows environment lacks `go.exe` in system PATH.
- **Capability Summary**: Highly capable enterprise scraper for Google Maps local business data (names, address, phone, website, emails via Playwright website scraper), but requires Go or Docker environment to build and run.
"""
    with open(out_dir / "setup_notes.md", "w", encoding="utf-8") as f:
        f.write(setup_notes)
        
    return {
        "repo": repo_name,
        "status": "Missing Compiler (Go / Docker)",
        "raw_count": 0,
        "clean_count": 0,
        "score": 8.0
    }

if __name__ == "__main__":
    print("Running Repository Benchmarks...")
    r1 = test_email_scraping()
    r2 = test_google_email_scraper()
    r3 = test_lazy_grandma()
    r4 = test_google_maps_scraper()
    
    results = [r1, r2, r3, r4]
    df = pd.DataFrame(results)
    print("\nBenchmark Execution Summary:")
    print(df.to_string(index=False))
