
# Setup

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

