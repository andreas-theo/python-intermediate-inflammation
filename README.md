# Inflam
![Continuous Integration build in GitHub Actions](https://github.com/andreas-theo/python-intermediate-inflammation/actions/workflows/main.yml/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features
Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites
Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing


## Installation
You can install the package by cloning the repository and then running
the following command in your virtual environment:
```
python3 -m pip install -r requirements.txt
```

## Contributing
To contribute please fork the repository, create a new branch from
develop and then file a pull request.

## Contact
Please file issues on this repository if you would like to discuss the software.

## Licence
The project is licensed under the MIT licence.

## Usage
You can run the inflammation analysis by issuing:
```
python3 inflammation-analysis.py --view visualize --patient <patient number> data/inflammation-01.csv
```
To see the results in plain text you can run:
```
python3 inflammation-analysis.py --view record --patient <patient number> data/inflammation-01.csv
```
