from setuptools import setup, find_packages

setup(
    name="ne-agent",
    version="0.2.0",
    author="MWire Labs",
    author_email="connect@mwirelabs.com",
    description="First open-source AI agent for Northeast Indian languages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MWirelabs/ne-agent",
    packages=find_packages(),
    package_data={"ne_agent": ["data/*.txt"]},
    install_requires=[
        "ne-lid",
        "ne-embed",
        "faiss-cpu",
        "rich",
        "requests",
        "pandas",
        "openpyxl",
        "transformers",
        "torch",
        "sentencepiece",
        "soundfile",
        "librosa",
    ],
    entry_points={
        "console_scripts": [
            "ne-agent=ne_agent.cli:main",
        ],
    },
    python_requires=">=3.9",
    license="CC-BY-4.0",
)
