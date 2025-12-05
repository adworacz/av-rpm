%global debug_package %{nil}

# Reference: https://src.fedoraproject.org/rpms/rocfft/blob/f42/f/rocfft.spec
%global toolchain rocm
 
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2/-Xarch_host -mtls-dialect=gnu2/')

#%%define commit  b25561316887c2b0bbc8b364dda6c07fee2cc85a

Name:           ffvship-hip
Version:        4.0.1
Release:        1%{?dist}
Summary:        (AMD HIP version) Standalone CLI for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz
# Source0:        https://github.com/Line-fr/Vship/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ rocm-hip-devel rocm-cmake rocm-rpm-macros hipfft-devel
BuildRequires:  pkgconfig(ffms2) pkgconfig(zimg)

Requires: libvship

Provides:       ffvship
Conflicts:      ffvship

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n Vship-%{version}
#%%autosetup -n Vship-%{commit}

%build
%make_build buildFFVSHIP

%install
# %%make_install
%{__install} -pDm755 FFVship %{buildroot}%{_bindir}/FFVship

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
* Fri Dec 05 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.1-1
- Update to 4.0.1

