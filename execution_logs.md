# Detailed Execution Logs: Full Portfolio Benchmark & Setup Run

**Run Date**: July 31, 2026  
**Environment**: Windows 11 Enterprise | Python 3.14.0 | PowerShell  
**Target Domain Count**: 345 unique domains

---

## 1. Environment Diagnostics
```
Python: Python 3.14.0 (C:\Program Files\Python314\python.exe)
Git: git version 2.40.1.windows.1
Go: CommandNotFoundException (go not found on PATH)
Shell: Windows PowerShell 7.x
```

---

## 2. Repository Setup & Cloning Log

```bash
mkdir -Force tools
cd tools
git clone https://github.com/ayushagarwalk/Email-Scraping
# Status: OK (Cloned to tools/Email-Scraping)

git clone https://github.com/kennyledet/Google-EmailScraper
# Status: OK (Cloned to tools/Google-EmailScraper)

git clone https://github.com/AhmedConstant/lazyGrandma
# Status: OK (Cloned to tools/lazyGrandma)

git clone https://github.com/gosom/google-maps-scraper
# Status: OK (Cloned to tools/google-maps-scraper)
```

---

## 3. Individual Execution Logs

### 3.1 `Email-Scraping`
```
Command: python tools/Email-Scraping/EmailScraping.py
CWD: tools/Email-Scraping
Input: urls.txt (5 URLs)
Stdout:
  1.https://www.google.com   Fetched in : 0.241s
      Number of Emails : 0
  2.https://www.bing.com     Fetched in : 0.198s
      Number of Emails : 0
  3.https://news.ycombinator.com Fetched in : 0.312s
      Number of Emails : 1
  ...
  Elapsed Time: 1.25s
Exit Code: 0
Raw Output: results/Email-Scraping/raw.csv
Cleaned Output: results/Email-Scraping/cleaned.csv (3 unique emails)
```

### 3.2 `Google-EmailScraper`
```
Command: python tools/Google-EmailScraper/main.py -query "domain investor email" -pages 1 -o test.csv
CWD: tools/Google-EmailScraper
Stderr Traceback:
  File "C:\Users\midaouadi\Documents\data analytics projects\emails-scraping\tools\Google-EmailScraper\main.py", line 43
    except Exception, e:
                    ^
  SyntaxError: invalid syntax
Exit Code: 1
Diagnostic Notes: Fails under Python 3 due to Python 2 syntax and missing urllib2 library.
Raw Output: results/Google-EmailScraper/raw.csv (0 rows)
Cleaned Output: results/Google-EmailScraper/cleaned.csv (0 rows)
```

### 3.3 `lazyGrandma`
```
Command: ./lazyGrandma.sh example.com
CWD: tools/lazyGrandma
Stderr:
  ./lazyGrandma.sh: line 14: xdg-open: command not found
  ./lazyGrandma.sh: line 18: iceweasel: command not found
Exit Code: 127
Diagnostic Notes: Incompatible with Windows host. Requires Linux desktop with xdg-open / browser.
Raw Output: results/lazyGrandma/raw.csv (0 rows)
Cleaned Output: results/lazyGrandma/cleaned.csv (0 rows)
```

### 3.4 `google-maps-scraper`
```
Command: go version
Stderr:
  go : Le terme 'go' n'est pas reconnu comme nom d'applet de commande...
Exit Code: 1
Diagnostic Notes: Go runtime compiler not found on host Windows system PATH.
Raw Output: results/google-maps-scraper/raw.csv (0 rows)
Cleaned Output: results/google-maps-scraper/cleaned.csv (0 rows)
```

---

## 4. Master Dataset Generation Log (Filtered TLD & Holding Company Run)

```
Input: domains_list.csv (345 unique domains)
Filter Condition 1: Excluded company_name IN ['Atom Inc. (formerly Squadhelp)', 'Replit Inc.', 'NEOM Company']
Filter Condition 2: Excluded target_domain ENDSWITH ('.link', '.info')
Engine: prospecting_engine.py -> build_master_dataset.py
Output Files:
  - master_prospects.csv (62 rows, 17 columns)
  - master_prospects.xlsx (OpenPyXL formatted, custom widths & header styling, 62 rows)
Status: Completed successfully without errors.
```
