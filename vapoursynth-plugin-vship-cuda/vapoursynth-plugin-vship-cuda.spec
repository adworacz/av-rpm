%global debug_package %{nil}

%define commit  b25561316887c2b0bbc8b364dda6c07fee2cc85a

Name:           vapoursynth-plugin-vship-cuda
Version:        4.0.1
Release:        1%{?dist}
Summary:        (CUDA version) VapourSynth plugin for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz
#Source0:        https://github.com/Line-fr/Vship/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

Provides:       vapoursynth-plugin-vship libvship
Conflicts:      vapoursynth-plugin-vship libvship

%description
%summary

%prep
%autosetup -n Vship-%{version}
#%%autosetup -n Vship-%{commit}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%make_build buildcudaall

%install
# %%make_install
%{__install} -p -Dm 755 libvship.so %{buildroot}%{_libdir}/libvship.so
%{__mkdir_p} %{buildroot}%{_libdir}/vapoursynth
%{__ln_s} ../libvship.so %{buildroot}%{_libdir}/vapoursynth/libvship.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/libvship.so
%{_libdir}/vapoursynth/libvship.so

%changelog
* Fri Dec 05 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.1-1
- Update to 4.0.1

