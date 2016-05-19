#!/bin/bash
# Authored by Rainier Ababao on 05/18/16

for CONDA_ENV in *.yml; do
    echo "conda env create -f $CONDA_ENV"
    conda env create -f $CONDA_ENV
done

conda env list
