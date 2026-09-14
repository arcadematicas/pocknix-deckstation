# Pocknix DeckStation

**Sistema de emulación portable para ARM — integrado en Pocknix**

---

## ¿Qué es?

Pocknix DeckStation es un emulador portable que transforma cualquier dispositivo ARM
(Android, Linux ARM, tablets, etc.) en una consola de emulación completa. Está
inspirado en Steam Deck y DeckStation, pero diseñado para funcionar en hardware
de menor potencia.

## Filosofía

- **Todo autocontenido**: Todo vive dentro de `/opt/deckstation/`
- **Nada en el sistema host**: No toca `/home/`, `/etc/` ni configs del usuario
- **Portable**: Mover el directorio funciona en otro dispositivo
- **Sin dependencias del sistema**: Se auto-descarga todo lo necesario
- **Modular**: Cada emulador es independiente

## Estructura del repo

```
pocknix-deckstation/
├── README.md                   # Este archivo
├── .gitignore                  # Qué ignorar
├── PKGBUILD                    # Paquete Arch Linux ARM
├── pocknix-deckstation.install # Hooks de instalación
├── scripts/
│   ├── deckstation-setup.sh    # Descarga emuladores
│   ├── deckstation-launcher.sh # Wrapper del sistema (portable, rutas relativas)
│   ├── deckstation-update.sh   # Actualizador
│   └── setup_arm64_apps.py     # Setup ARM64: busca AppImages aarch64 en PkgForge/GitHub
├── overlay/
│   └── usr/
│       └── bin/
│           └── deckstation     # Comando del sistema
├── configs/                    # Configs portable de emuladores (ver configs/README.md)
│   ├── retroarch/
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
├── DeckStation.AppImage        # La AppImage principal
├── DeckStation.sh              # Script de lanzamiento
├── Apps/                       # Emuladores descargados
├── saves/                      # Saves del usuario
├── logs/                       # Logs de ejecución
├── Media/                      # Assets multimedia
├── settings/                   # Configuraciones
├── scripts/                    # Scripts de gestión
└── configs/                    # Configs del sistema
```

## Cómo funciona

1. **Instalación**: El paquete Arch instala la estructura base
2. **Setup**: `deckstation-setup` descarga los emuladores necesarios
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
# Descargar emuladores
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
- **Emuladores**: RetroArch, Dolphin, AetherSX2, etc.
