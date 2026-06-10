
"""
Bluestock Mutual Fund Analytics Capstone

Master Pipeline Runner
Author: Bhimishetti Lohith
Purpose: Executes the main project scripts sequentially.
"""

import subprocess
import sys

print("=" * 60)
print("BLUESTOCK MF CAPSTONE PIPELINE")
print("=" * 60)

scripts = [
    "scripts/data_ingestion.py",
    "scripts/compute_metrics.py"
]

for script in scripts:

    print("\n" + "=" * 60)
    print(f"Running: {script}")
    print("=" * 60)

    try:

        subprocess.run(
            [sys.executable, script],
            check=True
        )

        print(f"Completed: {script}")

    except Exception as e:

        print(f"Error in {script}: {e}")

print("\n" + "=" * 60)
print("Pipeline Execution Completed Successfully")
print("=" * 60)

