<div align="center">
    <p>Brought to you by <a href="https://flawless.media">Flawless Media - Digitizing and Restoration</a></p>
</div>

# AV RPM
Welcome to AV RPM, my attempt at bringing a variety of unpackaged utilities to 
various RPM-based distro's. 

* **COPR Repo:** https://copr.fedorainfracloud.org/coprs/flawlessmedia/av-rpm/
* **Github**: https://github.com/adworacz/av-rpm

## Requests
Feel free to open a Github issue for any common AV utility or VapourSynth plugin that
you'd like to see added.

## Supported OS
Support for the following operatings systems is provided on a "best effort" basis.

What this means is that if a package doesn't build for a given OS/architecture, a few
minutes will be dedicated to troubleshooting to see if there are any obvious fixes, but not more than that.

Most often this will result in a) a bug report on the upstream project if reasonable (often the case for aarch64 builds
if the x86_64 version succeeds) or b) older OS' not having recent enough versions of dependencies.

In the latter case, nothing can be done, as we don't control what Redhat puts in Fedora/EPEL.

Supported OS List, from most to least:
1. Fedora 43
1. Fedora 42
1. Fedora 41
1. EPEL 10
1. EPEL 9

### CUDA
As of CUDA 13, Nvidia now supports the following operating systems.

1. Fedora 42
1. Fedora 41
1. EPEL 10
1. EPEL 9

### TensorRT
NVIDIA only seems to support TensorRT libraries on EPEL releases.

At the time of this writing, Nvidia doesn't have TensorRT support for EPEL 10 yet.

Hopefully this changes soon.

### Zig
Due to Zig not being available in EPEL10 yet, builds for EPEL10 constantly fail and thus have 
been disabled for the time being. Hopefully this changes with EPEL11.
