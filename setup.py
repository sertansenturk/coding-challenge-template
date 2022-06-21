import os
import re

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))
EXP_DIR = "src"
PACKAGE_NAME = "challenge_template"


def get_version():
    """Read version from __init__.py
    Raises:
        ValueError: if __init__ is not read, or __version__ is not in __init__
    Returns:
        str -- value of __version__ as defined in __init__.py
    """
    version_file = os.path.join(HERE, EXP_DIR, PACKAGE_NAME, "__init__.py")
    with open(version_file, encoding="utf-8") as f:
        init_contents = f.read().strip()

        exp = r"^__version__ = ['\"]([^'\"]*)['\"]"
        mo = re.search(exp, init_contents, re.M)
        if mo:
            return mo.group(1)

        raise ValueError(
            f"Unable to find version string in {version_file}:\n{init_contents}"
        )


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    entry_points={"console_scripts": ["ct = challenge_template.driver:main"]},
    author="Sertan Senturk",
    author_email="contact AT sertansenturk DOT com",
    maintainer="Sertan Senturk",
    maintainer_email="contact AT sertansenturk DOT com",
    url="https://github.com/sertansenturk/challenge_template",
    description="Makam Recognition Experiments",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    platforms="Linux",
    license="agpl 3.0",
    keywords=("machine-learning " "information-retrieval " "computational-analysis"),
    packages=find_packages(EXP_DIR),
    package_dir={"": EXP_DIR},
    python_requires="==3.8.*",
    install_requires=[],  # in requirements.txt
)
