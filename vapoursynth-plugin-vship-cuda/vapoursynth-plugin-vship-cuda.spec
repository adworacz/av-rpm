%global debug_package %{nil}

Name:           vapoursynth-plugin-vship-cuda
Version:        3.0.1
Release:        %autorelease
Summary:        (CUDA version) VapourSynth plugin for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

Provides:       vapoursynth-plugin-vship
Conflicts:      vapoursynth-plugin-vship

%description
%summary

%prep
%autosetup -n Vship-%{version}

%build
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
