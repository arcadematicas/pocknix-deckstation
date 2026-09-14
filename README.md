# Pocknix DeckStation ARM

**Sistema de emulación portable para arquitectura ARM (aarch64) — integrado en Pocknix**

> ⚠️ **Este es el proyecto DeckStation ARM**. Existe una versión hermana para
> **x86_64** (DeckStation original, para PC / Steam Deck) que se gestionará en
> su propio repositorio (`pocknix-deckstation-x86_64` o similar) más adelante.
> No confundir: este repo es SOLO para ARM.

---

## ¿Qué es?

Pocknix DeckStation ARM es un sistema de emulación portable que transforma
cualquier dispositivo **ARM64** (AYN Odin 3, Raspberry Pi, tablets, etc.) en una
consola de emulación completa. Está inspirado en Steam Deck y DeckStation, pero
diseñado para funcionar en hardware ARM.

## Filosofía

- **Todo autocontenido**: Todo vive dentro de `/opt/deckstation/`
- **Nada en el sistema host**: No toca `/home/`, `/etc/` ni configs del usuario
- **Portable**: Mover el directorio funciona en otro dispositivo
- **Sin dependencias del sistema**: Se auto-descarga todo lo necesario
- **Modular**: Cada emulador es independiente

## Arquitecturas soportadas

| Arquitectura | Estado |
|---|---|
| **aarch64 (ARM64)** | ✅ Este repo — soportada |
| **armv7h (ARM32)** | ⚠️ Parcial (depende del emulador) |
| **x86_64** | ❌ NO — ver proyecto DeckStation x86_64 |

## Estructura del repo

```
pocknix-deckstation/            # ← SOLO ARM
├── README.md                   # Este archivo
├── .gitignore                  # Qué ignorar
├── PKGBUILD                    # Paquete Arch Linux ARM (aarch64/armv7h)
├── pocknix-deckstation.install # Hooks de instalación
├── scripts/
│   ├── deckstation-setup.sh    # Descarga emuladores ARM64
│   ├── deckstation-launcher.sh # Wrapper del sistema (portable, rutas relativas)
│   ├── deckstation-update.sh   # Actualizador
│   └── setup_arm64_apps.py     # Setup ARM64: busca AppImages aarch64 en PkgForge/GitHub
├── overlay/
│   └── usr/
│       └── bin/
│           └── deckstation     # Comando del sistema
├── configs/                    # Configs portable de emuladores ARM (ver configs/README.md)
│   ├── retroarch/              #   + autoconfig (610 configs de mandos)
│   ├── es-de/                  #   ES-DE: es_find_rules.xml, es_systems.xml, es_settings.xml
│   ├── duckstation/
│   ├── azahar/
│   ├── citron/
│   ├── dolphin/
│   ├── pcsx2/
│   ├── ppsspp/
│   ├── flycast/
│   ├── dosboxpure/
│   ├── rmg/
│   ├── zsnes/
│   ├── supermodel/
│   ├── antimicrox/
│   ├── vita3k/
│   └── es-de-home/             # Reservado para configs de ES-DE
└── docs/
    └── INSTALACION.md          # Guía completa
```

## Estructura en ejecución (`/opt/deckstation/`)

```
/opt/deckstation/
├── DeckStation.AppImage        # La AppImage principal (ES-DE)
├── DeckStation.sh              # Script de lanzamiento
├── Apps/                       # Emuladores descargados (ARM64)
├── saves/                      # Saves del usuario
├── logs/                       # Logs de ejecución
├── Media/                      # Assets multimedia
├── settings/                   # Configuraciones
├── scripts/                    # Scripts de gestión
└── configs/                    # Configs del sistema
```

## Cómo funciona

1. **Instalación**: El paquete Arch instala la estructura base
2. **Setup**: `deckstation-setup` descarga los emuladores ARM64 necesarios
3. **Uso**: `deckstation` lanza el sistema completo
4. **Actualización**: `deckstation-update` actualiza todo

## Instalación

### Arch Linux ARM
```bash
# Compilar e instalar
makepkg -si

# O instalar desde pre-compilado
sudo pacman -U pocknix-deckstation-*.pkg.tar.zst
```

### Post-instalación
```bash
# Descargar emuladores ARM64
deckstation-setup

# Lanzar
deckstation
```

## Actualización
```bash
deckstation-update
```

## Licencia

Proyecto parte de Pocknix — Licencia GPL v2+

## Créditos

- **Pocknix**: Sistema base
- **DeckStation**: Inspiración original
- **DeckStation ARM**: Adaptación para arquitecturas ARM
- **Emuladores**: RetroArch, Dolphin, DuckStation, PPSSPP, etc. (versiones ARM64)