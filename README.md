# data-science-boilerplate
## Getting Started
This project assumes you have Anaconda or Miniconda installed on your machine. If you do not, please install from https://docs.conda.io/en/latest/miniconda.html. This is my boilerplate loosely based on [Cookie Cutter Data Science](https://github.com/drivendata/cookiecutter-data-science), with modifications including easier Anaconda support, `isort` seeding, pre-commit configs, and Travis CI.
1.  `git clone` this repository in the desired directory on your local machine.
2. `cd` into the project directory.
3. To create a conda environment:
    ```
    conda create -n <env_name> dep1 dep2 ...
    conda env export --no-builds --from-history | grep -v "prefix" > environment.yml
    ```
    These in the `export` command flags add only explicit dependencies to `environment.yml` and prevent cross-platform build issues with dependencies during CI.
    If you would like to use the premade `environment.yml` in this project, create an environment as follows:
    ```
    conda env create -f environment.yml
    ```
4. Run `conda env update && conda activate <env_name>`.
5. Run `pip install -e .`.
6. Run `pre-commit install`.
7. **If you would like to run tests:** In `.travis.yml`, uncomment `python -m pytest tests --cov=src --cov-fail-under=0` and change the `--cov-fail-under` value in  to your intended test coverage percentage.
