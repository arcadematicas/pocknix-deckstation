# Configs de emuladores — DeckStation ARM

Configuraciones personalizadas importadas desde el proyecto DeckStation ARM
(`/run/media/fransis/8TB/deckstation-arm/`) al repo portable pocknix-deckstation.

## Qué se copió y por qué

| Emulador | Archivo(s) | Origen | Notas |
|---|---|---|---|
| RetroArch | `retroarch/retroarch.cfg` | `.backup-configs-20260624_182554/retroarch.cfg.bak` | Config principal personalizada (116 KB). Sin paths hardcodeados. |
| DuckStation | `duckstation/settings.ini` | `Apps/Duckstation/.../.local/share/duckstation/settings.ini` | Config personalizada (idioma es-ES, fullscreen, etc.). |
| DuckStation | `duckstation/duckstation.ini` | `.backup-configs-20260624_182554/duckstation.ini.bak` | Backup de configuración. |
| DuckStation | `duckstation/qt.conf` | `Apps/Duckstation/qt.conf` | Plugins relativos (`./QtPlugins`), portable. |
| Azahar | `azahar/qt-config.ini` | `.backup-configs-20260624_182554/azahar-qt-config.ini.bak` | Paths nand/sdmc/screenshots convertidos a relativos. |
| Citron | `citron/qt-config.ini` | `.backup-configs-20260624_182554/citron-qt-config.ini.bak` | Paths nand/sdmc/load/dump/tas relativos; paths de ROMs eliminados. |
| Citron | `citron/custom/*.ini` | `Apps/Citron/.../.config/citron/custom/` | Configs por juego (10 títulos). |
| Dolphin | `dolphin/dolphin.ini` | `.backup-configs-20260624_182554/dolphin.ini.bak` | Eliminado `ISOPath1` (apuntaba a ROMs del usuario). |
| PCSX2 | `pcsx2/pcsx2.ini` | `.backup-configs-20260624_182554/pcsx2.ini.bak` | Eliminado `RecursivePaths` (apuntaba a ROMs del usuario). |
| PPSSPP | `ppsspp/ppsspp.ini` | `.backup-configs-20260624_182554/ppsspp.ini.bak` | `CurrentDirectory` convertido a relativo (`./`). |
| Flycast | `flycast/emu.cfg` | `Apps/Flycast/.../.config/flycast/emu.cfg` | Config limpia, sin paths hardcodeados. |
| DOSBox Pure | `dosboxpure/DOSBoxPure.cfg` | `Apps/DosBoxPure/.../.config/DOSBoxPure/DOSBoxPure.cfg` | `interface_contentpath` → `./ROMs/dos`. |
| RMG | `rmg/mupen64plus.cfg` | `Apps/RMG/.../.config/RMG/mupen64plus.cfg` | Config limpia. |
| ZSNES | `zsnes/*.cfg` | `Apps/ZSNES/.../.config/zsnes/` | Configs de input y video (zmovie, zinput, zsnesl). |
| Supermodel | `supermodel/Supermodel.ini` | `Apps/Supermodel/.../.config/supermodel/Config/Supermodel.ini` | Config limpia. |
| AntiMicroX | `antimicrox/antimicrox_settings.ini` | `Apps/Antimicrox/.../.config/antimicrox/` | Paths de perfiles convertidos a relativos. |
| Vita3K | `vita3k/*.xml` | `Apps/Vita3K/.../.config/Vita3K/config/` | Configs por juego (3 títulos). |

## Qué NO se copió (y por qué)

- **AppImages** — binarios grandes que se descargan con `setup_arm64_apps.py`.
- **ROMs / saves / memcards / savestates** — contenido del usuario, privado.
- **Caches** (shader cache, mesa) — se regeneran en runtime.
- **`QtProject.conf`** de DuckStation/Azahar — solo estado de UI con paths
  hardcodeados del sistema original.
- **`DeckStation.AppImage.home/`** — **el directorio estaba VACÍO** en el
  proyecto origen, por lo que no había configs de ES-DE que copiar.
- **`es_find_rules.xml`** — **no existe** en el proyecto DeckStation ARM
  (búsqueda exhaustiva en `deckstation-arm/`). Si ES-DE usa reglas custom,
  habrá que crearlas desde cero.

## Nota sobre `configs/es-de-home/`

Este directorio está reservado para los configs de ES-DE (el frontend). En el
proyecto origen `DeckStation.AppImage.home/` estaba vacío, así que no se pudo
importar nada. Cuando se personalice ES-DE, los configs deben ir aquí con
rutas relativas.