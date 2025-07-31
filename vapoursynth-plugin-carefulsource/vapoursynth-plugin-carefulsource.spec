Name:           vapoursynth-plugin-carefulsource
Version:        5
Release:        %autorelease
Summary:        Image source plugin for VapourSynth

License:        None
URL:            https://github.com/wwww-wwww/carefulsource
Source0:        https://github.com/wwww-wwww/carefulsource/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(lcms2) pkgconfig(libpng) pkgconfig(libjpeg)

%description
%summary

%prep
%autosetup -n carefulsource-%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libcarefulsource.so

%changelog
%autochangelog
