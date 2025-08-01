Name:           vapoursynth-plugin-ctmf
Version:        5
Release:        %autorelease
Summary:        Constant time median filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-CTMF
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-CTMF/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-CTMF-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libctmf.so

%changelog
%autochangelog
