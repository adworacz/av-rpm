# Plugin is significantly faster when compiled with clang instead of gcc
%global toolchain clang

%define commit  e516e90f9618a20c2dc06be05935d2abbb5f691b

Name:           vapoursynth-plugin-mvtools
Version:        24^20240906ge516e90
Release:        2%{?dist}
Summary:        Vapoursynth plugin for motion compensation and stuff

License:        GPL
URL:            https://github.com/dubhater/vapoursynth-mvtools
Source0:        https://github.com/dubhater/vapoursynth-mvtools/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  meson nasm clang
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)
Requires:       vapoursynth-libs

%description
%{summary}

%prep
%autosetup -n vapoursynth-mvtools-%{commit}


%build
# Workaround the fact that mvtools doesn't autoinstall into the vs directory.
%meson --libdir=%{_libdir}/vapoursynth/
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc readme.rst
%{_libdir}/vapoursynth/libmvtools.so

%changelog
* Mon Jan 26 2026 adworacz <561689+adworacz@users.noreply.github.com> - 24^20240906ge516e90-2
- Compile with clang for performance improvement

