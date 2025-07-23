Name:           vapoursynth-plugin-smoothuv
Version:        3
Release:        %autorelease
Summary:        smoothuv filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-smoothuv
Source0:        https://github.com/dubhater/vapoursynth-smoothuv/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

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
# Compiling with -O3 unrolls said loops properly, so it's a kind of workaround.
# 
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vapoursynth-plugin-smoothuv-git#n34
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=98927
# https://stackoverflow.com/questions/12913451/mm-extract-epi8-intrinsic-that-takes-a-non-literal-integer-as-argument
export CXXFLAGS="$CXXFLAGS -fpeel-loops"

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
