// Enregistre une vidéo 1920×1080 (30 i/s, H.264) d'une vue de la carte.
// Rendu image par image avec une horloge virtuelle : la vidéo est fluide quelle que soit la machine.
//
// Prérequis : Node.js, Playwright (avec Chromium) et ffmpeg (avec libx264).
// Usage, depuis le dossier main-de-washington/ :
//   node scripts/video.js <monde|europe|allies> <long|court> <secondes|0> <sortie.mp4> [légende]
//   (0 = durée automatique : un fait tous les 1/6 s, entre 60 et 240 s)
// Variables : FFMPEG (chemin de ffmpeg, par défaut « ffmpeg »), FONTS_CSS (feuille @font-face
// locale pour Syne et JetBrains Mono, si Google Fonts n'est pas joignable).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');

const [zone, per, dur, out, label] = process.argv.slice(2);
if (!out) { console.error('usage : node scripts/video.js <zone> <période> <secondes|0> <sortie.mp4> [légende]'); process.exit(1); }
const FPS = 30, HOLD = 5, FF = process.env.FFMPEG || 'ffmpeg';
const legende = label || ({ monde: 'MONDE', europe: 'EUROPE', allies: 'ALLIÉS' }[zone] + ' · ' + (per === 'long' ? '1900' : '2013') + ' → 2026');

(async () => {
  const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
  const tmp = path.join(os.tmpdir(), `mdw_${zone}_${per}_${process.pid}.html`);
  fs.writeFileSync(tmp, '<!doctype html><html><head><meta charset="utf-8"></head><body>' + html + '</body></html>');

  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1200 }, deviceScaleFactor: 1 });
  // horloge virtuelle : la page n'avance que lorsque __step() est appelé
  await p.addInitScript(lab => {
    let T = 0, cbs = []; window.__VIDEO = lab;
    performance.now = () => T;
    window.requestAnimationFrame = cb => { cbs.push(cb); return 1 };
    window.__step = ms => { T += ms; const c = cbs; cbs = []; c.forEach(f => f(T)) };
  }, legende);
  await p.goto('file://' + tmp);
  if (process.env.FONTS_CSS) await p.addStyleTag({ path: process.env.FONTS_CSS });
  await p.addStyleTag({ content: '#stage{width:1920px!important;max-width:none!important;margin:0!important} body{margin:0!important;padding:0!important}' });
  await p.evaluate(async ([z, pe]) => {
    await Promise.all(['800 120px Syne', '400 14px "JetBrains Mono"', '500 14px "JetBrains Mono"'].map(f => document.fonts.load(f).catch(() => {})));
    const click = (id, k) => { const x = [...document.getElementById(id).children].find(b => b.dataset.k === k); if (x && x.getAttribute('aria-pressed') !== 'true') x.click() };
    click('per', pe); click('zone', z);
  }, [zone, per]);
  await p.waitForTimeout(1500);

  // vitesse choisie pour que la lecture complète dure `dur` secondes
  const info = await p.evaluate(dur => {
    const M = window.__MDW;
    if (!dur) dur = Math.max(60, Math.min(240, Math.round(M.n() / 6)));
    let t = M.t0(), s = 0; const t1 = M.t1();
    while (t < t1) { t += M.rate(t) / 30; s += 1 / 30 }
    M.setSpeed(s / dur); window.__step(16);
    return { dur, faits: M.n() };
  }, +dur);
  console.log(zone, per, info);

  const ff = spawn(FF, ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '23', '-preset', 'slow', '-movflags', '+faststart', out],
    { stdio: ['pipe', 'ignore', 'inherit'] });
  const total = Math.round((info.dur + HOLD) * FPS);
  for (let i = 0; i < total; i++) {
    const d = await p.evaluate(() => { window.__step(1000 / 30); return document.getElementById('cv').toDataURL('image/jpeg', 0.92) });
    if (!ff.stdin.write(Buffer.from(d.split(',')[1], 'base64'))) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  await b.close(); fs.unlinkSync(tmp);
  console.log('écrit :', out);
})();
