# data-science-boilerplate
[![Build Status](https://app.travis-ci.com/camille-004/data-science-boilerplate.svg?branch=main)](https://app.travis-ci.com/camille-004/data-science-boilerplate)
## Getting Started
This project assumes you have Anaconda or Miniconda installed on your machine. If you do not, please install from https://docs.conda.io/en/latest/miniconda.html. This is my boilerplate loosely based on [Cookie Cutter Data Science](https://github.com/drivendata/cookiecutter-data-science), with modifications including easier Anaconda support, `isort` seeding, pre-commit configs, and Travis CI. If you would like to run a CI pipeline, make sure you have an account on [Travis CI](https://www.travis-ci.com/?_gl=1%2A1rbqnop%2A_ga%2ANTAxOTY5NDU3LjE2NTAxODczMDQ.%2A_ga_XRYGSZFQ0P%2AMTY1MDE4NzMwNC4xLjEuMTY1MDE5NzIzMi41OA..) and authorize builds on your GitHub repository. Otherwise, you may remove `.travis.yml`.
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
7. If you want to run CI, change `conda activate boilerplate` to `conda activate <your_env_name>`.
8. If you wish to use documentation, make any edits necessary in `docs/source/conf.py` and `docs/source/index.rst`, or add your own reStructuredText pages.
9. **If you to include test coverage in your build:** In `.travis.yml`, uncomment `python -m pytest tests --cov=src --cov-fail-under=0` and change the `--cov-fail-under` value in  to your intended test coverage percentage.

## To-Do
- [ ] Add `config` folder under `src` to keep all the YAML files which can then be used for data validation and settings management via Pydantic.
- [ ] Update `docs`.
- [X] Under `src`, the models folder will only contain the DL model building code or ML model code, nothing more.
- [X] Under `src`, a separate directory for training under which all the training code will reside.
- [X] Same for `inference`; a separate directory for inference and other supporting code which is always required in CV or NLP tasks.
- [X] Under `src`, create a directory with the name `base` to store all the base classes.
- [X] Under `src`, create a directory with the name `logger` to set up:
    1. Logging module to log code
    2. Model logging using Tensorboard, MLflow, or any other model logger.
- [X] Move the visualization directory  outside of `src` and store all the model logger visualizations and other charts in that folder that way it would be easy to track using DVC.
- [X] Rename the `data` folder to `data_blobs`, that way it is clear it is only used for data storage.
- [X] Rename the `model` folder to `model_weights`.
- [X] Add `docs` folder.
