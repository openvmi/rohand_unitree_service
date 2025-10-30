from setuptools import setup, find_packages

VERSION = "25.10.30"

INSTALL_REQUIRES = []
EXCLUDE_PACKAGES = [
    "ohand_serial_sdk_python",
    "unitree_sdk2_python"
]

setup(
    name="rohand_unitree_service",
    version=VERSION,
    author="oymotion",
    author_email="info@oymotion.com",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdonw",
    license="BSD-2-Clause",
    description="rohand service for unitree",
    url="",
    packages=find_packages(where="src", exclude=EXCLUDE_PACKAGES),
    package_dir={"":"src"},
    install_requreis=INSTALL_REQUIRES
)