Name:           vapoursynth-plugin-dfttest
Version:        7
Release:        %autorelease
Summary:        DFTTest filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-DFTTest/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

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
%autochangelog
