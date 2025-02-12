# pymt_heatc

This is an example of building a model, written in C and wrapped in
Python with the [babelizer](https://github.com/csdms/babelizer), with
the [meson-python](https://meson-python.readthedocs.io/en/latest/) build
system using a `pyproject.toml` file to describe the build.

## Build/Install

This is a sketch of how to build and install this project.

1. Create the conda environment from [environment.yml](./environment.yml) and activate it.
2. Build/install the [C BMI example](https://github.com/csdms/bmi-example-c/#buildinstall)
3. Build/install this project with `make install`

## Use

Import the standalone project into a Python session:

``` python
>>> import pymt_heatc
```

Import the *pymt* component:

``` python
>>> from pymt.MODELS import HeatModelC
```

Try the examples in the [examples](./examples/) directory.
