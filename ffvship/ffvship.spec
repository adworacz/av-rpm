%global debug_package %{nil}

Name:           ffvship
Version:        4.0.1
Release:        2%{?dist}
Summary:        Standalone CLI for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz
# Source0:        https://github.com/Line-fr/Vship/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ libvship
BuildRequires:  pkgconfig(ffms2) pkgconfig(zimg)

Requires: libvship

Provides:       ffvship ffvship-hip = %{version}-%{release} ffvship-cuda = %{version}-%{release}
Conflicts:      ffvship
Obsoletes:      ffvship-hip < 4.0.1-2%{?dist} ffvship-cuda < 4.0.1-2%{?dist}

%description
%summary
Replaces previous ffvship-hip and ffvship-cuda packages since the binary was merged into one and 
a dependency was added on the ROCM/CUDA-specific libvship package instead.

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
* Fri Dec 05 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.1-2
- Remove build limitation on x86_64, as CUDA version supports ARM

* Fri Dec 05 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.1-1
- Update to 4.0.1

