# Assemble la page : gabarit + géométrie de la carte + base d'incidents -> index.html
# Usage : python3 scripts/build.py
import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
lire=lambda *p:open(os.path.join(R,*p),encoding='utf-8').read()
t=lire('template.html')
t=t.replace('__MAP__',lire('carte','map.json')).replace('__RAW__',lire('donnees','incidents.json')).replace('__PROJ__',lire('carte','proj.json'))
open(os.path.join(R,'index.html'),'w',encoding='utf-8').write(t)
print('index.html :',len(t)//1024,'Ko')
