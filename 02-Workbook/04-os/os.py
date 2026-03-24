import os
import platform
from datetime import datetime

# ── Header ────────────────────────────────────────────────────────────────────
print("=" * 40)
print("         SYSTEM INFO")
print("=" * 40)

# ── System ────────────────────────────────────────────────────────────────────
print("\n🖥️  System")
print(f"   OS:       {platform.system()} {platform.release()}")
print(f"   Machine:  {platform.machine()}")
print(f"   Python:   {platform.python_version()}")
print(f"   PID:      {os.getpid()}")
print(f"   Home:     {os.environ.get('HOME', 'N/A')}")

# os.getlogin() can fail on some systems, so we use a try/except to be safe
try:
    print(f"   User:     {os.getlogin()}")
except Exception:
    print(f"   User:     {os.environ.get('USER', 'Unknown')}")

# ── Current folder ────────────────────────────────────────────────────────────
print("\n📂  Files in current folder")
print(f"   {os.getcwd()}\n")

files = sorted(os.listdir("."))           # get all items, sorted A–Z
for name in files:
    if os.path.isdir(name):               # is it a folder?
        print(f"   [DIR]  {name}")
    else:
        size = os.path.getsize(name)      # file size in bytes
        print(f"   [FILE] {name}  ({size} bytes)")

# ── Timestamp ─────────────────────────────────────────────────────────────────
now = datetime.now()
print(f"\n🕐  Run at: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 40)