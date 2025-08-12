
%define commit  562e06dcf21d2aed3fde54b97b9b19e4ca4e335d

Name:           vapoursynth-plugin-edgefixer
Version:        2^20230528g562e06d
Release:        %autorelease

Summary:        Edge fixing plugin for vapoursynth

License:        None
URL:            https://github.com/sekrit-twc/EdgeFixer
Source0:        https://github.com/sekrit-twc/EdgeFixer/archive/%{commit}.tar.gz
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vapoursynth-plugin-edgefixer-git#n28
Patch0:         0001-makefile.patch

BuildRequires:  gcc-c++ make
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n EdgeFixer-%{commit}

%build
%make_build

%install
ls
%{__install} -pDm755 libedgefixer.so %{buildroot}%{_libdir}/vapoursynth/libedgefixer.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libedgefixer.so


%changelog
%autochangelog
