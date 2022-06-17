#!/bin/bash
echo "Phease enter project name"
read -r name
if [ ! -d $name ]
then
    mkdir -p $name
fi
virtualenv -p "C:\Users\tuan.tran-quoc\AppData\Local\Programs\Python\Python39\python.exe" "env"

# Get requirement library
# pip freeze > requirements.txt
# Install follow requirements
# pip install -r requirements.txt