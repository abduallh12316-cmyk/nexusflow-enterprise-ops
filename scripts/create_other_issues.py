#!/usr/bin/env python3
import csv, json, subprocess, sys, ast

REPO = "abduallh12316-cmyk/nexusflow-enterprise-ops"

PRIORITY_LABEL = {"Critical": "priority:critical", "Very High": "priority:critical",
                   "High": "priority:high", "Medium": "priority:medium", "Low": "priority:low"}

STATUS_LABEL = {
    "Open": "status:open", "Blocked": "status:blocked", "Pending Decision": "status:pending-decision",
    "Approved": "status:approved", "Rejected": "status:rejected", "Under Assessment": "status:under-assessment",
    "Pending Approval": "status:pending-approval", "Deferred": "status:deferred",
}

def gh_api_post_issue(fields):
    cmd = ["gh", "api", f"repos/{REPO}/issues", "-X", "POST",
           "-f", f"title={fields['title']}",
           "-f", f"body={fields['body']}"]
    for lbl in fields["labels"]:
        cmd += ["-f", f"labels[]={lbl}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR creating {fields['title']}: {result.stderr}", file=sys.stderr)
        return None
    return json.loads(result.stdout)

all_mapping = {}

# --- Defects (bug template) ---
def body_for_defect(row):
    try:
        steps = ast.literal_eval(row["reproduction_steps"])
        steps_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    except Exception:
        steps_md = row["reproduction_steps"]
    return (
        f"## Environment\nNexusFlow staging environment (simulated)\n\n"
        f"## Steps to reproduce\n{steps_md}\n\n"
        f"## Expected result\n{row['expected']}\n\n"
        f"## Actual result\n{row['actual']}\n\n"
        f"## Severity\n{row['severity']}\n\n"
        f"## Owner (fictional)\n{row['owner']}\n\n"
        f"## Workaround / next action\nStatus: {row['status']}.\n\n"
        f"_Source: data/defects.csv ({row['id']}). Fictional data for AI-agent testing._"
    )

with open("data/defects.csv", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
for row in rows:
    labels = ["type:bug", PRIORITY_LABEL.get(row["severity"], "priority:medium"),
               STATUS_LABEL.get(row["status"], "status:open")]
    title = f"[{row['id']}] {row['title']}"
    res = gh_api_post_issue(dict(title=title, body=body_for_defect(row), labels=labels))
    if res:
        all_mapping[row["id"]] = res["number"]
        print(f"Created {row['id']} -> issue #{res['number']}")

# --- Project Issues (generic template) ---
def body_for_issue(row):
    return (
        f"## Description\n{row['title']}\n\n"
        f"## Severity\n{row['severity']}\n\n"
        f"## Owner (fictional)\n{row['owner']}\n\n"
        f"## Impact\n{row['impact']}\n\n"
        f"## Next action\n{row['next_action']}\n\n"
        f"## Status\n{row['status']}\n\n"
        f"_Source: data/issues.csv ({row['id']}). Fictional data for AI-agent testing._"
    )

with open("data/issues.csv", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
for row in rows:
    labels = ["type:project-issue", PRIORITY_LABEL.get(row["severity"], "priority:medium"),
               STATUS_LABEL.get(row["status"], "status:open")]
    title = f"[{row['id']}] {row['title']}"
    res = gh_api_post_issue(dict(title=title, body=body_for_issue(row), labels=labels))
    if res:
        all_mapping[row["id"]] = res["number"]
        print(f"Created {row['id']} -> issue #{res['number']}")

# --- Change Requests (change_request template) ---
def body_for_cr(row):
    return (
        f"## Business rationale\nRequested by: {row['requestor']}\n\n"
        f"## Requested change\n{row['title']}\n\n"
        f"## Scope impact\n{row['impact']}\n\n"
        f"## Schedule impact\nSee notes below.\n\n"
        f"## Budget impact\nSee notes below.\n\n"
        f"## Risk / dependency impact\n{row['notes']}\n\n"
        f"## Recommendation\n{row['notes']}\n\n"
        f"## Decision owner\n(fictional) Change Control Board\n\n"
        f"## Decision and date\nStatus: {row['status']}"
        f"{' | Decided: ' + row['decision_date'] if row['decision_date'] else ' | Decision pending'}\n\n"
        f"_Source: data/change_requests.csv ({row['id']}). Fictional data for AI-agent testing._"
    )

with open("data/change_requests.csv", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
for row in rows:
    labels = ["type:change-request", PRIORITY_LABEL.get(row["impact"], "priority:medium"),
               STATUS_LABEL.get(row["status"], "status:open")]
    title = f"[{row['id']}] {row['title']}"
    res = gh_api_post_issue(dict(title=title, body=body_for_cr(row), labels=labels))
    if res:
        all_mapping[row["id"]] = res["number"]
        print(f"Created {row['id']} -> issue #{res['number']}")

# --- Risks (no dedicated template - generic risk body) ---
def body_for_risk(row):
    return (
        f"## Description\n{row['description']}\n\n"
        f"## Probability / Impact / Rating\n{row['probability']} / {row['impact']} / {row['rating']}\n\n"
        f"## Owner (fictional)\n{row['owner']}\n\n"
        f"## Mitigation\n{row['mitigation']}\n\n"
        f"## Status\n{row['status']}\n\n"
        f"## Review date\n{row['review_date']}\n\n"
        f"_Source: data/risks.csv ({row['id']}). Fictional data for AI-agent testing._"
    )

with open("data/risks.csv", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
for row in rows:
    labels = ["type:risk", PRIORITY_LABEL.get(row["rating"], "priority:medium"),
               STATUS_LABEL.get(row["status"], "status:open")]
    title = f"[{row['id']}] {row['description'][:60]}"
    res = gh_api_post_issue(dict(title=title, body=body_for_risk(row), labels=labels))
    if res:
        all_mapping[row["id"]] = res["number"]
        print(f"Created {row['id']} -> issue #{res['number']}")

with open("scripts/other_issue_map.json", "w") as f:
    json.dump(all_mapping, f, indent=2)
print(f"\nCreated {len(all_mapping)} issues (defects+issues+CRs+risks). Mapping saved to scripts/other_issue_map.json")
