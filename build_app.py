import json, os

full = json.load(open('/home/user/workspace/leads_full.json'))

SHEET_ID = '1tucDUTMp9faTFDD7lGi4pV81FeowO3JHPRwZPNXYCFs'
GID = '305386884'

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Lead CRM · The Fit Clinic</title>
<style>
:root{
  --bg:#0e1116; --panel:#161b22; --panel2:#1c232d; --panel3:#212a35;
  --line:#283340; --line2:#323e4d;
  --text:#eef3f8; --muted:#94a2b3; --faint:#64727f;
  --accent:#27c79e; --accentInk:#06281f; --blue:#4b8dff; --warn:#f0b945;
  --violet:#a78bfa; --rose:#fb7185; --amber:#fbbf24; --cyan:#22d3ee;
  --shadow:0 8px 28px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--text);font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit}

/* header */
header{display:flex;align-items:center;justify-content:space-between;gap:10px;
  padding:0 20px;height:62px;border-bottom:1px solid var(--line);
  background:linear-gradient(180deg,#141b24,#0e1116);position:sticky;top:0;z-index:40}
.brand{display:flex;align-items:center;gap:11px;min-width:0;cursor:pointer}
.logo{width:33px;height:33px;border-radius:9px;background:linear-gradient(135deg,var(--accent),#1b9c7c);
  display:flex;align-items:center;justify-content:center;color:var(--accentInk);font-weight:800;flex:0 0 auto}
.brand h1{margin:0;font-size:15.5px;font-weight:700;white-space:nowrap}
nav{display:flex;align-items:center;gap:4px;margin-left:8px}
nav .tab{padding:8px 14px;border-radius:9px;color:var(--muted);font-size:13.5px;font-weight:600;
  cursor:pointer;border:1px solid transparent;background:transparent;white-space:nowrap;font-family:inherit}
nav .tab:hover{color:#fff;background:var(--panel2)}
nav .tab.on{color:var(--accent);background:rgba(39,199,158,.09);border-color:rgba(39,199,158,.25)}
nav .tab .xtra{font-size:9.5px;color:var(--faint);font-weight:700;letter-spacing:.5px;margin-left:5px;
  border:1px solid var(--line2);border-radius:5px;padding:1px 4px;vertical-align:1px}
.hright{display:flex;align-items:center;gap:8px}
.hbtn{display:inline-flex;align-items:center;gap:7px;padding:8px 12px;border-radius:9px;cursor:pointer;
  border:1px solid var(--line2);background:var(--panel2);color:var(--text);font-size:12.5px;font-weight:600;
  white-space:nowrap;text-decoration:none;font-family:inherit}
.hbtn:hover{border-color:var(--accent);color:#fff}
.hbtn svg{width:14px;height:14px;flex:0 0 auto}
.hbtn.green{border-color:rgba(39,199,158,.4);color:var(--accent)}
.hbtn.green:hover{background:rgba(39,199,158,.08)}

/* leads view */
.container{max-width:1160px;margin:0 auto;padding:24px 24px 60px}
.pagehead{display:flex;align-items:flex-end;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:18px}
.pagehead h2{margin:0;font-size:21px;font-weight:800;letter-spacing:-.2px}
.pagehead .sub{color:var(--muted);font-size:13px;margin-top:3px}
.syncrow{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:-6px 0 16px}
.syncbtn{display:inline-flex;align-items:center;gap:8px;padding:9px 16px;border-radius:9px;cursor:pointer;
  border:1px solid rgba(39,199,158,.45);background:rgba(39,199,158,.09);color:var(--accent);
  font-size:13px;font-weight:700;font-family:inherit}
.syncbtn:hover{background:rgba(39,199,158,.16)}
.syncbtn:disabled{opacity:.6;cursor:wait}
.syncbtn svg{width:15px;height:15px}
.syncbtn.spin svg{animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.syncstat{color:var(--muted);font-size:12.5px}
.syncstat .ok{color:var(--accent);font-weight:600}
.syncstat .err{color:var(--rose);font-weight:600}
.statgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:13px;margin-bottom:20px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:14px 17px;position:relative;overflow:hidden}
.stat:before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--c,var(--accent))}
.stat .n{font-size:24px;font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.stat .l{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.6px;margin-top:2px;font-weight:600}
.stat .d{font-size:11.5px;color:var(--faint);margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.chips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}
.chip{display:inline-flex;align-items:center;gap:7px;padding:8px 14px;border-radius:20px;cursor:pointer;
  border:1px solid var(--line2);background:var(--panel2);color:var(--muted);font-size:12.5px;font-weight:600;font-family:inherit}
.chip:hover{color:#fff;border-color:var(--faint)}
.chip.on{color:#fff;border-color:var(--c,var(--accent));background:color-mix(in srgb,var(--c,var(--accent)) 13%,transparent)}
.chip .dot{width:8px;height:8px;border-radius:50%;background:var(--c,var(--accent))}
.chip .num{font-size:11px;color:var(--faint);font-weight:700}
.chip.on .num{color:inherit}

.leadcard{background:var(--panel);border:1px solid var(--line);border-radius:13px;overflow:hidden}
.leadbar{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.leadbar .t{font-size:13.5px;font-weight:700}
.leadbar .pill{font-size:11px;color:var(--muted);background:var(--panel2);border:1px solid var(--line2);border-radius:20px;padding:3px 10px;font-weight:600}
.leadbar .right{margin-left:auto;display:flex;gap:8px;align-items:center}
.search{background:var(--panel2);border:1px solid var(--line2);border-radius:9px;padding:8px 12px;color:var(--text);
  font-size:13px;font-family:inherit;width:200px}
.search:focus{outline:none;border-color:var(--accent)}
table.leads{border-collapse:collapse;width:100%}
table.leads th,table.leads td{padding:11px 16px;text-align:left;border-bottom:1px solid var(--line);font-size:13px}
table.leads thead th{background:var(--panel2);color:#c7d2de;font-size:11.5px;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
table.leads tbody tr{cursor:pointer}
table.leads tbody tr:hover td{background:#19212b}
table.leads tr.hot td{background:rgba(240,185,69,.045)}
table.leads tr.hot td:first-child{box-shadow:inset 3px 0 0 var(--warn)}
table.leads tr.hot:hover td{background:rgba(240,185,69,.09)}
.lname{font-weight:700;color:#fff}
.ldate{color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
.lsrc{color:var(--muted);max-width:220px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.badge{display:inline-flex;align-items:center;gap:6px;padding:3px 10px;border-radius:20px;font-size:11.5px;font-weight:700;white-space:nowrap}
.badge .bd{width:7px;height:7px;border-radius:50%}
.b-un{background:rgba(240,185,69,.12);color:var(--amber)} .b-un .bd{background:var(--amber)}
.b-ct{background:rgba(75,141,255,.13);color:#8ab4ff} .b-ct .bd{background:var(--blue)}
.b-sold{background:rgba(39,199,158,.13);color:var(--accent)} .b-sold .bd{background:var(--accent)}
.b-lost{background:rgba(251,113,133,.12);color:var(--rose)} .b-lost .bd{background:var(--rose)}
.viewall{display:flex;justify-content:center;padding:14px}
.viewall button{padding:10px 22px;border-radius:9px;border:1px solid var(--line2);background:var(--panel2);
  color:var(--text);cursor:pointer;font-size:13px;font-weight:700;font-family:inherit}
.viewall button:hover{border-color:var(--accent);color:var(--accent)}

/* lead detail */
.backrow{display:flex;align-items:center;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.backbtn{display:inline-flex;align-items:center;gap:7px;padding:8px 14px;border-radius:9px;cursor:pointer;
  border:1px solid var(--line2);background:var(--panel2);color:var(--muted);font-size:13px;font-weight:600;font-family:inherit}
.backbtn:hover{color:#fff;border-color:var(--accent)}
.detailhead{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin-bottom:16px;
  display:flex;align-items:flex-start;justify-content:space-between;gap:16px;flex-wrap:wrap}
.detailhead h2{margin:0 0 4px;font-size:22px;font-weight:800}
.detailhead .meta{color:var(--muted);font-size:13px;display:flex;gap:14px;flex-wrap:wrap;margin-top:6px}
.detailhead .meta b{color:#dbe3ec}
.dsections{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px;align-items:start}
.dsec{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:16px 18px}
.dsec h3{margin:0 0 10px;font-size:12px;color:var(--accent);text-transform:uppercase;letter-spacing:.8px;font-weight:700}
.qa{padding:7px 0;border-bottom:1px solid var(--line)}
.qa:last-child{border-bottom:0}
.qa .q{font-size:11.5px;color:var(--faint);margin-bottom:2px;line-height:1.35}
.qa .a{font-size:13px;color:#e2e9f0;white-space:pre-wrap;word-break:break-word}
.prefgrid{display:grid;grid-template-columns:1fr auto;gap:2px 12px;font-size:12.5px}
.prefgrid .pk{color:var(--muted)} .prefgrid .pv{color:#e2e9f0;text-align:right;white-space:nowrap}
.prefblock{margin-bottom:12px}
.prefblock h4{margin:0 0 5px;font-size:12px;color:#c7d2de}

/* explorer (unchanged core) */
#view-explore{display:none}
.wrap{display:flex;align-items:stretch;min-height:calc(100vh - 62px)}
.sidebar{width:300px;flex:0 0 300px;border-right:1px solid var(--line);background:var(--panel);
  padding:18px 16px;height:calc(100vh - 62px);overflow-y:auto;position:sticky;top:62px}
.main{flex:1;padding:22px 26px;overflow-x:auto;min-width:0}
.ctl{margin-bottom:18px}
.ctlhead{display:flex;align-items:center;gap:7px;margin-bottom:7px}
.ctlhead .h{font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);font-weight:700}
.info{width:16px;height:16px;border-radius:50%;border:1px solid var(--line2);background:transparent;
  color:var(--faint);font-size:10px;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;
  justify-content:center;line-height:1;flex:0 0 auto;padding:0}
.info:hover{border-color:var(--accent);color:var(--accent)}
select{width:100%;padding:9px 11px;background:var(--panel2);color:var(--text);border:1px solid var(--line2);
  border-radius:9px;appearance:none;cursor:pointer;font-family:inherit;font-size:13px;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2394a2b3' stroke-width='2.5'><path d='M6 9l6 6 6-6'/></svg>");
  background-repeat:no-repeat;background-position:right 11px center}
select:focus{outline:none;border-color:var(--accent)}
.seg{display:flex;border:1px solid var(--line2);border-radius:9px;overflow:hidden;background:var(--panel2)}
.seg button{flex:1;border:0;background:transparent;color:var(--muted);padding:9px 4px;cursor:pointer;font-size:12.5px;font-weight:600;font-family:inherit}
.seg button:not(:last-child){border-right:1px solid var(--line2)}
.seg button.on{background:var(--accent);color:var(--accentInk);font-weight:700}
.filters details{border:1px solid var(--line2);border-radius:9px;margin-bottom:7px;background:var(--panel2);overflow:hidden}
.filters summary{cursor:pointer;padding:10px 12px;font-size:12.5px;font-weight:600;display:flex;
  justify-content:space-between;align-items:center;list-style:none;gap:8px}
.filters summary::-webkit-details-marker{display:none}
.filters summary:hover{background:var(--panel3)}
.filters summary .chev{margin-left:auto;color:var(--faint);transition:transform .15s;display:flex}
.filters details[open] summary .chev{transform:rotate(180deg)}
.filters summary .cnt{background:var(--accent);color:var(--accentInk);font-size:10px;font-weight:800;
  border-radius:10px;padding:1px 7px;min-width:18px;text-align:center;display:none}
.filters summary .cnt.show{display:inline-block}
.filters .opts{padding:5px 12px 11px;max-height:210px;overflow-y:auto;border-top:1px solid var(--line)}
.filters .opt{display:flex;gap:9px;align-items:flex-start;padding:4px 0;font-size:12.5px;color:#cbd5e1;cursor:pointer}
.filters .opt:hover{color:#fff}
.filters .opt input{margin-top:2px;accent-color:var(--accent)}
.btnrow{display:flex;gap:9px;margin-top:10px}
.btn{flex:1;padding:10px;border-radius:9px;border:1px solid var(--line2);background:var(--panel2);
  color:var(--text);cursor:pointer;font-size:13px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;gap:7px;font-family:inherit}
.btn:hover{border-color:var(--accent)}
.btn svg{width:15px;height:15px}
.btn.primary{background:var(--blue);border-color:var(--blue);color:#fff}
.btn.primary:hover{filter:brightness(1.08)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:13px;margin-bottom:20px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.kpi .n{font-size:24px;font-weight:800;color:var(--accent);font-variant-numeric:tabular-nums}
.kpi .l{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-top:3px;font-weight:600}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.cardbar{display:flex;align-items:center;gap:10px;padding:13px 16px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.cardbar .title{font-size:13.5px;font-weight:700}
.cardbar .pill{font-size:11px;color:var(--muted);background:var(--panel2);border:1px solid var(--line2);
  border-radius:20px;padding:3px 10px;font-weight:600}
.cardbar .hint{margin-left:auto;color:var(--faint);font-size:11.5px}
.tablescroll{overflow-x:auto}
table.pv{border-collapse:collapse;width:100%}
table.pv th,table.pv td{padding:10px 14px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
table.pv th:first-child,table.pv td:first-child{text-align:left;position:sticky;left:0;background:var(--panel);max-width:300px;overflow:hidden;text-overflow:ellipsis}
table.pv thead th{background:var(--panel2);color:#c7d2de;font-size:12px;font-weight:700;cursor:pointer;user-select:none;position:sticky;top:0}
table.pv thead th:first-child{background:var(--panel2)}
table.pv thead th .arrow{color:var(--accent);font-size:10px;margin-left:4px}
table.pv tbody tr:hover td{background:#19212b}
table.pv tbody tr:hover td:first-child{background:#202a36}
td.val{font-variant-numeric:tabular-nums}
td .pct{color:var(--muted);font-size:11px;margin-left:6px}
tr.totrow td{font-weight:800;background:#1a232e;border-top:2px solid var(--line2)}
tr.totrow td:first-child{background:#222d3a}
.bar{height:4px;background:var(--accent);border-radius:3px;margin-top:5px;opacity:.65;min-width:2px}
.empty{color:#3c4856}
.statusbar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;color:var(--muted);font-size:12px;margin-top:14px}
.statusbar .chipx{background:var(--panel2);border:1px solid var(--line2);border-radius:7px;padding:3px 9px}
.statusbar .multi{color:var(--warn);cursor:pointer;text-decoration:underline dotted;text-underline-offset:2px}

/* popover + modals */
.pop{position:fixed;z-index:50;max-width:280px;background:var(--panel3);border:1px solid var(--line2);
  border-radius:11px;padding:12px 14px;font-size:12.5px;color:#dbe3ec;box-shadow:var(--shadow);line-height:1.5}
.pop b{color:#fff}
.overlay{position:fixed;inset:0;background:rgba(6,9,13,.66);backdrop-filter:blur(3px);z-index:60;
  display:none;align-items:flex-start;justify-content:center;padding:40px 18px;overflow-y:auto}
.overlay.show{display:flex}
.modal{background:var(--panel);border:1px solid var(--line2);border-radius:16px;max-width:620px;width:100%;
  box-shadow:var(--shadow);animation:rise .18s ease}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.modal .mhead{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;border-bottom:1px solid var(--line)}
.modal .mhead h2{margin:0;font-size:16px}
.xbtn{width:30px;height:30px;border-radius:8px;border:1px solid var(--line2);background:var(--panel2);
  color:var(--muted);cursor:pointer;font-size:16px;line-height:1}
.xbtn:hover{color:#fff;border-color:var(--accent)}
.mbody{padding:6px 22px 20px}
.mbody section{padding:15px 0;border-bottom:1px solid var(--line)}
.mbody section:last-child{border-bottom:0}
.mbody h3{margin:0 0 6px;font-size:13px;color:var(--accent)}
.mbody p{margin:0;color:#c7d2de;font-size:13px}
.mbody .tag{display:inline-block;background:var(--panel2);border:1px solid var(--line2);border-radius:6px;
  padding:1px 7px;font-size:11.5px;color:#dbe3ec;margin:2px 3px 0 0}
.wsrow{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid var(--line);font-size:13px}
.wsrow:last-child{border-bottom:0}
.wsrow .k{color:#c7d2de}
.wsrow .v{font-weight:700;font-variant-numeric:tabular-nums}
.delta{font-size:11.5px;font-weight:700;border-radius:6px;padding:2px 7px;margin-left:8px}
.delta.up{background:rgba(39,199,158,.13);color:var(--accent)}
.delta.down{background:rgba(251,113,133,.12);color:var(--rose)}
.delta.flat{background:var(--panel2);color:var(--muted)}
.flagged{border:1px solid rgba(240,185,69,.4);background:rgba(240,185,69,.06);border-radius:10px;padding:10px 13px;margin-top:12px;font-size:12.5px;color:#f4d48a}

@media(max-width:860px){
  .wrap{flex-direction:column}
  .sidebar{width:100%;flex:none;height:auto;position:static;border-right:0;border-bottom:1px solid var(--line)}
  nav{margin-left:4px}
  nav .tab{padding:7px 9px;font-size:12.5px}
  nav .tab .xtra{display:none}
  header{padding:0 10px}
  .brand{flex:0 0 auto}
  .logo{width:29px;height:29px}
  .brand h1{display:none}
  .hright{gap:5px}
  .hbtn .hlbl{display:none}
  .hbtn{padding:8px 10px}
  .container{padding:16px 14px 50px}
  .lsrc{display:none}
  table.leads th:nth-child(3),table.leads td:nth-child(3){display:none}
}
</style>
</head>
<body>
<header>
  <div style="display:flex;align-items:center;min-width:0">
    <div class="brand" id="brandHome"><div class="logo">FC</div><h1>Lead CRM</h1></div>
    <nav>
      <button class="tab" data-nav="leads">Leads</button>
      <button class="tab" data-nav="explore">Pivot Explorer<span class="xtra">EXTRA</span></button>
    </nav>
  </div>
  <div class="hright">
    <button class="hbtn" id="weeklyBtn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
      <span class="hlbl">Weekly summary</span>
    </button>
    <a class="hbtn green" id="sheetLink" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3v5h5M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8z"/><path d="M9 13h6M9 17h6"/></svg>
      <span class="hlbl">Open Sheet</span>
    </a>
    <button class="hbtn" id="moreInfoBtn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 16v-4M12 8h.01"/></svg>
      <span class="hlbl">More info</span>
    </button>
  </div>
</header>

<!-- LEADS -->
<div id="view-leads">
  <div class="container">
    <div class="pagehead">
      <div>
        <h2>Leads</h2>
        <div class="sub">Newest first · click a lead to open their full questionnaire · <span style="color:var(--amber)">amber rows need contact</span></div>
      </div>
    </div>
    <div class="syncrow">
      <button class="syncbtn" id="syncBtn">
        <svg id="syncIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 11-2.64-6.36"/><path d="M21 3v6h-6"/></svg>
        Sync latest from Sheet
      </button>
      <span class="syncstat" id="syncStat"></span>
    </div>
    <div class="statgrid" id="homeStats"></div>
    <div class="chips" id="phaseChips"></div>
    <div class="leadcard">
      <div class="leadbar">
        <span class="t" id="listTitle"></span>
        <span class="pill" id="listCount"></span>
        <span class="right"><input class="search" id="searchBox" placeholder="Search name or source…"/></span>
      </div>
      <div style="overflow-x:auto">
        <table class="leads">
          <thead><tr><th>Name</th><th>Filled out</th><th>Source</th><th>Phase</th><th></th></tr></thead>
          <tbody id="leadRows"></tbody>
        </table>
      </div>
      <div class="viewall" id="viewAllWrap"><button id="viewAllBtn"></button></div>
    </div>
  </div>
</div>

<!-- LEAD DETAIL -->
<div id="view-lead" style="display:none"><div class="container" id="leadDetail"></div></div>

<!-- EXPLORER -->
<div id="view-explore">
  <div class="wrap">
    <aside class="sidebar">
      <div class="ctl">
        <div class="ctlhead"><span class="h">Rows · primary grouping</span><button class="info" data-info="rows">i</button></div>
        <select id="rowsDim"></select>
      </div>
      <div class="ctl">
        <div class="ctlhead"><span class="h">Columns · breakdown</span><button class="info" data-info="cols">i</button></div>
        <select id="colsDim"></select>
      </div>
      <div class="ctl">
        <div class="ctlhead"><span class="h">Metric</span><button class="info" data-info="metric">i</button></div>
        <div class="seg" id="metricSeg">
          <button data-m="count" class="on">Count</button>
          <button data-m="pct">% of total</button>
          <button data-m="both">Both</button>
        </div>
      </div>
      <div class="ctl filters">
        <div class="ctlhead"><span class="h">Filters</span><button class="info" data-info="filters">i</button></div>
        <div id="filterBox"></div>
      </div>
      <div class="btnrow">
        <button class="btn" id="resetBtn">Reset</button>
        <button class="btn primary" id="csvBtn">Export CSV</button>
      </div>
    </aside>
    <main class="main">
      <div class="kpis" id="kpis"></div>
      <div class="card">
        <div class="cardbar">
          <span class="title" id="cardTitle"></span>
          <span class="pill" id="cardMetric"></span>
          <span class="hint">Click a column header to sort</span>
        </div>
        <div class="tablescroll" id="tableWrap"></div>
      </div>
      <div class="statusbar" id="statusbar"></div>
    </main>
  </div>
</div>

<div class="pop" id="pop" style="display:none"></div>

<!-- more info modal -->
<div class="overlay" id="overlay">
  <div class="modal">
    <div class="mhead"><h2>About this CRM</h2><button class="xbtn" id="closeModal">&times;</button></div>
    <div class="mbody">
      <section><h3>The data</h3>
        <p><b id="modalCount"></b> leads from the Official Client Questionnaire V2, loaded directly from the Google Sheet (tab "Yes"). Each lead links back to its exact row in the sheet.</p></section>
      <section><h3>Phases</h3>
        <p><span class="tag">Uncontacted</span> no status recorded yet — these rows are highlighted amber. <span class="tag">Contacted</span> booked or rescheduled. <span class="tag">Consultation · Sold</span> consulted and bought a package. <span class="tag">Consultation · Lost</span> consulted but didn't buy.</p></section>
      <section><h3>Lead one-pagers</h3>
        <p>Click any lead name to see their full questionnaire — goals, health screening, nutrition, food preferences, training background, and internal notes — plus the date they filled it out.</p></section>
      <section><h3>Pivot explorer</h3>
        <p>The explorer tab is for aggregate analysis: group leads by any field, break them down by a second one, and export CSV. Multi-select fields can place one lead in several rows, so those counts may overlap; totals always count each lead once.</p></section>
      <section><h3>Weekly summary</h3>
        <p>The Weekly summary button compares the last 7 days to the 7 days before — new lead volume and cohort conversion — and flags any movement over 5%. An automated email version arrives every Monday morning.</p></section>
    </div>
  </div>
</div>

<!-- weekly summary modal -->
<div class="overlay" id="wsOverlay">
  <div class="modal">
    <div class="mhead"><h2>Weekly pipeline summary</h2><button class="xbtn" id="closeWs">&times;</button></div>
    <div class="mbody" id="wsBody"></div>
  </div>
</div>

<script>
let FULL = __FULL_DATA__;
const SHEET_URL = 'https://docs.google.com/spreadsheets/d/__SHEET_ID__/edit#gid=__GID__';
const SYNC_URL = '__SYNC_URL__';
const BUILT_AT = '__BUILT_AT__';
let DATA = [], LEADS = [], byRow = {};
document.getElementById('sheetLink').href = SHEET_URL;

/* ================= shared ================= */
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function parseD(s){
  if(!s) return null; s=String(s).trim();
  let m=s.match(/^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2}):(\d{2})/);
  if(m) return new Date(+m[1],+m[2]-1,+m[3],+m[4],+m[5],+m[6]);
  m=s.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})(?:\s+(\d{1,2}):(\d{2})(?::(\d{2}))?)?/);
  if(m) return new Date(+m[3],+m[1]-1,+m[2],+(m[4]||0),+(m[5]||0),+(m[6]||0));
  return null;
}
const MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
function fmtD(d){ return d? `${MONTHS[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}` : '—'; }

/* phases */
function phaseOf(l){
  const s=(l.status||'').toLowerCase();
  const a=Object.fromEntries(l.answers);
  const fu=(a[76]||'').toLowerCase(); // BY Follow Up
  if(/sold/.test(s)) return 'sold';
  if(/didn'?t buy|lost/.test(s)) return 'lost';
  if(s.trim()) return 'contacted';
  if(fu && fu!=='none') return 'contacted';
  return 'uncontacted';
}
const PHASES={
  all:{label:'All leads', c:'var(--accent)'},
  uncontacted:{label:'Uncontacted', c:'var(--amber)'},
  contacted:{label:'Contacted', c:'var(--blue)'},
  sold:{label:'Consultation · Sold', c:'var(--accent)'},
  lost:{label:'Consultation · Lost', c:'var(--rose)'},
};
const BADGE={uncontacted:['b-un','Uncontacted'],contacted:['b-ct','Contacted'],sold:['b-sold','Consult · Sold'],lost:['b-lost','Consult · Lost']};

function deriveAll(){
  LEADS = FULL.leads.map(l=>({
    ...l, d:parseD(l.date), phase:phaseOf(l),
    ref:(Object.fromEntries(l.answers)[8]||'').trim()
  })).sort((a,b)=>(b.d?b.d.getTime():0)-(a.d?a.d.getTime():0));
  byRow = {}; LEADS.forEach(l=>byRow[l.row]=l);
  DATA = FULL.leads.map(l=>{
    const a=Object.fromEntries(l.answers);
    return {ts:l.date, referral:a[8]||'', nutr_exp:a[23]||'', nutr_approach:a[25]||'',
      train_exp:a[68]||'', followup:a[71]||'', status:(l.status||'').trim()||'No status / uncontacted'};
  });
}
deriveAll();

/* ---- live sync from published sheet feed ---- */
function parseCSV(text){
  const rows=[];let row=[],cur='',q=false;
  for(let i=0;i<text.length;i++){
    const c=text[i];
    if(q){
      if(c==='"'){ if(text[i+1]==='"'){cur+='"';i++;} else q=false; }
      else cur+=c;
    } else {
      if(c==='"') q=true;
      else if(c===','){row.push(cur);cur='';}
      else if(c==='\n'){row.push(cur);rows.push(row);row=[];cur='';}
      else if(c==='\r'){/* skip */}
      else cur+=c;
    }
  }
  if(cur!==''||row.length){row.push(cur);rows.push(row);}
  return rows;
}
function buildFull(rows){
  const headers=rows[0];
  const leads=[];
  for(let ri=1;ri<rows.length;ri++){
    const row=rows[ri];
    const g=i=>((row[i]||'')+'').trim();
    if(!(g(2)||g(0)||g(8))) continue;
    const answers=[];
    for(let i=0;i<headers.length;i++){ if(i===73) continue; const v=g(i); if(v) answers.push([i,v]); }
    leads.push({row:ri+1,date:g(0),name:g(2),answers:answers,status:g(75)});
  }
  return {headers:headers,leads:leads};
}
async function syncNow(){
  const btn=document.getElementById('syncBtn'), st=document.getElementById('syncStat');
  if(!SYNC_URL||SYNC_URL.indexOf('http')!==0){ st.innerHTML='<span class="err">Sync feed not configured yet.</span>'; return; }
  btn.disabled=true; btn.classList.add('spin');
  st.textContent='Fetching latest from Google Sheets…';
  try{
    const res=await fetch(SYNC_URL+(SYNC_URL.includes('?')?'&':'?')+'_ts='+Date.now(),{cache:'no-store'});
    if(!res.ok) throw new Error('HTTP '+res.status);
    const text=await res.text();
    const rows=parseCSV(text);
    if(rows.length<2||rows[0].length<70) throw new Error('unexpected feed format');
    const prevN=FULL.leads.length;
    FULL=buildFull(rows);
    deriveAll();
    Object.keys(state.filters).forEach(d=>state.filters[d].clear());
    buildFilters();
    buildStats(); buildChips(); renderList(); render();
    const r=currentRoute(); if(r.startsWith('lead/')) renderLeadDetail(r.split('/')[1]);
    const diff=FULL.leads.length-prevN;
    const t=new Date().toLocaleTimeString([],{hour:'numeric',minute:'2-digit'});
    st.innerHTML=`<span class="ok">Synced at ${t}</span> · ${LEADS.length} leads${diff>0?` · <span class="ok">+${diff} new</span>`:(diff<0?` · ${diff}`:' · no new responses')}`;
  }catch(e){
    st.innerHTML=`<span class="err">Sync failed</span> — ${esc(e.message)}. Google refreshes the feed every few minutes; try again shortly.`;
  }
  btn.disabled=false; btn.classList.remove('spin');
}
if(SYNC_URL && SYNC_URL.indexOf('http')===0){
  document.getElementById('syncBtn').onclick=syncNow;
  document.getElementById('syncStat').textContent='Data snapshot: '+BUILT_AT+' · sync pulls the latest responses live';
}else{
  document.getElementById('syncBtn').style.display='none';
  document.getElementById('syncStat').innerHTML='<span class="ok">Data updated '+BUILT_AT+'</span> · refreshes automatically every morning';
}

/* ================= routing ================= */
function currentRoute(){
  const h=(location.hash||'#leads').slice(1);
  if(h.startsWith('lead/')) return h;
  if(h==='explore') return 'explore';
  return 'leads';
}
function navigate(r){ if(('#'+r)!==location.hash) location.hash=r; else showView(r); }
function showView(r){
  const isLead=r.startsWith('lead/');
  document.getElementById('view-leads').style.display = r==='leads'?'block':'none';
  document.getElementById('view-lead').style.display = isLead?'block':'none';
  document.getElementById('view-explore').style.display = r==='explore'?'block':'none';
  document.querySelectorAll('nav .tab').forEach(t=>t.classList.toggle('on', t.dataset.nav===(isLead?'leads':r)));
  if(isLead) renderLeadDetail(r.split('/')[1]);
  window.scrollTo(0,0);
}
window.addEventListener('hashchange',()=>showView(currentRoute()));
document.querySelectorAll('nav .tab').forEach(t=>t.onclick=()=>navigate(t.dataset.nav));
document.getElementById('brandHome').onclick=()=>navigate('leads');

/* ================= leads list ================= */
const listState={phase:'all', expanded:false, q:''};
const COLLAPSED_N=15;

function buildStats(){
  const total=LEADS.length;
  const sold=LEADS.filter(l=>l.phase==='sold').length;
  const unc=LEADS.filter(l=>l.phase==='uncontacted').length;
  const refc={};
  LEADS.forEach(l=>{ if(l.ref) refc[l.ref]=(refc[l.ref]||0)+1; });
  const top=Object.entries(refc).sort((a,b)=>b[1]-a[1])[0]||['—',0];
  const mc=document.getElementById('modalCount'); if(mc) mc.textContent=LEADS.length;
  document.getElementById('homeStats').innerHTML=`
    <div class="stat" style="--c:var(--accent)"><div class="n">${total}</div><div class="l">Total leads</div><div class="d">from Questionnaire V2</div></div>
    <div class="stat" style="--c:var(--blue)"><div class="n">${(sold/total*100).toFixed(1)}%</div><div class="l">Conversion rate</div><div class="d">${sold} sold</div></div>
    <div class="stat" style="--c:var(--violet)"><div class="n" title="${esc(top[0])}">${esc(top[0])}</div><div class="l">Top source</div><div class="d">${top[1]} leads (${(top[1]/total*100).toFixed(0)}%)</div></div>
    <div class="stat" style="--c:var(--amber)"><div class="n">${unc}</div><div class="l">Uncontacted</div><div class="d">need follow-up</div></div>`;
}
function buildChips(){
  const counts={all:LEADS.length};
  ['uncontacted','contacted','sold','lost'].forEach(p=>counts[p]=LEADS.filter(l=>l.phase===p).length);
  document.getElementById('phaseChips').innerHTML=Object.entries(PHASES).map(([k,v])=>
    `<button class="chip${listState.phase===k?' on':''}" style="--c:${v.c}" data-phase="${k}">
      <span class="dot"></span>${v.label}<span class="num">${counts[k]}</span></button>`).join('');
  document.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{
    listState.phase=c.dataset.phase; listState.expanded=false; buildChips(); renderList();
  });
}
function filteredLeads(){
  let arr=LEADS;
  if(listState.phase!=='all') arr=arr.filter(l=>l.phase===listState.phase);
  if(listState.q){
    const q=listState.q.toLowerCase();
    arr=arr.filter(l=>(l.name||'').toLowerCase().includes(q)||(l.ref||'').toLowerCase().includes(q));
  }
  return arr;
}
function renderList(){
  const arr=filteredLeads();
  const show=listState.expanded?arr:arr.slice(0,COLLAPSED_N);
  document.getElementById('listTitle').textContent=PHASES[listState.phase].label;
  document.getElementById('listCount').textContent=`${arr.length} lead${arr.length===1?'':'s'} · newest first`;
  document.getElementById('leadRows').innerHTML=show.map(l=>{
    const [bc,bl]=BADGE[l.phase];
    return `<tr class="${l.phase==='uncontacted'?'hot':''}" data-row="${l.row}">
      <td class="lname">${esc(l.name||'(no name)')}</td>
      <td class="ldate">${fmtD(l.d)}</td>
      <td class="lsrc" title="${esc(l.ref)}">${esc(l.ref||'—')}</td>
      <td><span class="badge ${bc}"><span class="bd"></span>${bl}</span></td>
      <td style="text-align:right;color:var(--faint)">›</td></tr>`;
  }).join('') || `<tr><td colspan="5" style="color:var(--faint);text-align:center;padding:26px">No leads match</td></tr>`;
  document.querySelectorAll('#leadRows tr[data-row]').forEach(tr=>tr.onclick=()=>navigate('lead/'+tr.dataset.row));
  const wrap=document.getElementById('viewAllWrap'), btn=document.getElementById('viewAllBtn');
  if(arr.length>COLLAPSED_N){
    wrap.style.display='flex';
    btn.textContent=listState.expanded?`Show recent ${COLLAPSED_N} only`:`View all ${arr.length} leads`;
    btn.onclick=()=>{listState.expanded=!listState.expanded;renderList();};
  } else wrap.style.display='none';
}
document.getElementById('searchBox').oninput=e=>{listState.q=e.target.value;listState.expanded=false;renderList();};

/* ================= lead detail ================= */
const H=FULL.headers;
const SECTIONS=[
  {t:'Contact & basics', idx:[1,3,4,5,6]},
  {t:'Goals', idx:[7]},
  {t:'How they found us', idx:[8]},
  {t:'Health screening', idx:[9,10,11,12,13,14,15,16,17,18]},
  {t:'Nutrition', idx:[19,20,21,22,23,24,25,26]},
  {t:'Meal plan requests', idx:[63,64,65]},
  {t:'Training', idx:[66,67,68,69,70]},
  {t:'Anything else', idx:[70.5]},
  {t:'Follow-up preference', idx:[71]},
  {t:'Internal (staff)', idx:[72,74,75,76,77]},
];
function shortQ(q){ return q.replace(/\s+/g,' ').trim(); }
function renderLeadDetail(row){
  const l=byRow[row];
  const el=document.getElementById('leadDetail');
  if(!l){ el.innerHTML='<div class="backrow"><button class="backbtn" onclick="history.back()">← Back</button></div><p style="color:var(--muted)">Lead not found.</p>'; return; }
  const a=Object.fromEntries(l.answers);
  const [bc,bl]=BADGE[l.phase];
  const rowUrl=`${SHEET_URL}&range=A${l.row}`;
  // preference groups (27-62)
  const prefGroups={};
  for(let i=27;i<=62;i++){
    if(a[i]===undefined) continue;
    const m=H[i].match(/^(.*?)\s*\[(.*)\]$/);
    if(!m) continue;
    (prefGroups[m[1]]=prefGroups[m[1]]||[]).push([m[2],a[i]]);
  }
  let prefHtml='';
  if(Object.keys(prefGroups).length){
    prefHtml=`<div class="dsec"><h3>Food preferences</h3>${Object.entries(prefGroups).map(([g,items])=>
      `<div class="prefblock"><h4>${esc(g)}</h4><div class="prefgrid">${items.map(([k,v])=>
        `<span class="pk">${esc(k)}</span><span class="pv">${esc(v)}</span>`).join('')}</div></div>`).join('')}</div>`;
  }
  const secHtml=SECTIONS.map(sec=>{
    const rows=sec.idx.filter(i=>Number.isInteger(i)&&a[i]!==undefined&&String(a[i]).trim()).map(i=>
      `<div class="qa"><div class="q">${esc(shortQ(H[i]))}</div><div class="a">${esc(a[i])}</div></div>`);
    // special: BS (69) anything else already in Training? keep simple
    if(!rows.length) return '';
    return `<div class="dsec"><h3>${sec.t}</h3>${rows.join('')}</div>`;
  }).join('');
  el.innerHTML=`
    <div class="backrow">
      <button class="backbtn" id="backBtn">← All leads</button>
      <a class="hbtn green" href="${rowUrl}" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><path d="M15 3h6v6M10 14L21 3"/></svg>
        Open row ${l.row} in Sheet</a>
    </div>
    <div class="detailhead">
      <div>
        <h2>${esc(l.name||'(no name)')}</h2>
        <div class="meta">
          <span>Filled out: <b>${fmtD(l.d)}</b></span>
          ${a[8]?`<span>Source: <b>${esc(a[8])}</b></span>`:''}
          ${a[72]?`<span>Score: <b>${esc(a[72])}</b></span>`:''}
        </div>
      </div>
      <span class="badge ${bc}" style="font-size:13px;padding:6px 14px"><span class="bd"></span>${bl}</span>
    </div>
    <div class="dsections">${secHtml}${prefHtml}</div>`;
  document.getElementById('backBtn').onclick=()=>navigate('leads');
}

/* ================= weekly summary ================= */
function weeklySummary(){
  const now=new Date();
  const wk=7*24*3600*1000;
  const w1s=new Date(now.getTime()-wk), w0s=new Date(now.getTime()-2*wk);
  const inW=(l,s,e)=>l.d&&l.d>=s&&l.d<e;
  const cur=LEADS.filter(l=>inW(l,w1s,now)), prev=LEADS.filter(l=>inW(l,w0s,w1s));
  const curSold=cur.filter(l=>l.phase==='sold').length, prevSold=prev.filter(l=>l.phase==='sold').length;
  const curCR=cur.length?curSold/cur.length*100:0, prevCR=prev.length?prevSold/prev.length*100:0;
  const total=LEADS.length, sold=LEADS.filter(l=>l.phase==='sold').length, unc=LEADS.filter(l=>l.phase==='uncontacted').length;
  const refc={}; LEADS.forEach(l=>{if(l.ref)refc[l.ref]=(refc[l.ref]||0)+1;});
  const top=Object.entries(refc).sort((a,b)=>b[1]-a[1])[0]||['—',0];
  function delta(c,p,unit){
    if(!p&&!c) return {h:'<span class="delta flat">no data</span>',flag:false};
    if(!p) return {h:'<span class="delta up">new</span>',flag:c>0};
    const d=(c-p)/p*100;
    const cls=Math.abs(d)<0.05?'flat':(d>0?'up':'down');
    return {h:`<span class="delta ${cls}">${d>0?'+':''}${d.toFixed(1)}%</span>`,flag:Math.abs(d)>5};
  }
  const dl=delta(cur.length,prev.length), dc=delta(curCR,prevCR);
  const flags=[];
  if(dl.flag) flags.push(`Lead volume moved ${cur.length>=prev.length?'up':'down'} more than 5% week-over-week (${prev.length} → ${cur.length}).`);
  if(dc.flag) flags.push(`Cohort conversion rate moved more than 5% week-over-week (${prevCR.toFixed(1)}% → ${curCR.toFixed(1)}%).`);
  document.getElementById('wsBody').innerHTML=`
    <section>
      <h3>This week vs last week</h3>
      <div class="wsrow"><span class="k">New leads (last 7 days)</span><span class="v">${cur.length}${dl.h}</span></div>
      <div class="wsrow"><span class="k">New leads (prior 7 days)</span><span class="v">${prev.length}</span></div>
      <div class="wsrow"><span class="k">Cohort conversion (last 7d)</span><span class="v">${curCR.toFixed(1)}%${dc.h}</span></div>
      <div class="wsrow"><span class="k">Cohort conversion (prior 7d)</span><span class="v">${prevCR.toFixed(1)}%</span></div>
      ${flags.length?`<div class="flagged">⚠ ${flags.join('<br>⚠ ')}</div>`:`<div style="color:var(--faint);font-size:12px;margin-top:10px">No movement greater than 5% — pipeline steady.</div>`}
    </section>
    <section>
      <h3>All-time core metrics</h3>
      <div class="wsrow"><span class="k">Total leads</span><span class="v">${total}</span></div>
      <div class="wsrow"><span class="k">Overall conversion rate</span><span class="v">${(sold/total*100).toFixed(1)}%</span></div>
      <div class="wsrow"><span class="k">Top source</span><span class="v">${esc(top[0])} (${top[1]})</span></div>
      <div class="wsrow"><span class="k">Uncontacted leads</span><span class="v">${unc}</span></div>
    </section>
    <section><p style="font-size:12px;color:var(--faint)">The automated email version of this summary is sent every Monday morning and logs metrics to the "Metrics Log" tab of the sheet for true week-over-week comparison.</p></section>`;
  document.getElementById('wsOverlay').classList.add('show');
}
document.getElementById('weeklyBtn').onclick=weeklySummary;
document.getElementById('closeWs').onclick=()=>document.getElementById('wsOverlay').classList.remove('show');
document.getElementById('wsOverlay').onclick=e=>{if(e.target.id==='wsOverlay')e.target.classList.remove('show');};

/* ================= pivot explorer (unchanged engine) ================= */
const DIMS = {
  referral:{label:'Referral Source', multi:false},
  train_exp:{label:'Training Experience', multi:true},
  nutr_exp:{label:'Nutrition Tracking Experience', multi:true},
  nutr_approach:{label:'Nutrition Approach (Service Path)', multi:false},
  followup:{label:'Preferred Follow-up', multi:false},
  status:{label:'Lead Status', multi:false},
};
const INFO = {
  rows:'<b>Primary grouping.</b> Each distinct value of this field becomes a row in the table.',
  cols:'<b>Secondary breakdown.</b> Splits each row by a second field. Choose “None” for a simple count per row.',
  metric:'<b>Count</b> = number of leads. <b>% of total</b> = each cell as a share of all leads in view. <b>Both</b> shows the count with its percentage beside it.',
  filters:'<b>Narrow the data.</b> Tick values to include them; a field left untouched includes everything.'
};
const state = {rows:'referral', cols:'none', metric:'count', filters:{}, sortCol:null, sortDir:-1};
Object.keys(DIMS).forEach(d=>state.filters[d]=new Set());
function vals(rec, dim){
  const raw = rec[dim] || '';
  if(DIMS[dim].multi){
    const parts = raw.split(',').map(s=>s.trim()).filter(Boolean);
    return [...new Set(parts.length?parts:['(blank)'])];
  }
  return [raw];
}
function distinct(dim){
  const s = new Set();
  DATA.forEach(r=>vals(r,dim).forEach(v=>s.add(v)));
  return [...s].sort((a,b)=>a.localeCompare(b));
}
function passFilters(rec){
  for(const dim of Object.keys(DIMS)){
    const f = state.filters[dim];
    if(f.size===0) continue;
    if(!vals(rec,dim).some(v=>f.has(v))) return false;
  }
  return true;
}
function buildPivot(){
  const recs = DATA.filter(passFilters);
  const grand = recs.length;
  const colDim = state.cols, rowDim = state.rows;
  const cellMap = {}, rowTot={}, colTot={};
  recs.forEach(rec=>{
    const rvs = vals(rec,rowDim);
    const cvs = colDim==='none' ? ['Total'] : vals(rec,colDim);
    rvs.forEach(rv=>{ rowTot[rv]=(rowTot[rv]||0)+1; });
    cvs.forEach(cv=>{ colTot[cv]=(colTot[cv]||0)+1; });
    rvs.forEach(rv=>cvs.forEach(cv=>{
      cellMap[rv]=cellMap[rv]||{}; cellMap[rv][cv]=(cellMap[rv][cv]||0)+1;
    }));
  });
  let rowKeys = Object.keys(rowTot);
  let colKeys = colDim==='none' ? ['Total'] : Object.keys(colTot).sort((a,b)=>colTot[b]-colTot[a]);
  if(state.sortCol && state.sortCol!=='__row__' && colKeys.includes(state.sortCol)){
    rowKeys.sort((a,b)=>((cellMap[b]?.[state.sortCol]||0)-(cellMap[a]?.[state.sortCol]||0))*(state.sortDir<0?1:-1));
  } else if(state.sortCol==='__row__'){
    rowKeys.sort((a,b)=>a.localeCompare(b)*(state.sortDir<0?-1:1));
  } else {
    rowKeys.sort((a,b)=>rowTot[b]-rowTot[a]);
  }
  return {recs,grand,cellMap,rowTot,colTot,rowKeys,colKeys,colDim,rowDim};
}
function fmt(v,total){
  if(state.metric==='count') return v?`${v}`:'<span class="empty">·</span>';
  if(state.metric==='pct') return v?`${(v/total*100).toFixed(1)}%`:'<span class="empty">·</span>';
  return v?`${v}<span class="pct">${(v/total*100).toFixed(0)}%</span>`:'<span class="empty">·</span>';
}
function arrowFor(c){ return state.sortCol===c ? `<span class="arrow">${state.sortDir<0?'▼':'▲'}</span>` : ''; }
function render(){
  const p = buildPivot();
  const conv = p.recs.filter(r=>/sold/i.test(r.status)).length;
  document.getElementById('kpis').innerHTML = `
    <div class="kpi"><div class="n">${p.grand}</div><div class="l">Leads in view</div></div>
    <div class="kpi"><div class="n">${p.rowKeys.length}</div><div class="l">${DIMS[p.rowDim].label} groups</div></div>
    <div class="kpi"><div class="n">${conv}</div><div class="l">Converted (sold)</div></div>
    <div class="kpi"><div class="n">${p.grand?((conv/p.grand)*100).toFixed(1):0}%</div><div class="l">Conversion rate</div></div>`;
  document.getElementById('cardTitle').textContent =
    p.colDim==='none' ? DIMS[p.rowDim].label : `${DIMS[p.rowDim].label} × ${DIMS[p.colDim].label}`;
  document.getElementById('cardMetric').textContent =
    state.metric==='count'?'Count':(state.metric==='pct'?'% of total':'Count + %');
  const maxRowTot = Math.max(1,...p.rowKeys.map(k=>p.rowTot[k]));
  let h='<table class="pv"><thead><tr>';
  h+=`<th data-c="__row__">${DIMS[p.rowDim].label}${arrowFor('__row__')}</th>`;
  if(p.colDim!=='none') p.colKeys.forEach(c=>h+=`<th data-c="${esc(c)}">${esc(c)}${arrowFor(c)}</th>`);
  h+=`<th data-c="__row__">Total${state.sortCol===null?'<span class="arrow">▼</span>':''}</th></tr></thead><tbody>`;
  p.rowKeys.forEach(rk=>{
    h+=`<tr><td title="${esc(rk)}">${esc(rk)}`;
    if(p.colDim==='none') h+=`<div class="bar" style="width:${(p.rowTot[rk]/maxRowTot*100).toFixed(0)}%"></div>`;
    h+='</td>';
    if(p.colDim!=='none') p.colKeys.forEach(ck=>{
      const v=p.cellMap[rk]?.[ck]||0; h+=`<td class="val">${fmt(v,p.grand)}</td>`;
    });
    h+=`<td class="val">${fmt(p.rowTot[rk],p.grand)}</td></tr>`;
  });
  h+=`<tr class="totrow"><td>Total</td>`;
  if(p.colDim!=='none') p.colKeys.forEach(ck=>h+=`<td class="val">${fmt(p.colTot[ck],p.grand)}</td>`);
  h+=`<td class="val">${state.metric==='count'?p.grand:(state.metric==='pct'?'100%':p.grand+'<span class=pct>100%</span>')}</td></tr>`;
  h+='</tbody></table>';
  document.getElementById('tableWrap').innerHTML=h;
  document.querySelectorAll('table.pv thead th').forEach(th=>th.onclick=()=>{
    const c=th.dataset.c; if(state.sortCol===c){state.sortDir*=-1;}else{state.sortCol=c;state.sortDir=-1;} render();
  });
  const multiActive = DIMS[p.rowDim].multi || (p.colDim!=='none'&&DIMS[p.colDim].multi);
  const act=Object.keys(DIMS).filter(d=>state.filters[d].size>0);
  let sb = `<span class="chipx">${p.grand} leads shown</span>`;
  sb += act.length ? `<span class="chipx">${act.length} filter${act.length>1?'s':''} active</span>` : `<span class="chipx">No filters</span>`;
  if(multiActive) sb += `<span class="multi" id="multiHint">Multi-select active — counts may overlap. Learn more</span>`;
  document.getElementById('statusbar').innerHTML = sb;
  const mh=document.getElementById('multiHint'); if(mh) mh.onclick=()=>openModal();
  window.__pivot=p;
}

/* popover */
const pop=document.getElementById('pop');
function showPop(btn){
  pop.innerHTML=INFO[btn.dataset.info]||'';
  pop.style.display='block';
  const r=btn.getBoundingClientRect();
  let left=r.left-6;
  pop.style.top=(r.bottom+10)+'px'; pop.style.left=left+'px';
  const pr=pop.getBoundingClientRect();
  if(pr.right>window.innerWidth-12){ left=window.innerWidth-12-pr.width; pop.style.left=left+'px'; }
}
function hidePop(){ pop.style.display='none'; }
document.querySelectorAll('.info').forEach(b=>{
  b.onclick=e=>{ e.stopPropagation(); if(pop.style.display==='block'&&pop.dataset.k===b.dataset.info){hidePop();return;} pop.dataset.k=b.dataset.info; showPop(b); };
});
document.addEventListener('click',e=>{ if(!pop.contains(e.target)&&!e.target.classList.contains('info')) hidePop(); });
window.addEventListener('resize',hidePop);
window.addEventListener('scroll',hidePop,true);

/* more info modal */
const overlay=document.getElementById('overlay');
function openModal(){ overlay.classList.add('show'); hidePop(); }
function closeModal(){ overlay.classList.remove('show'); }
document.getElementById('moreInfoBtn').onclick=openModal;
document.getElementById('closeModal').onclick=closeModal;
overlay.onclick=e=>{ if(e.target===overlay) closeModal(); };
document.addEventListener('keydown',e=>{ if(e.key==='Escape'){closeModal();document.getElementById('wsOverlay').classList.remove('show');} });

/* explorer controls */
function buildFilters(){
  const fb=document.getElementById('filterBox');
  fb.innerHTML='';
  Object.entries(DIMS).forEach(([k,v])=>{
    const opts=distinct(k);
    let inner=`<details><summary><span>${v.label}</span><span class="cnt" id="cnt_${k}"></span>`+
      `<span class="chev"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></span></summary><div class="opts">`;
    opts.forEach(o=>inner+=`<label class="opt"><input type="checkbox" data-dim="${k}" value="${esc(o)}"> <span>${esc(o)}</span></label>`);
    inner+='</div></details>';
    fb.insertAdjacentHTML('beforeend',inner);
  });
  fb.querySelectorAll('input[type=checkbox]').forEach(cb=>cb.onchange=()=>{
    const d=cb.dataset.dim;
    if(cb.checked) state.filters[d].add(cb.value); else state.filters[d].delete(cb.value);
    const c=document.getElementById('cnt_'+d); c.textContent=state.filters[d].size||''; c.classList.toggle('show',state.filters[d].size>0);
    render();
  });
}
function initControls(){
  const rs=document.getElementById('rowsDim'), cs=document.getElementById('colsDim');
  Object.entries(DIMS).forEach(([k,v])=>rs.insertAdjacentHTML('beforeend',`<option value="${k}">${v.label}</option>`));
  cs.insertAdjacentHTML('beforeend',`<option value="none">None (simple count)</option>`);
  Object.entries(DIMS).forEach(([k,v])=>cs.insertAdjacentHTML('beforeend',`<option value="${k}">${v.label}</option>`));
  rs.value=state.rows; cs.value=state.cols;
  rs.onchange=e=>{state.rows=e.target.value;state.sortCol=null;render();};
  cs.onchange=e=>{state.cols=e.target.value;state.sortCol=null;render();};
  document.querySelectorAll('#metricSeg button').forEach(b=>b.onclick=()=>{
    state.metric=b.dataset.m;
    document.querySelectorAll('#metricSeg button').forEach(x=>x.classList.toggle('on',x===b));
    render();
  });
  buildFilters();
  document.getElementById('resetBtn').onclick=()=>{
    Object.keys(DIMS).forEach(d=>{state.filters[d].clear();const c=document.getElementById('cnt_'+d);if(c){c.textContent='';c.classList.remove('show');}});
    document.getElementById('filterBox').querySelectorAll('input').forEach(i=>i.checked=false);
    render();
  };
  document.getElementById('csvBtn').onclick=exportCSV;
}
function exportCSV(){
  const p=window.__pivot; const cols=p.colDim==='none'?[]:p.colKeys;
  let lines=[[DIMS[p.rowDim].label,...cols,'Total'].map(csvq).join(',')];
  p.rowKeys.forEach(rk=>{
    const row=[rk]; cols.forEach(ck=>row.push(p.cellMap[rk]?.[ck]||0)); row.push(p.rowTot[rk]);
    lines.push(row.map(csvq).join(','));
  });
  const totrow=['Total']; cols.forEach(ck=>totrow.push(p.colTot[ck]||0)); totrow.push(p.grand);
  lines.push(totrow.map(csvq).join(','));
  const blob=new Blob([lines.join('\n')],{type:'text/csv'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download=`pivot_${p.rowDim}_by_${p.colDim}.csv`;a.click();
}
function csvq(v){v=String(v);return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v;}

/* init */
initControls();
buildStats();
buildChips();
renderList();
render();
showView(currentRoute());
</script>
</body>
</html>'''

import datetime
from zoneinfo import ZoneInfo
SYNC_URL = ''
try:
    SYNC_URL = open('/home/user/workspace/sync_url.txt').read().strip()
except FileNotFoundError:
    pass
html = html.replace('__FULL_DATA__', json.dumps(full, ensure_ascii=False))
html = html.replace('__SHEET_ID__', SHEET_ID).replace('__GID__', GID)
html = html.replace('__SYNC_URL__', SYNC_URL)
html = html.replace('__BUILT_AT__', datetime.datetime.now(ZoneInfo('America/Los_Angeles')).strftime('%b %-d, %Y'))
os.makedirs('/home/user/workspace/pivot_app', exist_ok=True)
open('/home/user/workspace/pivot_app/index.html','w').write(html)
os.makedirs('/home/user/workspace/pivot_app_vercel/public', exist_ok=True)
open('/home/user/workspace/pivot_app_vercel/public/index.html','w').write(html)
print('written', len(html), 'bytes (pivot_app + pivot_app_vercel/public)')
