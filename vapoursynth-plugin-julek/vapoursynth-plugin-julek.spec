%define libjxl_commit  e4698c5bc19d106cb4c22344c5d2f818bc915f0e

Name:           vapoursynth-plugin-julek
Version:        3
Release:        %autorelease
Summary:        julek plugin for VapourSynth

License:        MIT
URL:            https://github.com/dnjulek/vapoursynth-julek-plugin
Source0:        https://github.com/dnjulek/vapoursynth-julek-plugin/archive/refs/tags/r%{version}.tar.gz
Source1:        https://github.com/libjxl/libjxl/archive/%{libjxl_commit}.tar.gz
Patch0:         0001-fix-cmake.patch

BuildRequires:  gcc-c++ cmake
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(libjxl) pkgconfig(libhwy)

%description
%summary

%prep
%autosetup -n vapoursynth-julek-plugin-r%{version} -D -a 1

rm -rf thirdparty/libjxl && mv libjxl-%{libjxl_commit} thirdparty/libjxl

%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release \
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libjulek.so

%changelog
%autochangelog
