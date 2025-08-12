%global debug_package %{nil}

# Reference: https://src.fedoraproject.org/rpms/rocfft/blob/f42/f/rocfft.spec
%global toolchain rocm
 
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

Name:           ffvship-hip
Version:        3.0.1
Release:        %autorelease
Summary:        (AMD HIP version) Standalone CLI for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-fix-makefile.patch

BuildRequires:  gcc-c++ rocm-hip-devel rocm-cmake rocm-rpm-macros hipfft-devel
BuildRequires:  pkgconfig(ffms2) pkgconfig(zimg)

Provides:       ffvship

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n Vship-%{version} -p1

%build
%make_build buildFFVSHIPall

%install
# %%make_install
%{__install} -pDm755 FFVship %{buildroot}%{_bindir}/FFVship

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
