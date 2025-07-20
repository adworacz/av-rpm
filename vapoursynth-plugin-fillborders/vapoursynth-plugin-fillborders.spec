Name:           vapoursynth-plugin-fillborders
Version:        2^20240818g215a2a8
Release:        %autorelease
Summary:        Motion mask plugin for VapourSynth

%define commit  215a2a87be51495c5fad4b4cab1bdd8f5a0aaf7f

License:        None
URL:            https://github.com/dubhater/vapoursynth-fillborders
Source0:        https://github.com/dubhater/vapoursynth-fillborders/archive/%{commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-fillborders-%{commit}

%build
%meson --libdir=%{_libdir}/vapoursynth/
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libfillborders.so

%changelog
%autochangelog
