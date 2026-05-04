import json
import os
from datetime import datetime, timezone

# Always write paths relative to the repo root, not the script location
repo_root = os.path.join(os.path.dirname(__file__), "..", "..")
output_path = os.path.join(repo_root, "dashboards", "data", "datetime_test.json")

os.makedirs(os.path.dirname(output_path), exist_ok=True)

payload = {
    "last_updated": datetime.now(timezone.utc).isoformat(),
    "label": "Dashboard last refreshed at"
}

with open(output_path, "w") as f:
    json.dump(payload, f, indent=2)

print(f"Written: {payload['last_updated']}")
