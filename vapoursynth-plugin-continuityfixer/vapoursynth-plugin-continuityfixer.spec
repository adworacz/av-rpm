%global debug_package %{nil}

Name:           vapoursynth-plugin-continuityfixer
Version:        7
Release:        %autorelease

Summary:        Continuity Fixer port for Vapoursynth 

License:        None
URL:            https://github.com/MonoS/VS-ContinuityFixer
Source0:        https://github.com/MonoS/VS-ContinuityFixer/archive/refs/tags/V%{version}.tar.gz
#https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vapoursynth-plugin-continuityfixer-git
Patch0:         0001-makefile.patch

BuildRequires:  gcc-c++ make
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VS-ContinuityFixer-%{version} -p1

%build
%make_build

%install
%{__install} -pDm755 libcontinuityfixer.so %{buildroot}%{_libdir}/vapoursynth/libcontinuityfixer.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libcontinuityfixer.so


%changelog
%autochangelog
