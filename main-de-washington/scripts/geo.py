# Projette et simplifie les frontières de Natural Earth (paquet npm world-atlas, countries-50m.json).
# Usage : python3 scripts/geo.py chemin/vers/countries-50m.json
import json,math,sys,os
ICI=os.path.dirname(os.path.abspath(__file__));CARTE=os.path.join(ICI,'..','carte')
d=json.load(open(sys.argv[1]))
tf=d['transform'];sc,tr=tf['scale'],tf['translate']
arcs=[]
for a in d['arcs']:
    x=y=0;pts=[]
    for dx,dy in a:
        x+=dx;y+=dy;pts.append((x*sc[0]+tr[0],y*sc[1]+tr[1]))
    arcs.append(pts)
def arc(i):
    return arcs[i] if i>=0 else arcs[~i][::-1]
def ring(r):
    out=[]
    for i in r:
        p=arc(i); out.extend(p if not out else p[1:])
    return out
# Equal Earth
A1,A2,A3,A4=1.340264,-0.081106,0.000893,0.003796;M=math.sqrt(3)/2
LON0=11
def ee(lon,lat):
    l=((lon-LON0+180)%360-180)*math.pi/180; p=lat*math.pi/180
    th=math.asin(M*math.sin(p)); t2=th*th; t6=t2**3
    x=l*math.cos(th)/(M*(A1+3*A2*t2+t6*(7*A3+9*A4*t2)))
    y=th*(A1+A2*t2+t6*(A3+A4*t2))
    return x,y
PW=2400
X0,_=ee(-180+LON0+1e-9,0);X1,_=ee(180+LON0-1e-9,0)
K=PW/(X1-X0)
_,YT=ee(0,80);_,YB=ee(0,-58)
PH=round((YT-YB)*K)
def P(lon,lat):
    x,y=ee(lon,lat);return (x-X0)*K,(YT-y)*K
def dp(pts,eps):
    if len(pts)<3:return pts
    (x1,y1),(x2,y2)=pts[0],pts[-1];dx,dy=x2-x1,y2-y1;L=math.hypot(dx,dy) or 1e-9
    im,dm=0,0
    for i in range(1,len(pts)-1):
        x,y=pts[i];dd=abs(dy*(x-x1)-dx*(y-y1))/L
        if dd>dm:im,dm=i,dd
    if dm>eps:return dp(pts[:im+1],eps)[:-1]+dp(pts[im:],eps)
    return [pts[0],pts[-1]]
out=[]
for g in d['objects']['countries']['geometries']:
    n=g['properties']['name']
    if n=='Antarctica' or 'type' not in g or g['type'] is None:continue
    polys=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]
    rs=[];small=[]
    for poly in polys:
        r=ring(poly[0])
        # split rings crossing antimeridian of projection: drop segments jumping
        pr=[P(lo,la) for lo,la in r]
        seg=[[pr[0]]]
        for a,b in zip(pr,pr[1:]):
            if abs(a[0]-b[0])>PW/3: seg.append([b])
            else: seg[-1].append(b)
        for s in seg:
            if len(s)>3 and s[0]==s[-1]:
                far=max(range(len(s)),key=lambda i:(s[i][0]-s[0][0])**2+(s[i][1]-s[0][1])**2)
                s=dp(s[:far+1],0.9)[:-1]+dp(s[far:],0.9)
            else: s=dp(s,0.9)
            xs=[p[0] for p in s];ys=[p[1] for p in s]
            area=abs(sum(s[i][0]*s[i-1][1]-s[i-1][0]*s[i][1] for i in range(len(s))))/2
            if len(s)<3: continue
            if area<3 and len(polys)>1:
                small.append((area,s)); continue
            if max(ys)<0 or min(ys)>PH:continue
            rs.append([v for p in s for v in (round(p[0]),round(p[1]))])
    if not rs and small:
        s=max(small,key=lambda x:x[0])[1]; rs=[[v for p in s for v in (round(p[0]),round(p[1]))]]
    if rs: out.append({'n':n,'r':rs})
json.dump({'PW':PW,'PH':PH,'c':out},open(os.path.join(CARTE,'map.json'),'w'),separators=(',',':'))
open(os.path.join(CARTE,'countries.txt'),'w').write('\n'.join(sorted(c['n'] for c in out)))
print(PH,len(out),'pays')
# emit projection constants for JS
json.dump({'X0':X0,'YT':YT,'K':K,'LON0':LON0},open(os.path.join(CARTE,'proj.json'),'w'))
