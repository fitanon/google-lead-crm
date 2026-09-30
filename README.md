# Fit Clinic Lead CRM

Leads-first CRM + pivot explorer for the Official Client Questionnaire V2 (Google Sheet, tab "Yes").

## Structure
- `build_app.py` — generates the single-file app (`pivot_app/index.html`) with data embedded from `clean_data.json` (pivot) and `leads_full.json` (full lead responses).
- `pivot_app/index.html` — the built app (leads list, phase tabs, one-pager lead views, weekly summary, pivot explorer).

## Rebuild
```
python3 build_app.py
```

## Deployments
- question.pplx.app (Perplexity, org visibility)
- pivotapp.vercel.app (Vercel)

## Data refresh
Re-pull the sheet (`gws sheets spreadsheets values get`, range `Yes!A1:BZ`) into `leads_full.json` / `clean_data.json`, then rebuild.

## Public repository note

This public copy intentionally excludes generated lead data and the bundled HTML snapshot. Those files contain private contact and health information and must remain in the private source repository or a protected deployment environment.
