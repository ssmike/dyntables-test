#!/bin/bash
cd /root/
git init
git remote add origin https://github.com/ssmike/dotfiles
git pull origin
git checkout mini
git submodule update --init
chsh root -s /bin/zsh
