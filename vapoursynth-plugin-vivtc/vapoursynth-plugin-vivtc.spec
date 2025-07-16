Name:           vapoursynth-plugin-vivtc
Version:        1^20221029g4ac661d
Release:        %autorelease
Summary:        Field matcher and decimation filter for VapourSynth similar to TIVTC 

%define commit  4ac661d78eaf8b5ab7c5dd2d05c81234fe9aaca8

License:        LGPL-2.1
URL:            https://github.com/vapoursynth/vivtc
Source0:        https://github.com/vapoursynth/vivtc/archive/%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary


%prep
%autosetup -n vivtc-%{commit}


%build
%meson
%meson_build


%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%{_libdir}/vapoursynth/libvivtc.so


%changelog
%autochangelog
