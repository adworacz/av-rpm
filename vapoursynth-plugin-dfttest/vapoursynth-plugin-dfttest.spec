%define commit  bc5e0186a7f309556f20a8e9502f2238e39179b8

Name:           vapoursynth-plugin-dfttest
Version:        7^20220415gbc5e018
Release:        3%{?dist}
Summary:        DFTTest filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest
#Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest/archive/refs/tags/r%{version}.tar.gz
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest/archive/%{commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

Requires: pkgconfig(fftw3f)

%description
%summary

%prep
#%%autosetup -n VapourSynth-DFTTest-r%{version}
%autosetup -n VapourSynth-DFTTest-%{commit}

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
* Tue Dec 23 2025 adworacz <561689+adworacz@users.noreply.github.com> - 7^20220415gbc5e018-3
- Update to latest commit to fix fftw3 threads dependency

* Mon Dec 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 7-2
- Add direct dependency on fftw3

