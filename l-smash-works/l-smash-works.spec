Name:           l-smash-works
Version:        1253.0.0.0
Release:        %autorelease
Summary:        A source plugin for AviSynth and VapourSynth

License:        LGPL
URL:            https://github.com/HomeOfAviSynthPlusEvolution/L-SMASH-Works
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/L-SMASH-Works/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblsmash)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  obuparse-devel
Requires:       vapoursynth-libs
Requires:       l-smash
Requires:       obuparse

%description
%summary

%prep
%autosetup -n L-SMASH-Works-%{version}


%build
pushd VapourSynth
%meson
%meson_build
popd


%install
pushd VapourSynth
%meson_install
popd
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license VapourSynth/LICENSE
%{_libdir}/vapoursynth/libvslsmashsource.so


%changelog
* Wed Jun 25 2025 Austin Dworaczyk Wiltshire <adw.wiltshire@gmail.com>
- Initial commit.
