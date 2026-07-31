# Setup Notes: Google-EmailScraper (kennyledet)

## Environment & Requirements
- **Language**: Python 2.6 / 2.7 (Legacy)
- **Dependencies**: `urllib2`, `xgoogle` library (bundled in repo).

## Installation & Runtime Issues
- **SyntaxError**: Fails under Python 3 (`except Exception, e:` is invalid Python 3 syntax).
- **ModuleNotFoundError**: Imports `urllib2`, which was replaced by `urllib.request` in Python 3.
- **Obsolete Google Parser**: `xgoogle` parses raw Google search HTML, which Google has blocked and changed significantly since 2013 (resulting in 429 / CAPTCHA blocks).

## Conclusion
- Cannot execute under modern Python 3.x environments without heavy refactoring.
