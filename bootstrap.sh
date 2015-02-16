#!/usr/bin/env bash

apt-get update
update-alternatives --install /usr/bin/python python /usr/bin/python3 10
apt-get install -y python3-setuptools
sudo easy_install3 pip
pip install Django==1.7.4
