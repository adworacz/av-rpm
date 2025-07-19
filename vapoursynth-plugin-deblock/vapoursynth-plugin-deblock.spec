Name:           vapoursynth-plugin-deblock
Version:        6.1
Release:        %autorelease
Summary:        Deblock filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Deblock
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Deblock/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-Deblock-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libdeblock.so

%changelog
%autochangelog
