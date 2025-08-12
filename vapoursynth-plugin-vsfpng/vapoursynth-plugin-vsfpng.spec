%define commit  d2c59bb4e4949a1b747d21f76494705c315b382a

Name:           vapoursynth-plugin-vsfpng
Version:        1.0^20250812gd2c59bb
Release:        %autorelease
Summary:        fpng for VapourSynth 

License:        LGPL-2.1
URL:            https://github.com/Mikewando/vsfpng
#Source0:        https://github.com/Mikewando/vsfpng/archive/refs/tags/%{version}.tar.gz
Source0:        https://github.com/Mikewando/vsfpng/archive/%{commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%{summary}

%prep
# %%autosetup -n vsfpng-%{version}
%autosetup -n vsfpng-%{commit}

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
