Name:           vapoursynth-plugin-deblock
Version:        7.1
Release:        1%{?dist}
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
* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 7.1-1
- Update to 7.1
