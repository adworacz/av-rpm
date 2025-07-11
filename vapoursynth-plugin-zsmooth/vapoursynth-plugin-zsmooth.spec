%global debug_package %{nil}

Name:           vapoursynth-plugin-zsmooth
Version:        0.12
Release:        %autorelease
Summary:        Cross-platform, cross-architecture video smoothing functions for Vapoursynth, written in Zig

License:        MIT
URL:            https://github.com/adworacz/zsmooth
Source0:        https://github.com/adworacz/zsmooth/archive/refs/tags/%{version}.tar.gz

BuildRequires:  zig
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n zsmooth-%{version}


%build
# TODO: Create subpackages for different cpus
# %zig_prep
# %zig_build
zig build -Doptimize=ReleaseFast -Dtarget=native -Dcpu=baseline --build-id=sha1 --summary all --verbose

%install
%{__install} -pDm 755 zig-out/lib/libzsmooth.so %{buildroot}%{_libdir}/vapoursynth/libzsmooth.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libzsmooth.so

%changelog
%autochangelog
