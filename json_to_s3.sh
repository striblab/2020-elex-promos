#!/bin/bash

csvjson data/local.csv > data/local.json
csvjson data/wire.csv > data/wire.json

python s3.py
