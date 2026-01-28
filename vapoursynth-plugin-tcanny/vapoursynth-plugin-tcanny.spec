# Output is broken with GCC, apparently.
# So we use clang
# https://github.com/HomeOfVapourSynthEvolution/VapourSynth-TCanny/issues/14
%global toolchain clang

Name:           vapoursynth-plugin-tcanny
Version:        14
Release:        3%{?dist}
Summary:        TCanny filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-TCanny
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-TCanny/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson clang
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
* Wed Jan 28 2026 adworacz <561689+adworacz@users.noreply.github.com> - 14-3
- Actually include clang in deps

* Wed Jan 28 2026 adworacz <561689+adworacz@users.noreply.github.com> - 14-2
- Compile with clang to workaround gcc bug.

