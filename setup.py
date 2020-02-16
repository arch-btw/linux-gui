"""setup.py: setuptools control."""


import re
from setuptools import setup


# version = re.search(
#     r'(VERSION = "(\d.\d.\d)")',
#     open("protonvpn_cli/constants.py").read(),
#     re.M
#     ).group(2)

long_descr = """
The Unofficial Linux GUI for ProtonVPN.

For further information and a usage guide, please view the project page:

https://github.com/calexandru2018/protonvpn-linux-gui
"""


setup(
    name="protonvpn-linux-gui-calexandru2018",
    packages=["protonvpn_linux_gui", "protonvpn_cli_ng"],
    entry_points={
            "console_scripts": "protonvpn-gui = protonvpn_linux_gui.gui:initialize_gui"
        },
    version="1.0.0",
    description="Unofficial Linux GUI client for ProtonVPN",
    long_description=long_descr,
    author="calexandru2018",
    license="GPLv3",
    url="https://github.com/calexandru2018/protonvpn-linux-gui",
    install_requires=[
        "requests",
        "docopt",
    ],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: X11 Applications :: GTK",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
