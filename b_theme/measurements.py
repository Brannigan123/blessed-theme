from dataclasses import dataclass, field
from dataclass_wizard import YAMLWizard


@dataclass
class MeasurementsConfig(YAMLWizard):
    padding: int=field(default=4)
    margin: int=field(default=2)
    border_width: int=field(default=3)


