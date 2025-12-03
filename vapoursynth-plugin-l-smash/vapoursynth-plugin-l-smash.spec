Name:           vapoursynth-plugin-l-smash
Version:        1266.0.0.0
Release:        2%{?dist}
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
* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com> - 1266.0.0.0-2
- Bump to rebuild

* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com> - 1266.0.0.0-1
- Upgrade to 1266

* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com> - 1262.0.0.0-1
- Upgrade to 1262

* Wed Jun 25 2025 adworacz <561689+adworacz@users.noreply.github.com>
- Initial commit.
