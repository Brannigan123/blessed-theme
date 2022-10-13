from dataclasses import dataclass, field
from dataclass_wizard import YAMLWizard

import os

from .measurements import MeasurementsConfig
from .wallpapers import WallpaperConfig

THEME_CONFIG_DEFAULT_PATH = os.path.expanduser('~/.config/theme/config.yml')


@dataclass
class ThemeConfig(YAMLWizard):
    colors: str = field(default='default')
    fonts: str = field(default='default')
    measurements: MeasurementsConfig = field(default_factory=MeasurementsConfig)
    wallpaper: WallpaperConfig = field(default_factory=WallpaperConfig)


def load_theme_config() -> ThemeConfig:
    try:
        loaded = ThemeConfig.from_yaml_file(THEME_CONFIG_DEFAULT_PATH)
        if isinstance(loaded, ThemeConfig):
            return loaded
    except Exception:
        pass
    return ThemeConfig()
