#!/usr/bin/env python3
import csv, json, subprocess, sys

REPO = "abduallh12316-cmyk/nexusflow-enterprise-ops"

PRIORITY_LABEL = {"Critical": "priority:critical", "High": "priority:high",
                   "Medium": "priority:medium", "Low": "priority:low"}

STATUS_LABEL = {
    "Done": "status:done", "In Progress": "status:in-progress", "Blocked": "status:blocked",
    "Not Started": "status:not-started", "At Risk": "status:at-risk", "Overdue": "status:overdue",
    "Pending Approval": "status:pending-approval",
}

def gh_api_post_issue(fields):
    cmd = ["gh", "api", f"repos/{REPO}/issues", "-X", "POST",
           "-f", f"title={fields['title']}",
           "-f", f"body={fields['body']}"]
    for lbl in fields["labels"]:
        cmd += ["-f", f"labels[]={lbl}"]
    if fields.get("milestone"):
        cmd += ["-F", f"milestone={fields['milestone']}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR creating {fields['title']}: {result.stderr}", file=sys.stderr)
        return None
    return json.loads(result.stdout)

def body_for_task(row):
    dep = row["depends_on"].strip()
    dep_line = f"Depends on: {dep}" if dep else "None"
    return (
        f"## Objective\n{row['title']} (workstream: {row['workstream']})\n\n"
        f"## Owner (fictional)\n{row['owner']}\n\n"
        f"## Priority / Due date\n{row['priority']} / {row['due_date']}\n\n"
        f"## Dependencies\n{dep_line}\n\n"
        f"## Acceptance criteria\n"
        f"- [ ] Deliverable for \"{row['title']}\" is complete and matches the Product Backlog / Technical Scope description\n"
        f"- [ ] Owner has verified the result and updated status to Done\n\n"
        f"## Evidence / updates\n"
        f"Progress as of 2026-10-12: {row['progress_percent']}% complete. Status: {row['status']}.\n\n"
        f"_Source: data/tasks.csv ({row['id']}). Fictional data for AI-agent testing._"
    )

mapping = {}
with open("data/tasks.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    labels = ["type:task", PRIORITY_LABEL.get(row["priority"], "priority:medium"),
               STATUS_LABEL.get(row["status"], "status:open")]
    title = f"[{row['id']}] {row['title']}"
    res = gh_api_post_issue(dict(title=title, body=body_for_task(row), labels=labels))
    if res:
        mapping[row["id"]] = res["number"]
        print(f"Created {row['id']} -> issue #{res['number']}")

with open("scripts/task_issue_map.json", "w") as f:
    json.dump(mapping, f, indent=2)
print(f"\nCreated {len(mapping)} task issues. Mapping saved to scripts/task_issue_map.json")
