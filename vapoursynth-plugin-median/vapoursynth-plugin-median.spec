Name:           vapoursynth-plugin-median
Version:        4
Release:        %autorelease
Summary:        Generates a pixel-by-pixel median of several clips.

License:        None
URL:            https://github.com/dubhater/vapoursynth-median
Source0:        https://github.com/dubhater/vapoursynth-median/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-median-%{version}

%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libmedian.so

%changelog
%autochangelog
