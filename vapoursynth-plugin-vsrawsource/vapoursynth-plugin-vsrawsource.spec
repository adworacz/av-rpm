Name:           vapoursynth-plugin-vsrawsource
Version:        20191105AC
Release:        %autorelease
Summary:        Raw format video reader for VapourSynth

%define real_version 20191105-AC

License:        LGPL-2.1
URL:            https://github.com/AmusementClub/vsrawsource
Source0:        https://github.com/AmusementClub/vsrawsource/archive/refs/tags/%{real_version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vsrawsource-%{real_version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE.LGPLv2.1
%doc readme.rst
%{_libdir}/vapoursynth/libvsrawsource.so

%changelog
%autochangelog
