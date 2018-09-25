# hactar/python-base

A base container on which to build your python project. Installs all the bits you need to get Weasyprint and Pillow to operate, as well as a a couple of bits for asset compilation.


## Building

    docker build -t hactar/python-base .

or if you need to force the build...

    docker build -t hactar/python-base . --no-cache

## Pushing to Quay.io

Right after building, you can usually get the container ID with...

    docker run hactar/python-base
    docker ps -l

You can then push it to Quay.io with

    docker commit {containerId} quay.io/hactar/python-base
    docker push quay.io/hactar/python-base


## Supported Webassets filters

### Javascript Compilers

* Closure Compiler
* uglify-js


### CSS Compilers

* libsass

