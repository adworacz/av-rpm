Name:           vapoursynth-plugin-motionmask
Version:        2^20210719ged86b06
Release:        %autorelease
Summary:        Motion mask plugin for VapourSynth

%define commit  ed86b06688c2db1b05d7026f66a2574e64c9e69e

License:        None
URL:            https://github.com/dubhater/vapoursynth-motionmask
Source0:        https://github.com/dubhater/vapoursynth-motionmask/archive/%{commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-motionmask-%{commit}

%build
%meson --libdir=%{_libdir}/vapoursynth/
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libmotionmask.so

%changelog
%autochangelog
