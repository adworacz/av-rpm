Name:           vapoursynth-plugin-addgrain
Version:        10
Release:        %autorelease
Summary:        AddGrain filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-AddGrain
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-AddGrain/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-AddGrain-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libaddgrain.so

%changelog
%autochangelog
