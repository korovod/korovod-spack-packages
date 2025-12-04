# korovod-spack-packages

This repository contains a collection of [Spack](https://spack.io/) packages to build the Korovod suite. You can add the current repository to your Spack installation using:

```console
spack repo add --name korovod https://github.com/korovod/korovod-spack-packages.git
```

## Packages

The following packages can be installed using this repository:

### nanotron

https://github.com/korovod/kenotron

```bash
spack install py-nanotron
```

If you want to install C++ extensions for Nanotron in one shot, use the following command:

```bash
spack install py-nanotron +datastates
```

### datastates

https://github.com/korovod/datastates

```bash
spack install py-datastates
```

## Patches

These packages are broken upstream. This repository patches them (this is transparent to you).

### htmldate & dateutil

This release https://github.com/dateutil/dateutil/releases/tag/2.9.0.post0 pins `setuptools_scm` to `<8` which is bad because not compatible with Python 3.13. There should be a new release without such a constraint. Waiting for it. Project seems unmaintained.

### kenlm

Python 3.13 breaks the build

- https://github.com/kpu/kenlm/pull/468
- https://github.com/kpu/kenlm/pull/473
