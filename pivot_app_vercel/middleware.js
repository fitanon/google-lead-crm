const PASS = 'admin';
const COOKIE = 'crm_auth=tfc_ok_v2';

const LOGIN_HTML = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Lead CRM · The Fit Clinic</title>
<style>
:root{--bg:#0e1116;--panel:#161b22;--line:#242c37;--accent:#27c79e;--muted:#8b98a9;--text:#e8edf4;--rose:#f47174}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif}
.card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:36px 34px;width:min(92vw,380px)}
h1{margin:0 0 6px;font-size:19px;font-weight:800;letter-spacing:-.2px}
p{margin:0 0 22px;color:var(--muted);font-size:13.5px}
.logo{width:38px;height:38px;border-radius:10px;background:rgba(39,199,158,.12);border:1px solid rgba(39,199,158,.4);display:flex;align-items:center;justify-content:center;margin-bottom:16px}
input{width:100%;padding:12px 14px;border-radius:10px;border:1px solid var(--line);background:#0e1218;color:var(--text);font-size:15px;outline:none}
input:focus{border-color:var(--accent)}
button{width:100%;margin-top:12px;padding:12px;border-radius:10px;border:0;background:var(--accent);color:#06251c;font-size:14.5px;font-weight:800;cursor:pointer}
button:hover{filter:brightness(1.08)}
.err{color:var(--rose);font-size:13px;margin-top:10px;display:none}
</style></head><body>
<div class="card">
  <div class="logo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#27c79e" stroke-width="2"><rect x="3" y="11" width="18" height="2" rx="1"/><rect x="1" y="8" width="4" height="8" rx="1.2"/><rect x="19" y="8" width="4" height="8" rx="1.2"/></svg></div>
  <h1>Lead CRM · The Fit Clinic</h1>
  <p>This dashboard contains client data. Enter the password to continue.</p>
  <form id="f"><input id="pw" type="password" placeholder="Password" autofocus autocomplete="current-password">
  <button type="submit">Unlock</button>
  <div class="err" id="err">Wrong password — try again.</div></form>
</div>
<script>
document.getElementById('f').onsubmit=async e=>{
  e.preventDefault();
  const r=await fetch(location.pathname,{method:'POST',headers:{'x-crm-pass':document.getElementById('pw').value}});
  if(r.ok) location.reload();
  else{const el=document.getElementById('err');el.style.display='block';document.getElementById('pw').select();}
};
</script>
</body></html>`;

export const config = { matcher: '/(.*)' };

export default function middleware(req) {
  const cookie = req.headers.get('cookie') || '';
  if (cookie.includes(COOKIE)) return; // authenticated -> continue to static assets

  if (req.method === 'POST') {
    if (req.headers.get('x-crm-pass') === PASS) {
      return new Response('ok', {
        status: 200,
        headers: {
          'Set-Cookie': COOKIE + '; Path=/; Max-Age=2592000; HttpOnly; Secure; SameSite=Lax',
        },
      });
    }
    return new Response('unauthorized', { status: 401 });
  }

  return new Response(LOGIN_HTML, {
    status: 401,
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' },
  });
}
