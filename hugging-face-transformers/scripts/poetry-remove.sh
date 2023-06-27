#!/bin/bash

# Uninstall Poetry
curl -sSL https://install.python-poetry.org | python3 - --uninstall

curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -

sudo rm -rf ~/.cache/pypoetry

sudo rm -rf ~/Library/Caches/pypoetry
