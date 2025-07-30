%define commit 889fd9ca913867bfacbd5ac2b7ea1edaf8154889

Name:           vapoursynth-plugin-decross
Version:        2
Release:        %autorelease
Summary:        Spatio-temporal derainbox filter for VapourSynth.

License:        None
URL:            https://github.com/dubhater/vapoursynth-decross
Source0:        https://github.com/dubhater/vapoursynth-decross/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-decross-%{commit}

%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libdecross.so

%changelog
%autochangelog
