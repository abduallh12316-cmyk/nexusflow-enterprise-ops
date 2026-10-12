#!/usr/bin/env python3
import csv, json, re, subprocess, sys

REPO = "abduallh12316-cmyk/nexusflow-enterprise-ops"
ID_PATTERN = re.compile(r"\b(TASK-\d+|DEF-\d+|ISS-\d+|CR-\d+|RISK-\d+|MS-\d+)\b")

with open("scripts/task_issue_map.json") as f:
    combined = json.load(f)
with open("scripts/other_issue_map.json") as f:
    combined.update(json.load(f))

def row_text(row):
    return " | ".join(str(v) for v in row.values())

def load_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

all_rows = {}
for path in ["data/tasks.csv", "data/defects.csv", "data/issues.csv",
             "data/change_requests.csv", "data/risks.csv"]:
    for row in load_csv(path):
        all_rows[row["id"]] = row

def gh_api_get(path):
    result = subprocess.run(["gh", "api", f"repos/{REPO}/{path}"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR GET {path}: {result.stderr}", file=sys.stderr)
        return None
    return json.loads(result.stdout)

def gh_api_patch_body(issue_number, new_body):
    result = subprocess.run(
        ["gh", "api", f"repos/{REPO}/issues/{issue_number}", "-X", "PATCH", "-f", f"body={new_body}"],
        capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR PATCH #{issue_number}: {result.stderr}", file=sys.stderr)
        return False
    return True

updated = 0
for this_id, issue_num in combined.items():
    row = all_rows.get(this_id)
    if row is None:
        continue
    mentions = set(ID_PATTERN.findall(row_text(row)))
    mentions.discard(this_id)
    related_ids = [m for m in mentions if m in combined and combined[m] != issue_num]
    if not related_ids:
        continue
    current = gh_api_get(f"issues/{issue_num}")
    if current is None:
        continue
    body = current["body"] or ""
    if "## Related" in body:
        continue  # already linked, skip (idempotent re-run safety)
    links = "\n".join(f"- {rid} → #{combined[rid]}" for rid in sorted(related_ids))
    new_body = body + f"\n\n## Related\n{links}\n"
    if gh_api_patch_body(issue_num, new_body):
        print(f"Linked {this_id} (#{issue_num}) -> {related_ids}")
        updated += 1

print(f"\nUpdated {updated} issues with cross-references.")
