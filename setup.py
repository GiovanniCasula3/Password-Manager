from setuptools import setup, find_packages

setup(
    name="password-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography>=3.4.7",
        "argon2-cffi>=21.3.0",
        "PyYAML>=6.0",
        "pytest>=7.0.0",
        "python-dotenv>=0.19.0"
    ],
    entry_points={
        'console_scripts': [
            'password-manager=src.cli.interface:main',
        ],
    }
)