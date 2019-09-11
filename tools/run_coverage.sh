#!/usr/bin/env bash

source ./env/bin/activate
pytest --cov --cov-report html --cov-report term-missing
open /Applications/Google\ Chrome.app htmlcov/index.html
