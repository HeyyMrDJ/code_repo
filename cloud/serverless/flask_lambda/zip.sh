#!/bin/sh

python3 -m pip install --target ./package -r requirements.txt
cd package
zip -r ../my-deployment-package.zip .
cd ..
zip -g my-deployment-package.zip app.py