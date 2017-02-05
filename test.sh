#!/bin/bash
set -e

for i in `ls src/*Test.py`; do
    echo $i
    python $i
done
