# Starterpack UI Tests framework. Powered by Python and Selenium.
=================================================
## Requirements
Python 3.9+

### Install Python 3
https://www.python.org/downloads/

### Install pip if needed
https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py

### Install poetry
https://pypi.org/project/poetry/

## Для pre-commit проверок установи pre-commit
1. Для Linux `pip install pre-commit` или для Mac `brew install pre-commit`

2. Выполни `poetry install`

3. Установи git-хуки в свою .git-папку:
`pre-commit install`
Удали `rm .git/hooks/pre-commit.legacy` если этот хук был создан предыдущей командой

4. Запустить принудительную проверку всех файлов в проекте:
`pre-commit run --all-files`

5. Запустить проверку только для измененных файлов (нужен git add --all):
`pre-commit run`

### Change stage for run tests
Change variable TESTING_HOST_URL in pytest-local.ini file

### Run all your tests with local Python in `uitests` directory
`poetry run pytest tests -c tests/pytest-local.ini` – with config `pytest-local.ini`

### Run your tests with parallel mode
Change in *.ini-file `addopts = -nX` option for desired count of parallel tests

## HTML report output
Add "--html=\`pwd\`/output/report.html --self-contained-html" to pytest-command to generate HTML-report in .../output/ directory
Default for docker-script

You can view report in http://localhost:8000/output/report.html

`python3 -m http.server`

## Run with custom ONE thread and without reruns on failed tests
`poetry run pytest tests -c tests/pytest-local.ini -n0 --reruns 0`

## Run one specific test
`poetry run pytest tests/test_sample_ui.py -k 'test_example' -c tests/pytest-local.ini`

## Run one specific file with tests
`poetry run pytest tests/test_sample_ui.py -c tests/pytest-local.ini`

## Config count of rerunning failed tests
`-max-runs=X` in pytest-local.ini file
