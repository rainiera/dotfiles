### Conda envs

[how-to](http://conda.pydata.org/docs/using/envs.html)

```
#!/bin/bash

for CONDA_ENV in *.yml; do
    echo "conda env create -f $CONDA_ENV"
    conda env create -f $CONDA_ENV
done

conda env list
```
