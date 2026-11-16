import sys,time
P,N,B,R,Q,K=1,2,3,4,5,6
T='7AKKKKA7AKKKKKKAAKUZZUKAAKZ__ZKAAKZ__ZKAAKUZZUKAAKKKKKKA7AKKKKA77AFFFFA7AKPPPPKAAKPUUPKAAPPUUPPAAKUUUUKAAUUUUUUAAPKKKKPA7AFFFFA7FPPPPPPFPZZZZZZPPZ____ZPPZ____ZPPZ____ZPPZZZZZZPFPPPPPPFKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKPPKKKFKKKKKKFFKKKKKKFFKKKKKKFFKKKKKKFFKKKKKKFKKKKKKKAAAAAAA'
D=(-9,-11,9,11,-1,-10,1,10,-19,-21,-8,12,8,19,-12,21)
b=[0]*64;c=1
def E():
 v=sum(b[i]for i in range(64)if b[i])
 for i in range(64):
  x=b[i]
  if x:v+=(ord(T[64*(abs(x)-1)+i])-75)*(1 if x>0 else-1)
 return v*(1 if c>0 else-1)
def A(sq):return 0<=sq<64 and(sq%8 or 1)
def M():
 m=[];e=c;h=6 if e>0 else 1;r=4 if e>0 else 3;q=(4,3,2,5)
 for f in range(64):
  x=b[f]
  if x*e<=0:continue
  a=abs(x)
  if a==P:
   d=8*e;t=f-d
   if A(t)and b[t]==0:
    if f>>3==h:
     for p in q:m+=[(f,t,p)]
    else:m+=[(f,t,0)]
    if f>>3==r:
     t2=f-d-d
     if A(t2)and b[t2]==0:m+=[(f,t2,0)]
   for dd in(7*e,9*e):
    t=f-dd
    if A(t)and b[t]*e<0:
     if f>>3==h:
      for p in q:m+=[(f,t,p)]
     else:m+=[(f,t,0)]
  elif a==N:
   for d in D[8:]:
    t=f+d
    if A(t)and b[t]*e<=0:m+=[(f,t,0)]
  elif a in(B,R,Q):
   for i,d in enumerate(D[:8]):
    for j in range(1,8):
     t=f+d*j
     if not A(t):break
     if b[t]==0:m+=[(f,t,0)]
     elif b[t]*e<0:m+=[(f,t,0)];break
     else:break
     if a==B and i>3:break
     if a==R and i<4:break
  elif a==K:
   for d in D[:8]:
    t=f+d
    if A(t)and b[t]*e<=0:m+=[(f,t,0)]
 return m
def X():
 k=-6*c
 for i in range(64):
  if b[i]==k:ks=i;break
 for f in range(64):
  x=b[f]
  if not x or x*c>=0:continue
  a=abs(x)
  if a==P:
   for d in(7*c,9*c):
    t=f-d
    if A(t)and t==ks:return 1
  elif a==N:
   for d in D[8:]:
    if A(f+d)and f+d==ks:return 1
  elif a in(B,R,Q):
   for i,d in enumerate(D[:8]):
    for j in range(1,8):
     t=f+d*j
     if not A(t):break
     if t==ks:return 1
     if b[t]:break
     if a==B and i>3:break
     if a==R and i<4:break
  elif a==K:
   for d in D[:8]:
    if A(f+d)and f+d==ks:return 1
 return 0
def U(m):
 r=''
 for f,t,p in m:r+=chr(97+f%8)+chr(49+f//8)+chr(97+t%8)+chr(49+t//8)+('nbrq'[p-2]if p else'')
 return r
def G(a,bt,d):
 global c
 if d<1:return E()
 ms=M()
 if not ms:return-9999 if X()else 0
 ms.sort(key=lambda m:-max(1,abs(b[m[1]])))
 best=-99999
 for m in ms:
  f,t,p=m;nb=b[:];nb[t]=nb[f];nb[f]=0
  if p:nb[t]=p*c
  oc=c;c=-c;bs=b[:];b[:]=nb
  sc=-G(-bt,-a,d-1)
  b[:]=bs;c=oc
  if sc>best:best=sc
  if sc>a:a=sc
  if a>=bt:return a
 return best
def S(dm):
 global c
 st=time.time();rv='';ap=-99999
 for d in range(1,dm+1):
  ms=M()
  if not ms:return'bestmove (none)'
  bm=None
  for m in ms:
   f,t,p=m;nb=b[:];nb[t]=nb[f];nb[f]=0
   if p:nb[t]=p*c
   oc=c;c=-c;bs=b[:];b[:]=nb
   sc=-G(-99999,-ap,d-1)
   b[:]=bs;c=oc
   if sc>ap:ap=sc;bm=m
  if bm:rv=U([bm])
  if time.time()-st>2 or ap>9000:break
 return'bestmove '+rv if rv else'bestmove (none)'
Z='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
def F(fen):
 global b,c
 b=[0]*64
 rr=fen.split()[0].split('/')
 pt={80:P,78:N,66:B,82:R,81:Q,75:K}
 for i,row in enumerate(rr):
  j=0
  for ch in row:
   if'0'<=ch<='8':j+=ord(ch)-48
   else:sq=(7-i)*8+j;v=ord(ch);b[sq]=pt.get(v&95,6)*(1 if v&32==0 else-1);j+=1
 c=[-1,1][len(fen.split())<2 or fen.split()[1]=='w']
F(Z)
while 1:
 try:l=input()
 except:break
 if l=='uci':print('id name TinyChess\nid author hafizanpurnama-dev\nuciok')
 elif l[0]=='i':print('readyok')
 elif l[0]=='q':break
 elif l[0]=='p':
  a=l.split()
  if'startpos'in a:F(Z)
  else:fi=a.index('fen')+1;F(' '.join(a[fi:fi+6]))
  mi=a.index('moves')+1 if'moves'in a else len(a)
  for i in range(mi,len(a)):
   mv=a[i];f=(ord(mv[0])-97)+(int(mv[1])-1)*8;t=(ord(mv[2])-97)+(int(mv[3])-1)*8
   p=0
   if len(mv)>4:p={110:N,98:B,114:R,113:Q}.get(ord(mv[4]),0)
   b[t]=b[f];b[f]=0
   if p:b[t]=p*c
   c=-c
 elif l[0]=='g':
  a=l.split();dm=99
  if'depth'in a:dm=int(a[a.index('depth')+1])
  print(S(dm))