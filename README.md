<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="1oma1e — I build honest software. Desktop apps that show what they do, real-time web games, and a self-hosted homelab that runs it all." src="assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://github.com/1oma1e/Drivn/releases/latest"><img alt="Drivn" src="https://img.shields.io/badge/Drivn-v1.0.0-6366F1?style=for-the-badge&logo=windows11&logoColor=white"></a>
  <a href="https://github.com/1oma1e/Hyphn/releases/latest"><img alt="Hyphn" src="https://img.shields.io/github/v/release/1oma1e/Hyphn?style=for-the-badge&label=Hyphn&color=0EA5E9&logo=apple&logoColor=white"></a>
  <a href="https://tchinz.1oma1e.club"><img alt="Tchinz" src="https://img.shields.io/badge/Tchinz-play%20now-D946EF?style=for-the-badge&logo=nextdotjs&logoColor=white"></a>
  <a href="https://tchop.1oma1e.club"><img alt="tchop" src="https://img.shields.io/badge/tchop-live-F43F5E?style=for-the-badge&logo=fastapi&logoColor=white"></a>
  <img alt="Based in France" src="https://img.shields.io/badge/based%20in-France-0EA5E9?style=for-the-badge">
</p>

## 👋 About me

I'm a computer science student in France (BUT Informatique) who would rather ship than talk about shipping.
I like the layer where software meets the real world: **drivers, disks, phones, networks and the house I live in.**

- 🛡️ **Honest by default.** Free, no ads, no account, no telemetry. If my app does something, it tells you.
- 🏠 **Local-first.** Most of what I build runs on your machine or on my own home server, not someone's cloud.
- 📐 **Docs → mockup → code → tests.** Every project has its own decision log before it has a line of code.
- 🌐 **Network & virtualization nerd.** Docker, reverse proxies, VPNs and VMs are my comfort zone.

## ⭐ Featured

<a href="https://github.com/1oma1e/Drivn">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/drivn-dark.svg">
    <img alt="Drivn: your drivers and apps, up to date, from official sources only. Exact hardware match, signature and hash checks, restore point and one-click rollback." src="assets/drivn-light.svg" width="100%">
  </picture>
</a>

<p align="center">
  <a href="https://github.com/1oma1e/Drivn/releases/latest"><b>⬇ Download Drivn</b></a> ·
  <a href="https://github.com/1oma1e/Drivn"><b>Read how it works</b></a>
</p>

## 🧰 Things I build

<a href="#-things-i-build"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/safesweep-dark.svg"><img alt="SafeSweep — Windows disk analyzer that tells you what you can delete safely" src="assets/safesweep-light.svg" width="49%"></picture></a>
<a href="https://github.com/1oma1e/Hyphn"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/hyphn-dark.svg"><img alt="Hyphn — iPhone as a 4K60 webcam and file drop for Windows, 100% local" src="assets/hyphn-light.svg" width="49%"></picture></a>
<a href="https://tchinz.1oma1e.club"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tchinz-dark.svg"><img alt="Tchinz — real-time party games for 2 to 30 friends" src="assets/tchinz-light.svg" width="49%"></picture></a>
<a href="https://tchop.1oma1e.club"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/tchop-dark.svg"><img alt="tchop — TikTok and YouTube to MP4 or MP3" src="assets/tchop-light.svg" width="49%"></picture></a>
<a href="#-things-i-build"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/apphome-dark.svg"><img alt="AppHome Nexus — smart home dashboard over Home Assistant" src="assets/apphome-light.svg" width="49%"></picture></a>
<a href="#-things-i-build"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/powkey-dark.svg"><img alt="Powkey — all-in-one Discord bot" src="assets/powkey-light.svg" width="49%"></picture></a>
<a href="#-things-i-build"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/stormisland-dark.svg"><img alt="Storm Island — co-op survival game on Roblox" src="assets/stormisland-light.svg" width="49%"></picture></a>
<a href="#-things-i-build"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/spotifymigrate-dark.svg"><img alt="Spotify Migrator — move a whole Spotify account to another" src="assets/spotifymigrate-light.svg" width="49%"></picture></a>

<sub>🎓 Also: <a href="https://github.com/Lecasly10/SAE_5"><b>Spot'It</b></a>, a team university project. Snap a car, a TensorFlow model recognizes it and adds it to your collection, Pokédex-style (Flutter · Node.js · MongoDB · Docker).</sub>

## 🏠 My homelab

Everything that is "live" above runs on a small Debian server at home, one `docker compose` per app, deployed with a single command that pushes, rebuilds and checks the site is up.

```mermaid
flowchart LR
    U(("🌍 Internet")) --> CF["☁️ Cloudflare<br/>DNS + proxy"]
    CF --> NPM
    subgraph HOME["🖥️ Debian 13 home server · Docker"]
        direction LR
        NPM["🔀 Nginx Proxy Manager<br/>TLS + routing"]
        NPM --> TZ["🎉 Tchinz<br/>Next.js + Colyseus"]
        NPM --> TC["🎬 tchop<br/>FastAPI + yt-dlp"]
        TZ --> LT["🌐 LibreTranslate"]
        AH["🏡 AppHome Nexus<br/>Svelte + Fastify"] --> HA["⚙️ Home Assistant"]
        PK["🤖 Powkey<br/>Node.js + PM2"]
    end
    VPN["🔐 WireGuard"] --> AH
    PH["📱 Family phones"] --> VPN
    DC["💬 Discord"] <--> PK
```

## 🛠️ Tech I use

<p align="center"><b>Languages</b><br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=rust,ts,python,swift,dart,lua,bash,powershell&theme=dark">
    <img alt="Rust, TypeScript, Python, Swift, Dart, Lua, Bash, PowerShell" src="https://skillicons.dev/icons?i=rust,ts,python,swift,dart,lua,bash,powershell&theme=light">
  </picture>
</p>

<p align="center"><b>Apps & frameworks</b><br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=tauri,react,nextjs,svelte,vite,tailwind,nodejs,fastapi,flutter,discordjs,tensorflow&theme=dark">
    <img alt="Tauri, React, Next.js, Svelte, Vite, Tailwind, Node.js, FastAPI, Flutter, discord.js, TensorFlow" src="https://skillicons.dev/icons?i=tauri,react,nextjs,svelte,vite,tailwind,nodejs,fastapi,flutter,discordjs,tensorflow&theme=light">
  </picture>
</p>

<p align="center"><b>Infra, data & tooling</b><br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=docker,nginx,cloudflare,debian,linux,githubactions,git,sqlite,mongodb,vitest&theme=dark">
    <img alt="Docker, Nginx, Cloudflare, Debian, Linux, GitHub Actions, Git, SQLite, MongoDB, Vitest" src="https://skillicons.dev/icons?i=docker,nginx,cloudflare,debian,linux,githubactions,git,sqlite,mongodb,vitest&theme=light">
  </picture>
</p>

<p align="center"><b>Design & notes</b><br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=figma,blender,obsidian&theme=dark">
    <img alt="Figma, Blender, Obsidian" src="https://skillicons.dev/icons?i=figma,blender,obsidian&theme=light">
  </picture>
</p>

## 📐 How I work

| Principle | In practice |
|---|---|
| 📓 **Docs first** | Each project is an Obsidian vault: vision, architecture, ADRs and a session log. Code that isn't documented isn't done. |
| 🎨 **Mockup before code** | Screens are designed and validated as clickable mockups before the first component is written. |
| 🔒 **Safe by design** | Server-authoritative game logic, unprivileged UIs with a separate elevated helper, signature and hash checks, strict input validation. |
| ✅ **Ship & verify** | Lint, types and tests gate every commit. One command deploys, then checks the live site actually answers. |

## 🔭 Right now

- 📱 Shipping **[Hyphn](https://github.com/1oma1e/Hyphn)**: an iPhone as a 4K60 Windows webcam over Wi-Fi or USB, with auto updates and an English/French UI.
- 🏝️ Rebuilding the interface of **Storm Island** and modelling its world in Blender.
- 🎲 Adding new party games to **Tchinz**. [Come play](https://tchinz.1oma1e.club) with your friends.

<br>

<p align="center">
  <a href="https://tchinz.1oma1e.club"><img alt="Website" src="https://img.shields.io/badge/1oma1e.club-website-111827?style=flat-square&logo=googlechrome&logoColor=white"></a>
  <a href="https://github.com/1oma1e?tab=repositories"><img alt="Repositories" src="https://img.shields.io/badge/all-repositories-111827?style=flat-square&logo=github&logoColor=white"></a>
</p>

<p align="center"><sub>Made in France 🇫🇷 · Built with care, shipped with docs.</sub></p>
