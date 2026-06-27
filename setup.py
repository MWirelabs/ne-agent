from setuptools import setup, find_packages

setup(
    name="ne-agent",
    version="0.1.0",
    author="MWire Labs",
    author_email="connect@mwirelabs.com",
    description="First open-source AI agent for Northeast Indian languages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MWirelabs/ne-agent",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
