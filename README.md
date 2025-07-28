# AV RPM
Welcome to AV RPM, my attempt at bringing a variety of unpackaged utilities to 
various RPM-based distro's. 

**COPR Repo:** https://copr.fedorainfracloud.org/coprs/flawlessmedia/av-rpm/

## Requests
Feel free to open an issue for any common AV utility or VapourSynth plugin that
you'd like to see added.

## Supported OS
Support for the following operatings systems is provided on a "best effort" basis.

What this means is that if a package doesn't build for a given OS/architecture, a few
minutes will be dedicated to troubleshooting to see if there are any obvious fixes, but not more than that.

Most often this will result in a) a bug report on the upstream project if reasonable (often the case for aarch64 builds
if the x86_64 version succeeds) or b) older OS' not having recent enough versions of dependencies.

In the latter case, nothing can be done, as we don't control what Redhat puts in Fedora/EPEL.

Supported OS List, from most to least:
1. Fedora 42
2. Fedora 41
3. EPEL 10
4. EPEL 9

### CUDA
NVIDIA often lags a bit behind more recent Fedora (and EPEL) releases.

At this time, NVIDIA only officially supports Fedora 41 (and not 42), and EPEL 9 (and not EPEL 10).

This means that CUDA plugins are only available on:
1. Fedora 41
2. EPEL 9

### TensorRT
NVIDIA only seems to support TensorRT libraries on EPEL releases.

Since NVIDIA doesn't support CUDA on EPEL 10 (yet), only EPEL 9 provides TensorRT support.
