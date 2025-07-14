Name:           vapoursynth-plugin-eedi2
Version:        7.1
Release:        %autorelease
Summary:        EEDI2 filter for VapourSynth 

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI2
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI2/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n VapourSynth-EEDI2-r%{version}


%build
%meson
%meson_build


%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libeedi2.so

%changelog
%autochangelog
