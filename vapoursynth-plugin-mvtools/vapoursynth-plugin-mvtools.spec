Name:           vapoursynth-plugin-mvtools
Version:        24^20240906ge516e90
Release:        %autorelease
Summary:        Vapoursynth plugin for motion compensation and stuff

%define commit  e516e90f9618a20c2dc06be05935d2abbb5f691b

License:        GPL
URL:            https://github.com/dubhater/vapoursynth-mvtools
Source0:        https://github.com/dubhater/vapoursynth-mvtools/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(fftw3f)
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
%autochangelog
