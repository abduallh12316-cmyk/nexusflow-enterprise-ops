# NexusFlow — Enterprise Operations Management Platform (Fictional Sandbox)

> **Simulation notice:** All people, emails, budgets, tasks, and events are fictional. Emails use `example.com`. This pack is a project-management simulation, not a deployed application.

## Purpose
A complete simulated technology project for testing AI Agent capabilities in PMO reporting, risk and issue analysis, stakeholder communication, and GitHub workflows.

## Current status (12 Oct 2026)
- Health: **AMBER**
- Completion: **32% actual vs 38% planned**
- Budget baseline: **SAR 480,000**
- Forecast at completion: **SAR 505,000** (SAR 25,000 over baseline)
- Priority concerns: architecture decision, security review, critical API authorization defect, overdue hosting estimate, KPI sign-off.

## Phases
1. Initiation & Discovery — 1–18 Sep 2026
2. Planning & Solution Design — 14 Sep–16 Oct 2026
3. Core Platform Development — 5 Oct–4 Dec 2026
4. Integration & Quality Assurance — 23 Nov 2026–22 Jan 2027
5. UAT, Training & Go-Live — 11 Jan–12 Feb 2027
6. Closure & Handover — 15–26 Feb 2027

## Structure
- `01_Project_Governance/` — charter, scope, stakeholders, RACI
- `02_Planning/` — WBS, schedule, budget, communications
- `03_Execution/` — backlog, technical scope, test strategy
- `04_Monitoring_Control/` — status report, KPI, risks, issues, changes, decisions
- `05_Closure/` — closure and handover template
- `06_Agent_Testing/` — 30 test scenarios
- `data/` — JSON master dataset and CSV extracts
- `email_templates/` — draft-only email templates
- `github_templates/` — issue and change-request templates

## Usage
1. Upload this ZIP to your Agent or push the folder contents to GitHub.
2. Tell the Agent to treat `data/project_master.json` as master source and use CSVs as extracts.
3. Ask it to generate reports from source data, cite IDs, and flag contradictions.
4. Email actions are draft-only/mock by default.

## Data rules
- Reporting date: 2026-10-12; dates use ISO `YYYY-MM-DD`; currency is SAR.
- All emails use `example.com`.
- If a CSV differs from the master JSON, flag the discrepancy.
- Deliberate test cases include schedule slippage, blocked critical defect, overdue hosting estimate, pending changes, and KPI sign-off delay.
