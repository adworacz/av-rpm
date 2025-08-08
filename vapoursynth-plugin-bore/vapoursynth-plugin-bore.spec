%global debug_package %{nil}

Name:           vapoursynth-plugin-bore
Version:        1.0.0
Release:        %autorelease
Summary:        Border deringing filter for VapourSynth

License:        GPL-2.0
URL:            https://github.com/OpusGang/bore
Source0:        https://github.com/OpusGang/bore/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(gsl)

%description
%summary

%prep
%autosetup -n bore-%{version}

%build
%meson -Dlibtype=vapoursynth 
%meson_build

%install
%{__install} -p -Dm 755 %{_vpath_builddir}/libbore.so %{buildroot}%{_libdir}/vapoursynth/libbore.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libbore.so

%changelog
%autochangelog
