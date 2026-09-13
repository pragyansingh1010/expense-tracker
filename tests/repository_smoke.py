from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
page = ROOT / "expense tracker.html"
assert page.exists(), "main expense tracker page is missing"
html = page.read_text(encoding="utf-8")
assert "<html" in html.lower()
assert "<script" in html.lower()
print("Expense Tracker smoke check passed")
