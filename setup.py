from setuptools import setup, find_packages

setup(
    name="nxtabroad-visa-readiness-ml",
    version="1.0.0",
    description="NxtAbroad AI – Visa Readiness & Eligibility Intelligence Engine",
    author="Ibrahim Akintunde Akinyera",
    author_email="team@nxtabroad.com",
    packages=find_packages(where=".", exclude=("tests", "docs", "site")),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "python-dateutil>=2.8.2",
        "argparse>=1.4.0",
        "xlrd>=2.0.1",
        "openpyxl>=3.1.0",
        "scikit-learn>=1.0.2",
        "joblib>=1.2.0",
        "fastapi>=0.110.0",
        "uvicorn>=0.24.0",
        "requests>=2.31.0",
    ],
    python_requires=">=3.9",
)