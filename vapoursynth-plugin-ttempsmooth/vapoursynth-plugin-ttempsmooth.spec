Name:           vapoursynth-plugin-ttempsmooth
Version:        4.1
Release:        %autorelease
Summary:        TTempSmooth filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-ttempsmooth
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-ttempsmooth/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-TTempSmooth-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libttempsmooth.so

%changelog
%autochangelog
