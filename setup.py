import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smv2",
    version="0.0.3",
    author="Nova Kwok",
    author_email="noc@nova.moe",
    description="The CLI Tool for SM.MS, based on API v2.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n0vad3v/smv2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "terminaltables"
    ],
    # scripts=['smv2/smv2.py'],
    entry_points={
        'console_scripts': [
            'smv2 = smv2.smv2:exe_main',
        ],
    }
)
