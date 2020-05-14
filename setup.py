from setuptools import setup, find_packages

setup(
    name='audio',
    version="0.0.1",
    description='fastai_audio, Bluefruit fork',
    url='https://github.com/absw/fastai_audio',
    author='Bluefire Team',
    author_email='bluefire@bluefruit.co.uk',
    license='MIT',
    packages=['audio'],
    install_requires=[
        "fastai",
        "torchaudio",
        "pydub",
        "librosa",
        "matplotlib",
        "fire",
    ],
    zip_safe=False,
)
