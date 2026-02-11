
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

## Build cross-architecture
Hint: Use `--root fedora-42-aarch64` as an example.

```
fedpkg --release 42 mockbuild --root fedora-42-aarch64
```

## CUDA packages
CUDA toolkit needs to be installed from Nvidia, apparently:
https://rpmfusion.org/Howto/CUDA?hig%2E%2E%2E9#CUDA_Toolkit

## Build CUDA packages locally
We need to use `mock` directly, since `fedpkg` doesn't expose the `--addrepo` option unfortunately...

So in the directory that contains the spec file in question:
2. Fedora: `fedpkg --release f42 srpm && mock -r fedora-42-x86_64 --addrepo https://developer.download.nvidia.com/compute/cuda/repos/fedora42/x86_64 --resultdir result_foobar foobar.src.rpm`
3. EPEL: `fedpkg --release epel10 srpm && mock -r rocky+epel-10-x86_64 --addrepo https://developer.download.nvidia.com/compute/cuda/repos/rhel10/x86_64 --resultdir result_foobar foobar.src.rpm`

## COPR dependencies
To build packages that depend on other packages that already exist in the COPR repo, use a command like:

```sh
fedpkg --release f43 srpm && mock -r fedora-43-x86_64 --addrepo https://download.copr.fedorainfracloud.org/results/flawlessmedia/av-rpm/fedora-43-x86_64/ --resultdir result_foobar foobar*.src.rpm
```

# Tips n Tricks

## Listing files in a package via dnf
```sh
dnf repoquery --files foo-package
```

## Finding which packages match a specific pkgconfig

```sh
dnf provides 'pkgconfig(ffnvcodec)'
```


## References:
* https://docs.fedoraproject.org/en-US/package-maintainers/Installing_Packager_Tools/
* https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_1_banner/
* https://docs.fedoraproject.org/en-US/packaging-guidelines/Meson/
* http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html

