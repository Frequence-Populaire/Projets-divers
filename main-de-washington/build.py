import sys
src=sys.argv[1] if len(sys.argv)>1 else 'events2.json'
t=open('template.html').read()
t=t.replace('__MAP__',open('map.json').read()).replace('__RAW__',open(src).read()).replace('__PROJ__',open('proj.json').read())
open('../main-de-washington.html','w').write(t); print(len(t))
