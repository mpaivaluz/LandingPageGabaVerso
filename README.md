# Gabaverso — Landing Page

Página de links (bio) do canal **Gabaverso**: canal de promoções no WhatsApp, redes sociais
(YouTube, Instagram, TikTok, Twitch) e uma seção "sobre mim".

HTML + CSS puro, sem build e sem dependências. É só abrir o `index.html` no navegador.

Paleta: **azul `#243FF8`** e **verde `#BDFF3C`** sobre fundo escuro.

```
index.html   -> conteúdo (textos e links)
styles.css   -> visual (cores, animações, responsivo)
assets/      -> coloque aqui o avatar.png
```

## Links já configurados

| Onde | Link |
|---|---|
| WhatsApp (promoções) | `https://whatsapp.com/channel/0029VbDIjBVKAwEiz6YQQa2A` |
| YouTube | `https://www.youtube.com/@gabaverso` |
| Instagram | `https://www.instagram.com/gaba_verso` |
| TikTok | `https://www.tiktok.com/@gabaverso` |
| Twitch | `https://www.twitch.tv/gabaversoo` |
| Vídeo em destaque | ID `b5lHGqSEki0` |

## O que ainda falta

Está marcado com `<!-- TROQUE ... -->` no `index.html`:

| Onde | O quê |
|---|---|
| `assets/avatar.png` | Sua foto de perfil (quadrada, ex. 400x400). Sem ela aparece um "G" no lugar. |
| E-mail | `contato@gabaverso.com` → seu e-mail de parcerias. |
| Seção "Sobre mim" | Textos, números das estatísticas e as tags de gênero. |

### Trocar o vídeo em destaque
Pegue o ID na URL do YouTube (o que vem depois de `watch?v=`) e troque em **três lugares**
do bloco `.video-embed`: no `data-id` e nos dois links da miniatura (`src` e `onerror`).

## Como colocar no ar (grátis)

**Opção 1 — Netlify Drop (mais rápido):** acesse <https://app.netlify.com/drop> e arraste a
pasta inteira. Sai um link na hora.

**Opção 2 — GitHub Pages:** suba os arquivos num repositório, depois
`Settings → Pages → Branch: main / root`. Fica em `seuusuario.github.io/repo`.

**Opção 3 — Vercel:** `Add New → Project → Import` a pasta/repo. Deploy automático.

Depois é só trocar o link do Linktree na bio do Instagram pelo endereço da página.

## Ajustes rápidos

- **Cores:** mudam todas de uma vez no topo do `styles.css`, em `--blue` e `--green`.
- **Nova rede social:** copie um bloco `<a class="social ...">` inteiro no `index.html` e
  troque o ícone (SVG), o texto e o link.
- **Tirar as animações:** remova a classe `reveal` das seções, ou deixe como está — quem usa
  "reduzir movimento" no sistema já recebe a página sem animação automaticamente.
