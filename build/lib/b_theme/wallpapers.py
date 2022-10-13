from dataclasses import dataclass, field
from typing import Dict, Optional
from dataclass_wizard import YAMLWizard

import os

WALLPAPERS_DEFAULT_PATH = os.path.expanduser(
    '~/.config/theme/wallpapers')


@dataclass
class WallpaperConfig(YAMLWizard):
    path: str = field(default='default')
    stretch: bool = field(default=False)


def load_wallpaper_paths() -> Dict[str, str]:
    return {
        fname: os.path.join(WALLPAPERS_DEFAULT_PATH, fname)
        for fname in os.listdir(WALLPAPERS_DEFAULT_PATH) if fname.endswith(('.jpg', '.jpeg', '.png', '.webp'))
    }


def load_wallpaper_path(fname) -> Optional[str]:
    path = os.path.join(WALLPAPERS_DEFAULT_PATH, fname)
    if os.path.exists(path):
        return path
        
    path = os.path.expanduser(fname)
    if os.path.exists(path):
        return path
