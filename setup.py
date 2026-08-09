from setuptools import setup, find_packages

setup(
    name="CLIP-CC",
    version="0.1.0",
    description="CLIP-CC: YouTube summary dataset with optional download/clip helper",
    author="Mukhtiar Ali, Harsh Dubey, Sugam Mishra, Chulwoo Pack",
    author_email="sugam.mishra@jacks.sdstate.edu",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "yt-dlp",
        "ffmpeg-python"
    ],
    package_data={
        "clip_cc": ["data/metadata.jsonl"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
