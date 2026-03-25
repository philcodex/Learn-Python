import os
import platform
from datetime import datetime

# print("=" * 40)
# print("  OS INFO")
# print("=" * 40)
print(os.getcwd())

# Current directory
print(f"\n📁 Current directory:\n   {os.getcwd()}")


# Files in current directory
files = os.listdir(".")
print(f"\n📂 Files in current directory ({len(files)} items):")
for f in sorted(files):
    if os.path.isdir(f):
        print(f"   [DIR]  {f}")
    else:
        size = os.path.getsize(f)
        print(f"   [FILE] {f}  ({size} bytes)")

# Environment info
print(f"\n🖥️  System info:")
print(f"   OS:       {platform.system()} {platform.release()}")
print(f"   Machine:  {platform.machine()}")
print(f"   Python:   {platform.python_version()}")
print(f"   User:     {os.getlogin()}")
print(f"   PID:      {os.getpid()}")
print(f"   Home:     {os.environ.get('HOME', 'N/A')}")

# Timestamp
print(f"\n🕐 Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 40)


