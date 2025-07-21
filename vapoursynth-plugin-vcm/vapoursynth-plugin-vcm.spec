Name:           vapoursynth-plugin-vcm
Version:        20220210.AC3
Release:        %autorelease
Summary:        vcm for VapourSynth

%define tag     2022-02-10.AC3

License:        GPL
URL:            https://github.com/AmusementClub/vcm
Source0:        https://github.com/AmusementClub/vcm/archive/refs/tags/%{tag}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

%description
%summary

%prep
%autosetup -n vcm-%{tag}

%build
# Courtesy of AUR: https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vapoursynth-plugin-vcm-git#n37
# Remove included files, since we want to use system libs.
rm -fr VSHelper.h VapourSynth.h
sed -e '/VapourSynth.h/c#include <VapourSynth.h>' \
  -e '/VsHeper.h/c#include <VSHelper.h>' \
  -e '/VSHelper/c#include <VSHelper.h>' \
  -i *.cpp \
  -i *.h

# Ensure that the install steps are enabled.
sed 's|^  #|  |g' -i meson.build

%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvcmod.so

%changelog
%autochangelog
