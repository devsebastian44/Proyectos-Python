from setuptools import setup, find_packages

setup(
    name="sysadmin_utils",
    version="1.0.0",
    description="A professional suite of system administration and security tools.",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mysql-connector-python>=8.0.0",
        "pandas>=1.3.0",
        "psutil>=5.8.0",
        "winotify>=1.0.4; sys_platform == 'win32'",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.8",
)
