Name:           vapoursynth-plugin-frfun7
Version:        2
Release:        %autorelease
Summary:        frfun7 filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-frfun7
Source0:        https://github.com/dubhater/vapoursynth-frfun7/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-frfun7-%{version}

%build
%meson --libdir %{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libfrfun7.so

%changelog
%autochangelog
