Name:           vapoursynth-plugin-sangnom
Version:        42
Release:        %autorelease
Summary:        sangnom filter for VapourSynth

License:        MIT
URL:            https://github.com/dubhater/vapoursynth-sangnom
Source0:        https://github.com/dubhater/vapoursynth-sangnom/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-sangnom-r%{version}

%build
%meson --libdir %{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libsangnom.so

%changelog
%autochangelog
