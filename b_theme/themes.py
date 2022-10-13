from dataclasses import dataclass
from dataclass_wizard import YAMLWizard

from .colors import ColorScheme, load_color_scheme
from .fonts import FontScheme, load_font_scheme
from .measurements import MeasurementsConfig
from .wallpapers import WallpaperConfig
from .config import load_theme_config


@dataclass
class Theme(YAMLWizard):
    colors: ColorScheme
    fonts: FontScheme
    measurements: MeasurementsConfig
    wallpaper: WallpaperConfig


def load_theme() -> Theme:
    config = load_theme_config()
    return Theme(
        colors=load_color_scheme(config.colors),
        fonts=load_font_scheme(config.fonts),
        measurements=config.measurements,
        wallpaper=config.wallpaper
    )
