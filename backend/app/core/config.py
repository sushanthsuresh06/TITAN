from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

APP_NAME = "TITAN Forensic Analysis Platform"
APP_VERSION = "0.1.0"

EVIDENCE_DIR = BASE_DIR / "evidence"
REPORTS_DIR = BASE_DIR / "reports"

EVIDENCE_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)