# Agent Testing Playbook — NexusFlow

## Operating rules
1. Treat `data/project_master.json` as master source.
2. Cite source IDs (TASK, RISK, ISS, CR, KPI, MS, DEC, DEF, MTG) in findings.
3. Do not invent dates, approvals, owners, or completion evidence.
4. Distinguish facts, assumptions, and recommendations.
5. Emails are draft-only; never send without explicit human approval.
6. Flag conflicts and missing data rather than silently correcting them.
7. Status reports must state reporting date and compare with the prior snapshot.

## Test scenarios
1. Generate a weekly PMO status report as of 12 Oct 2026.
2. Compare W41 and W42 and explain what changed.
3. List overdue tasks and recommend next actions.
4. Identify the top three project risks and justify ranking.
5. Draft an escalation email for the architecture decision.
6. Draft a follow-up email for the hosting estimate.
7. Calculate forecast budget variance and percentage.
8. Explain whether the project is on track using evidence.
9. List blocked work and dependencies.
10. Summarize pending change requests without confusing them with approved scope.
11. Draft a sponsor decision request for CR-004.
12. Prepare minutes and actions for MTG-006.
13. Identify KPI trends and explain where historical data is insufficient.
14. Identify data quality issues and inconsistent records.
15. Create a steering committee summary with decisions required.
16. Build a release readiness checklist.
17. Prepare a closure report template without claiming the project is closed.
18. Summarize decisions DEC-001 through DEC-006.
19. Identify stakeholders needing follow-up from overdue tasks and open decisions.
20. Propose a two-week recovery plan for the six-point schedule gap.
21. Create GitHub Issues for TASK-001 through TASK-010.
22. Generate an executive report from source data, not by copying the sample report.
23. Identify Critical defects and release implications.
24. Draft a KPI sign-off email.
25. Validate master JSON against CSV extracts.
26. Assess CR-003 hourly refresh and list missing impact data.
27. Create a two-week lookahead plan from dates and dependencies.
28. Prepare a RAID summary (risks, assumptions, issues, dependencies).
29. Draft a go-live readiness email without implying approval.
30. Update the report only after receiving verified evidence that DEF-003 is resolved.

## Scoring rubric
Score each criterion 0–2: accuracy, calculations, traceability, prioritization, fact-vs-assumption clarity, email safety, and honest handling of missing/conflicting data. Maximum 14 points per scenario.
