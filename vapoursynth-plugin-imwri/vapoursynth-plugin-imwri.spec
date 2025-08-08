%define commit  da17f01b9581a78ee5b54edf5b6f47d5f8e3d2f5

Name:           vapoursynth-plugin-imwri
Version:        2^20250918gda17f01
Release:        %autorelease
Summary:        imwri image source plugin for VapourSynth

License:        LGPL-2.1
URL:            https://github.com/vapoursynth/vs-imwri
Source0:        https://github.com/vapoursynth/vs-imwri/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(libheif) pkgconfig(libjxl) pkgconfig(libtiff-4) pkgconfig(Magick++)

%description
%{summary}

%prep
%autosetup -n vs-imwri-%{commit}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc docs/imwri.rst
%{_libdir}/vapoursynth/libimwri.so


%changelog
%autochangelog
