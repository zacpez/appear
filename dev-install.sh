#!/bin/bash

python setup.py build
python setup.py install
appear-schema --help
echo ""
echo "The above print is the installed varient of Appear Schema"
