# Lê o feed público da playlist definida no data-playlist do index.html
# e grava o vídeo mais recente (sem Shorts) em ultimo-video.json.
# Roda no GitHub Actions; o site lê esse arquivo do próprio domínio,
# sem depender de proxy de CORS.
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SAIDA = RAIZ / 'ultimo-video.json'

html = (RAIZ / 'index.html').read_text(encoding='utf-8')
m = re.search(r'data-playlist="([^"]+)"', html)
if not m:
    sys.exit('data-playlist não encontrado no index.html')

feed = 'https://www.youtube.com/feeds/videos.xml?playlist_id=' + m.group(1)
req = urllib.request.Request(feed, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    raiz = ET.fromstring(r.read())

ns = {'a': 'http://www.w3.org/2005/Atom', 'yt': 'http://www.youtube.com/xml/schemas/2015'}
videos = []
for e in raiz.findall('a:entry', ns):
    link = e.find('a:link', ns)
    href = link.get('href', '') if link is not None else ''
    if '/shorts/' in href:
        continue
    videos.append({
        'id': e.findtext('yt:videoId', '', ns),
        'titulo': e.findtext('a:title', '', ns),
        'data': e.findtext('a:published', '', ns),
    })

videos = [v for v in videos if v['id']]
if not videos:
    sys.exit('feed sem vídeos')

# ISO 8601 com o mesmo fuso ordena certo como texto
novo = max(videos, key=lambda v: v['data'])
SAIDA.write_text(json.dumps(novo, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(novo['id'], novo['titulo'])
