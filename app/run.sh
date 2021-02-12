#!/bin/bash

export FLASK_ENV=development
export FLASK_APP=main.py

flask run -p 1133

## run on a public ip
# flask run --host=0.0.0.0
