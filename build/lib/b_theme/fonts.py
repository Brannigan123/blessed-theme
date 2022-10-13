from dataclasses import dataclass
from dataclass_wizard import YAMLWizard
from typing import Dict

import os

FONT_SCHEMES_DEFAULT_PATH = os.path.expanduser(
    '~/.config/theme/fonts')


@dataclass
class FontScheme(YAMLWizard):
    power_font: str
    power_font_size: int
    font0: str
    font0_size: int
    font1: str
    font1_size: int
    font2: str
    font2_size: int
    font3: str
    font3_size: int
    font4: str
    font4_size: int
    font5: str
    font5_size: int


def load_font_schemes() -> Dict[str, FontScheme]:
    schemes: Dict[str, FontScheme] = {}

    for fname in os.listdir(FONT_SCHEMES_DEFAULT_PATH):
        if fname.endswith('.yml'):
            try:
                scheme = FontScheme.from_yaml_file(
                    os.path.join(FONT_SCHEMES_DEFAULT_PATH, fname)
                )
                if isinstance(scheme, FontScheme):
                    schemes[fname[:-4]] = scheme
            except Exception:
                pass

    return schemes


def load_font_scheme(name: str) -> FontScheme:
    try:
        fname = f'{name}.yml'
        scheme = FontScheme.from_yaml_file(
            os.path.join(FONT_SCHEMES_DEFAULT_PATH, fname)
        )
        return scheme if isinstance(scheme, FontScheme) else scheme[0]
    except Exception:
        pass
    return FontScheme()