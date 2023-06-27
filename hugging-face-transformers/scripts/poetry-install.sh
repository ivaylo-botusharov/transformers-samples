#!/bin/bash

sudo -H curl -sSL 'https://install.python-poetry.org' | python3 -

if ! (grep 'export PATH="$HOME/.local/bin:$PATH"' < ~/.zshrc); then
    echo '\nexport PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc;
fi
