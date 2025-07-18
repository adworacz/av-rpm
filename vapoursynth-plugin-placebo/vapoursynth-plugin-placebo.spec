Name:           vapoursynth-plugin-placebo
Version:        3.2.4
Release:        %autorelease

%define libp2p_commit f52c14efc88c53317d00f45610a9e42030ba8a21
%define libplacebo_commit 02f4f9862395d0379a0ec654345f52daf81e1aee

Summary:        libplacebo-based debanding, scaling and color mapping plugin for VapourSynth 

License:        MIT
URL:            https://github.com/sgt0/vs-placebo
Source0:        https://github.com/sgt0/vs-placebo/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/sekrit-twc/libp2p/archive/%{libp2p_commit}.tar.gz
Source2:        https://github.com/haasn/libplacebo/archive/%{libplacebo_commit}.tar.gz
# TODO - bring in all of libplacebo's deps too...

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(dovi) pkgconfig(libunwind) pkgconfig(shaderc) pkgconfig(spirv)

%description
%summary

%prep
%autosetup -n vs-placebo-%{version} -D -a 1
%setup -n vs-placebo-%{version} -D -a 2

# Rename p2p directory to match bestsource meson.build's expectations.
rm -rf libp2p && mv libp2p-%{libp2p_commit} libp2p
rm -rf subprojects/libplacebo && mv libplacebo-%{libplacebo_commit} subprojects/libplacebo

%build
%meson -Dlibplacebo:demos=false -Dlibplacebo:glslang=enabled -Dlibplacebo:d3d11=disabled
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvs_placebo.so


%changelog
%autochangelog
