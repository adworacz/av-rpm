
# Setup - Fedora
```sh
sudo dnf install fedora-packager
```

cd to directory with spec file.

```sh
spectool -g foo.spec
```

```
fedpkg --release 42 mockbuild
```

## Build multiple dependent packages together.
Given an example of package A which depends on package B:

1. Create SRPM files for both packages. `fedpkg --release f42 srpm` in each directory is a great help.
2. Run a mock build (which writes results to a local `.results` directory) that chains both together:
`mock --localrepo .results --chain path/to/package-b.srpm path/to/packaga-a.srpm`

Note the order of the `--chain` params

## Build packages that require network access
For example rust packages using cargo directly need network access.

```
fedpkg --release 42 mockbuild --enable-network
```

# Setup - RPM compatible

```sh
rpmdev-setuptree
```

Sets up the ~/rpmbuild directory and subdirectories.

```sh
spectool -g -R foo.spec
```
Gets the sources for the given spec into the ~/rpmbuild/SOURCES directory.

```sh
rpmbuild -ba foo.spec
```

Builds the given spec file (presuming sources have been downloaded).


## References:
* https://docs.fedoraproject.org/en-US/package-maintainers/Installing_Packager_Tools/
* https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_1_banner/
* https://docs.fedoraproject.org/en-US/packaging-guidelines/Meson/
* http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html

## CUDA packages
CUDA toolkit needs to be installed from Nvidia, apparently:
https://rpmfusion.org/Howto/CUDA?hig%2E%2E%2E9#CUDA_Toolkit
