#!/usr/bin/env python3
"""
Setup ARM64/aarch64 emulators for DeckStation.
Searches PkgForge (pkgforge-dev) and GitHub releases for aarch64 AppImages.
"""
import os
import subprocess
import requests
import sys
import time

# Define the base directory (portable: derive from script location or env var)
# DECKSTATION_ROOT env var takes precedence; otherwise use the parent of scripts/
BASE_DIR = os.environ.get(
    "DECKSTATION_ROOT",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)
APPS_DIR = os.path.join(BASE_DIR, "Apps")

# ─── PkgForge AppImage repos (pkgforge-dev organization on GitHub) ───────────
# These repos build and maintain aarch64 AppImages for Linux emulators.
# https://pkgforge.dev / https://github.com/pkgforge
PKGFORGE_REPOS = {
    "Dolphin":    "pkgforge-dev/Dolphin-emu-AppImage",
    "Flycast":    "pkgforge-dev/Flycast-AppImage-Enhanced",
    "MAME":       "pkgforge-dev/MAME-AppImage",
    "Supermodel": "pkgforge-dev/Supermodel-AppImage",
    "Cemu":       "pkgforge-dev/Cemu-AppImage-Enhanced",
    "Xemu":       "pkgforge-dev/Xemu-AppImage",
}

# ─── Fallback GitHub repos (official upstream or community builds) ───────────
# Used when PkgForge doesn't have an aarch64 AppImage.
FALLBACK_REPOS = {
    "DuckStation":  "stenzek/duckstation",
    "PPSSPP":       "hrydgard/ppsspp",
    "mGBA":         "mgba-emu/mgba",
    "RetroArch":    "libretro/RetroArch",
    "Dolphin":      "dolphin-emu/dolphin",
    "Mesen":        "SourMesen/Mesen",
    "Flycast":      "flyinghead/flycast",
    "MAME":         "mamedev/mame",
    "Xemu":         "xemu-project/xemu",
    "Supermodel":   "trzy/Supermodel",
    "Redream":      "inolen/redream",
    "Cemu":         "cemu-project/Cemu",
}

# Ordered list of apps to process (PkgForge repo is tried first)
APPS_TO_SETUP = [
    "DuckStation",
    "PPSSPP",
    "mGBA",
    "RetroArch",
    "Dolphin",
    "Cemu",
    "Mesen",
    "Flycast",
    "MAME",
    "Xemu",
    "Supermodel",
    "Redream",
]

GITHUB_API = "https://api.github.com"


def get_latest_release_assets(repo):
    """Return list of (download_url, filename) from the latest release."""
    url = f"{GITHUB_API}/repos/{repo}/releases/latest"
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        assets = resp.json().get("assets", [])
        return [(a["browser_download_url"], a["name"]) for a in assets]
    except Exception as e:
        print(f"  Error fetching release for {repo}: {e}")
    return []


def pick_arm64_asset(assets):
    """Pick the best aarch64/arm64 AppImage (or tar.xz) from a list of assets."""
    # Priority: .appimage > .tar.xz
    for ext in (".appimage", ".tar.xz"):
        for url, name in assets:
            nl = name.lower()
            if ("aarch64" in nl or "arm64" in nl) and nl.endswith(ext):
                return url, name
    return None, None


def find_asset(app_name):
    """
    Search for an aarch64/arm64 asset across:
      1. PkgForge repo (if available for this app)
      2. Fallback upstream repo
    """
    # 1) Try PkgForge first
    if app_name in PKGFORGE_REPOS:
        pf_repo = PKGFORGE_REPOS[app_name]
        print(f"  [PkgForge] {pf_repo}")
        assets = get_latest_release_assets(pf_repo)
        url, name = pick_arm64_asset(assets)
        if url:
            return url, name, pf_repo

    # 2) Try fallback repo
    if app_name in FALLBACK_REPOS:
        fb_repo = FALLBACK_REPOS[app_name]
        print(f"  [GitHub]   {fb_repo}")
        assets = get_latest_release_assets(fb_repo)
        url, name = pick_arm64_asset(assets)
        if url:
            return url, name, fb_repo

    return None, None, None


def setup_app(app_name):
    """Download and set up a single app."""
    print(f"\n{'='*60}")
    print(f"Setting up {app_name}")
    print(f"{'='*60}")

    app_dir = os.path.join(APPS_DIR, app_name)
    os.makedirs(app_dir, exist_ok=True)

    download_url, filename, source_repo = find_asset(app_name)
    if not download_url:
        print(f"  ✗ No aarch64/arm64 AppImage or tar.xz found for {app_name}")
        return False

    file_path = os.path.join(app_dir, filename)
    print(f"  Downloading {filename} from {source_repo}...")
    try:
        resp = requests.get(download_url, stream=True, timeout=120)
        resp.raise_for_status()
        total = int(resp.headers.get("content-length", 0))
        downloaded = 0
        with open(file_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=65536):
                f.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded * 100 // total
                    print(f"\r  Progress: {pct}% ({downloaded}/{total})", end="", flush=True)
        print()  # newline after progress

        if filename.lower().endswith(".appimage"):
            os.chmod(file_path, 0o755)
            print(f"  ✓ AppImage made executable: {filename}")
        elif filename.lower().endswith(".tar.xz"):
            subprocess.run(["tar", "-xf", file_path, "-C", app_dir], check=True)
            os.remove(file_path)
            print(f"  ✓ Extracted: {filename}")

        print(f"  ✓ Installed in {app_dir}")
        return True
    except Exception as e:
        print(f"  ✗ Error setting up {app_name}: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)
        return False


def main():
    if not os.path.exists(APPS_DIR):
        print(f"Error: {APPS_DIR} does not exist.")
        sys.exit(1)

    print(f"DeckStation ARM64 Emulator Setup")
    print(f"Target directory: {APPS_DIR}")
    print(f"Apps to process: {len(APPS_TO_SETUP)}")

    results = {"success": [], "failed": []}
    for app_name in APPS_TO_SETUP:
        ok = setup_app(app_name)
        if ok:
            results["success"].append(app_name)
        else:
            results["failed"].append(app_name)
        time.sleep(1)  # Be nice to GitHub API

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Successfully installed ({len(results['success'])}):")
    for name in results["success"]:
        print(f"  ✓ {name}")
    if results["failed"]:
        print(f"\nFailed / not available ({len(results['failed'])}):")
        for name in results["failed"]:
            print(f"  ✗ {name}")
    print(f"\nTotal: {len(results['success'])}/{len(APPS_TO_SETUP)}")


if __name__ == "__main__":
    main()
