# Plugin is significantly faster when compiled with clang instead of gcc
%global toolchain clang

#%define commit  e516e90f9618a20c2dc06be05935d2abbb5f691b
%define vs_commit 76034ba406dbb58e59a79afcf1f59105b107163b

Name:           vapoursynth-plugin-mvtools
Version:        25
Release:        1%{?dist}
Summary:        Vapoursynth plugin for motion compensation and stuff

License:        GPL
URL:            https://github.com/dubhater/vapoursynth-mvtools
#Source0:        https://github.com/dubhatervapoursynth/vapoursynth-mvtools/archive/%{commit}/%{name}-%{version}.tar.gz
Source0:        https://github.com/dubhatervapoursynth/vapoursynth-mvtools/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/vapoursynth/vapoursynth/archive/%{vs_commit}.tar.gz

BuildRequires:  meson nasm clang
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)
Requires:       vapoursynth-libs

%description
%{summary}

%prep
#%%autosetup -n vapoursynth-mvtools-%{commit}
%autosetup -n vapoursynth-mvtools-%{version}
%setup -n vapoursynth-mvtools-%{version} -T -D -a 1

rm -rf vapoursynth && mv vapoursynth-%{vs_commit} vapoursynth


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
* Mon Apr 20 2026 adworacz <561689+adworacz@users.noreply.github.com> - 25-1
- Upgrade to 25

* Mon Jan 26 2026 adworacz <561689+adworacz@users.noreply.github.com> - 24^20240906ge516e90-2
- Compile with clang for performance improvement

