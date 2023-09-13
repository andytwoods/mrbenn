import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="mrbenn-toolbar-plugin",
    version="0.0.2",
    description="An addon for Django Debug Toolbar that allows for directly opening static files and views",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/andytwoods/mrbenn",
    author="Andy Woods",
    author_email="andytwoods@gmail.com",
)
