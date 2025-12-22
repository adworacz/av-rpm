Name:           vapoursynth-plugin-dfttest
Version:        7
Release:        2%{?dist}
Summary:        DFTTest filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

Requires: pkgconfig(fftw3f)

%description
%summary

%prep
%autosetup -n VapourSynth-DFTTest-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libdfttest.so

%changelog
* Mon Dec 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 7-2
- Add direct dependency on fftw3

