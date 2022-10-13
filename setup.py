from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Package for reading & writing custom theme configs'
LONG_DESCRIPTION = 'Package for reading & writing custom theme configs'

packages = find_packages()
package_data = {package: ["py.typed"] for package in packages}


setup(
    name="b_theme",
    version=VERSION,
    author="Brannigan Sakwah",
    author_email="<brannigansakwah@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=packages,
    package_data=package_data,
    install_requires=[
        'dataclass_wizard',
    ],
    keywords=['python', 'theme', 'config', 'qtile'],
)
