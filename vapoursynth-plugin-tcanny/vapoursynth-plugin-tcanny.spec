Name:           vapoursynth-plugin-tcanny
Version:        14
Release:        %autorelease
Summary:        TCanny filter for VapourSynth

License:        MIT
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-TCanny
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-TCanny/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-TCanny-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libtcanny.so

%changelog
%autochangelog
