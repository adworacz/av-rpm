%global debug_package %{nil}

%define commit  b25561316887c2b0bbc8b364dda6c07fee2cc85a

Name:           ffvship-cuda
Version:        3.0.1^20250813gb255613
Release:        %autorelease
Summary:        (CUDA version) Standalone CLI for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
#Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz
Source0:        https://github.com/Line-fr/Vship/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(ffms2) pkgconfig(zimg)

Provides:       ffvship
Conflicts:      ffvship

%description
%summary

%prep
%autosetup -n Vship-%{commit}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%make_build buildFFVSHIPcudaall

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
