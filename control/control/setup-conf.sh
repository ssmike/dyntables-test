#!/bin/bash
cd /root/
git clone https://github.com/ssmike/dotfiles config
cd config
git checkout mini
git submodule update --init
./make-symlinks.sh
chsh root -s /bin/zsh
#vim -c ":BundleUpdate"
#rm -r /root/.vim/bundle/YouCompleteMe/
