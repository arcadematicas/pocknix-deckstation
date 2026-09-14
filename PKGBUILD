# Maintainer: Pocknix Team <pocknix@example.com>
pkgname=pocknix-deckstation
pkgver=1.0.0
pkgrel=1
pkgdesc="Sistema de emulación portable para ARM — integrado en Pocknix"
arch=('aarch64' 'armv7h')
url="https://github.com/pocknix/pocknix-deckstation"
license=('GPL2')
depends=(
    'python'
    'python-requests'
    'gamemode'
)
makedepends=()
optdepends=(
    'lib32-mesa: soporte OpenGL 32-bit'
    'vulkan-icd-loader: soporte Vulkan'
    'pulseaudio: audio del sistema'
    'pipewire-pulse: audio moderno'
)
source=()
sha256sums=()
install=pocknix-deckstation.install

package() {
    # Directorio base
    install -dm755 "${pkgdir}/opt/deckstation"

    # Scripts principales
    install -Dm755 scripts/deckstation-setup.sh \
        "${pkgdir}/opt/deckstation/scripts/deckstation-setup.sh"
    install -Dm755 scripts/deckstation-launcher.sh \
        "${pkgdir}/opt/deckstation/scripts/deckstation-launcher.sh"
    install -Dm755 scripts/deckstation-update.sh \
        "${pkgdir}/opt/deckstation/scripts/deckstation-update.sh"
    install -Dm755 scripts/setup_arm64_apps.py \
        "${pkgdir}/opt/deckstation/scripts/setup_arm64_apps.py"

    # Configs de emuladores (portables, rutas relativas)
    install -dm755 "${pkgdir}/opt/deckstation/configs"
    cp -r configs/* "${pkgdir}/opt/deckstation/configs/"

    # Overlay: comando del sistema
    install -Dm755 overlay/usr/bin/deckstation \
        "${pkgdir}/usr/bin/deckstation"

    # Estructura de directorios (se crearán en post-install)
    install -dm755 "${pkgdir}/opt/deckstation/Apps"
    install -dm755 "${pkgdir}/opt/deckstation/saves"
    install -dm755 "${pkgdir}/opt/deckstation/logs"
    install -dm755 "${pkgdir}/opt/deckstation/Media"
    install -dm755 "${pkgdir}/opt/deckstation/settings"
}
