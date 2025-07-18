Name:           vapoursynth-plugin-placebo
Version:        3.2.4
Release:        %autorelease

%define libp2p_commit f52c14efc88c53317d00f45610a9e42030ba8a21

Summary:        libplacebo-based debanding, scaling and color mapping plugin for VapourSynth 

License:        LGPL-2.1
URL:            https://github.com/sgt0/vs-placebo
Source0:        https://github.com/sgt0/vs-placebo/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/sekrit-twc/libp2p/archive/%{libp2p_commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(dovi) pkgconfig(libplacebo)

%description
%summary

%prep
%autosetup -n vs-placebo-%{version} -D -a 1

# Rename p2p directory to match bestsource meson.build's expectations.
rm -rf libp2p && mv libp2p-%{libp2p_commit} libp2p

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libvs_placebo.so


%changelog
%autochangelog
