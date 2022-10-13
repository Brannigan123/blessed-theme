from dataclasses import dataclass, field
from dataclass_wizard import YAMLWizard
from typing import Dict

import os

COLOR_SCHEMES_DEFAULT_PATH = os.path.expanduser(
    '~/.config/theme/colors')


@dataclass
class ColorScheme(YAMLWizard):
    background: str = field(default='#282a36')
    foreground: str = field(default='#f8f8f2')
    black: str = field(default='#21222c')
    gray: str = field(default='#5a5958')
    red: str = field(default='#ff5555')
    green: str = field(default='#50fa7b')
    yellow: str = field(default='#f1fa8c')
    orange: str = field(default='#ffb86c')
    blue: str = field(default='#bd93f9')
    magenta: str = field(default='#ff79c6')
    cyan: str = field(default='#8be9fd')
    white: str = field(default='#f8f8f2')


def load_color_schemes() -> Dict[str, ColorScheme]:
    schemes: Dict[str, ColorScheme] = {}

    for fname in os.listdir(COLOR_SCHEMES_DEFAULT_PATH):
        if fname.endswith('.yml'):
            try:
                scheme = ColorScheme.from_yaml_file(
                    os.path.join(COLOR_SCHEMES_DEFAULT_PATH, fname)
                )
                if isinstance(scheme, ColorScheme):
                    schemes[fname[:-4]] = scheme
            except Exception:
                pass

    return schemes


def load_color_scheme(name: str) -> ColorScheme:
    try:
        fname = f'{name}.yml'
        scheme = ColorScheme.from_yaml_file(
            os.path.join(COLOR_SCHEMES_DEFAULT_PATH, fname)
        )
        if isinstance(scheme, ColorScheme):
            return scheme
    except Exception:
        pass
    return ColorScheme()
