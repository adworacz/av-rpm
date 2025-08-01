Name:           vapoursynth-plugin-yadifmod
Version:        10.1
Release:        %autorelease
Summary:        yadifmod filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Yadifmod
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Yadifmod/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-Yadifmod-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libyadifmod.so

%changelog
%autochangelog
