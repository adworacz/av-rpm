%global debug_package %{nil}

%define commit  b25561316887c2b0bbc8b364dda6c07fee2cc85a

Name:           vapoursynth-plugin-vship-cuda
Version:        3.0.1^20250813gb255613
Release:        %autorelease
Summary:        (CUDA version) VapourSynth plugin for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
#Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz
Source0:        https://github.com/Line-fr/Vship/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

Provides:       vapoursynth-plugin-vship
Conflicts:      vapoursynth-plugin-vship

%description
%summary

%prep
%autosetup -n Vship-%{commit}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%make_build buildcudaall

%install
# %%make_install
%{__install} -p -Dm 755 vship.so %{buildroot}%{_libdir}/vapoursynth/vship.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/vship.so

%changelog
%autochangelog
