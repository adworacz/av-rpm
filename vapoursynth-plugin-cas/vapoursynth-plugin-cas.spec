Name:           vapoursynth-plugin-cas
Version:        2
Release:        %autorelease
Summary:        Contrast Adaptive Sharpening filter for VapourSynth

License:        MIT
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-CAS
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-CAS/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-CAS-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libcas.so

%changelog
%autochangelog
