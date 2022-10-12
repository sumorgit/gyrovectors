from setuptools import setup, find_namespace_packages

with open("requirements.txt", "r") as f:
    requirements = [package.replace("\n", "") for package in f.readlines()]

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name="gyrovectors",
    url="https://github.com/Raffaelbdl/gyrovectors",
    author="Raffael Bolla Di Lorenzo",
    author_email="raffaelbdl@gmail.com",
    packages=find_namespace_packages(),
    install_requires=requirements[:],
    version="0.0.1",
    license="MIT",
    description="Möbius operations",
)
