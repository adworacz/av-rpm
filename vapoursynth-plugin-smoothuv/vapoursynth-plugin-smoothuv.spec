# Disable debug packages for smoothuv, as 
# EPEL9 fails to build them for some reason and we 
# don't really need them anyway.
%global debug_package %{nil}

Name:           vapoursynth-plugin-smoothuv
Version:        3
Release:        %autorelease
Summary:        smoothuv filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-smoothuv
Source0:        https://github.com/dubhater/vapoursynth-smoothuv/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

# Project explicitly only supports x86_64
# https://github.com/dubhater/vapoursynth-smoothuv/blob/master/meson.build#L26
ExclusiveArch: x86_64

#TODO: Add RainbowSmooth.py

%description
%summary

%prep
%autosetup -n vapoursynth-smoothuv-%{version}

%build
# Certain loops need to be properly unrolled in order
# for intrinsic code to compile properly, otherwise we get
# "selector must be an integer constant in the range [0, 7]" errors.
#
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vapoursynth-plugin-smoothuv-git#n34
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=98927
# https://stackoverflow.com/questions/12913451/mm-extract-epi8-intrinsic-that-takes-a-non-literal-integer-as-argument
# Force the use of -O2, because EPEL9 uses -O0 (for some damn reason)
export CXXFLAGS="$CXXFLAGS -O2 -fpeel-loops"

%meson --libdir %{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libsmoothuv.so

%changelog
%autochangelog
