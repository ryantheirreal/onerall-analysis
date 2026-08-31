import re
from pathlib import Path

html = Path(r"C:\Users\Dell\Desktop\onerall-analysis\public\index.html").read_text(encoding="utf-8")

print("TITLE :", (re.search(r"<title>(.*?)</title>", html) or [None, "?"])[1])
m = re.search(r'name="description" content="([^"]+)"', html)
print("DESC  :", m.group(1) if m else "?")
m = re.search(r'property="og:title" content="([^"]+)"', html)
print("OG    :", m.group(1) if m else "?")
m = re.search(r'property="og:url" content="([^"]+)"', html)
print("OGURL :", m.group(1) if m else "?")
m = re.search(r'rel="canonical" href="([^"]+)"', html)
print("CANON :", m.group(1) if m else "n/a")
print()
print("Artificial Analysis restantes:", html.count("Artificial Analysis"))
print("Onerall Analysis AI  no HTML :", html.count("Onerall Analysis AI"))