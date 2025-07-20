Name:           vapoursynth-plugin-awarpsharp2
Version:        4
Release:        %autorelease
Summary:        Sharpens by warping plugin for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-awarpsharp2
Source0:        https://github.com/dubhater/vapoursynth-awarpsharp2/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-awarpsharp2-%{version}

%build
%meson --libdir %{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libawarpsharp2.so

%changelog
%autochangelog
