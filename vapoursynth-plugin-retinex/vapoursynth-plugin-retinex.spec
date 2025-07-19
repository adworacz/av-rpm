Name:           vapoursynth-plugin-retinex
Version:        4
Release:        %autorelease
Summary:        Retinex algorithm filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Retinex
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Retinex/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-Retinex-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libretinex.so

%changelog
%autochangelog
