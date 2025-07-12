%global debug_package %{nil}

Name:           vapoursynth-plugin-vszip
Version:        7
Release:        %autorelease
Summary:        VapourSynth Zig Image Process

License:        MIT
URL:            https://github.com/dnjulek/vapoursynth-zip
Source0:        https://github.com/dnjulek/vapoursynth-zip/archive/refs/tags/R7.tar.gz

BuildRequires:  zig
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n vapoursynth-zip-R%{version}


%build
# TODO: Create subpackages for different cpus
# %zig_prep
# %zig_build
zig build -Doptimize=ReleaseFast -Dtarget=native -Dcpu=baseline --build-id=sha1 --summary all --verbose

%install
%{__install} -pDm 755 zig-out/lib/libvszip.so %{buildroot}%{_libdir}/vapoursynth/libvszip.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvszip.so

%changelog
%autochangelog
