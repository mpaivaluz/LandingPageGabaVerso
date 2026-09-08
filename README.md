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
| Canal (ID) | `UCOUBY6WToeg7yZuasla_uqA` |
| Vídeo reserva | ID `b5lHGqSEki0` |

## O que ainda falta

Está marcado com `<!-- TROQUE ... -->` no `index.html`:

| Onde | O quê |
|---|---|
| `assets/avatar.png` | Sua foto de perfil (quadrada, ex. 400x400). Sem ela aparece um "G" no lugar. |
| E-mail | `contato@gabaverso.com` → seu e-mail de parcerias. |
| Seção "Sobre mim" | Textos, números das estatísticas e as tags de gênero. |

## Último vídeo (automático)

A seção do vídeo **se atualiza sozinha**: um script lê o feed RSS público da aba **Vídeos**
do canal e coloca o vídeo mais recente na capa. Você posta no YouTube e a página acompanha —
sem mexer em nada.

O feed usado é o da playlist `UULFOUBY6WToeg7yZuasla_uqA`, que é a aba Vídeos — **lives e
Shorts ficam de fora**. O ID sai do ID do canal trocando o prefixo `UC` por:

| Prefixo | Aba do canal |
|---|---|
| `UULF` | Vídeos (em uso) |
| `UUSH` | Shorts |
| `UULV` | Ao vivo |
| `UU` | tudo junto |

Pra mudar, é só trocar o prefixo no `data-playlist` do `<div class="video-embed">`.

Detalhes de como funciona:

- **Sem chave de API.** O feed é público e não tem cota pra estourar.
- **Passa por um leitor de RSS** (`rss2json`, com `allorigins` de reserva) porque o YouTube
  não libera esse feed direto pro navegador (bloqueio de CORS). São serviços gratuitos e
  de terceiros — se um sair do ar, entra o outro.
- **Se os dois falharem**, fica o vídeo reserva do `data-id` e a página segue normal.
- **Cache de 30 minutos** no navegador do visitante: quem volta vê a capa na hora, sem
  nova consulta.
- **O player só carrega ao clicar**, então nada disso pesa na abertura da página.

Se algum dia quiser fixar um vídeo específico em vez do mais recente, remova o
atributo `data-playlist` do `<div class="video-embed">` e deixe só o `data-id` com o vídeo
escolhido.

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
