Name:           vapoursynth-plugin-vsfpng
Version:        1.0
Release:        %autorelease
Summary:        fpng for VapourSynth 

License:        LGPL-2.1
URL:            https://github.com/Mikewando/vsfpng
Source0:        https://github.com/Mikewando/vsfpng/archive/refs/tags/%{version}.tar.gz
Patch0:         0001-fix-meson.patch

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%{summary}

%prep
%autosetup -n vsfpng-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libfpng.so

%changelog
%autochangelog
