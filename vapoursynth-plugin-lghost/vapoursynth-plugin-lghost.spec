Name:           vapoursynth-plugin-lghost
Version:        1
Release:        %autorelease
Summary:        lghost filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-LGhost
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-LGhost/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-LGhost-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/liblghost.so

%changelog
%autochangelog
