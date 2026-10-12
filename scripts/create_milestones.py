#!/usr/bin/env python3
import csv, json, subprocess, sys

REPO = "abduallh12316-cmyk/nexusflow-enterprise-ops"

def gh_api_post(path, fields):
    cmd = ["gh", "api", f"repos/{REPO}/{path}", "-X", "POST"]
    for k, v in fields.items():
        cmd += ["-f", f"{k}={v}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR creating {fields.get('title')}: {result.stderr}", file=sys.stderr)
        return None
    return json.loads(result.stdout)

mapping = {}
with open("data/milestones.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = f"{row['id']}: {row['name']}"
        state = "closed" if row["status"] == "Completed" else "open"
        due_on = f"{row['date']}T23:59:59Z"
        description = f"Owner (fictional): {row['owner']} | Status: {row['status']}"
        res = gh_api_post("milestones", dict(title=title, state=state, due_on=due_on, description=description))
        if res:
            mapping[row["id"]] = res["number"]
            print(f"Created milestone {row['id']} -> #{res['number']} ({title})")

with open("scripts/milestone_map.json", "w") as f:
    json.dump(mapping, f, indent=2)
print("\nSaved mapping to scripts/milestone_map.json")
