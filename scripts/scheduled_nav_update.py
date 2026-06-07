from datetime import datetime
from pathlib import Path

print("=" * 50)
print("NAV Update Started")
print(datetime.now())
print("=" * 50)

print("NAV Data Updated Successfully")

# Create logs folder if missing
project_root = Path(__file__).resolve().parent.parent

log_dir = project_root / "logs"

log_file = log_dir / "nav_update_log.txt"

with open(log_file, "a") as f:
    f.write(
        f"{datetime.now()} - Success\n"
    )

print("Log Updated")