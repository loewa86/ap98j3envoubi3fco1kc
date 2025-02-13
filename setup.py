from setuptools import find_packages, setup

setup(
    name="ap98j3envoubi3fco1kc",
    version="0.0.73",
    packages=find_packages(),
    install_requires=["lxml>=4.9.3", "wordsegment==1.3.1", "exorde_data", "aiohttp", "aiohttp_socks"],
    extras_require={"dev": ["pytest", "pytest-cov", "pytest-asyncio"]},
)
