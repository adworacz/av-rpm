Name:           vapoursynth-plugin-bilateralgpu
Version:        10^20231110ga2198f1
Release:        %autorelease
Summary:        Bilateral filter in CUDA and SYCL for VapourSynth. 

%define commit  a2198f12f998f582eb703e62385f7dac3389c4eb

License:        MIT
URL:            https://github.com/WolframRhodium/VapourSynth-BilateralGPU
Source0:        https://github.com/WolframRhodium/VapourSynth-BilateralGPU/archive/%{commit}.tar.gz

# Requires nvidia cuda toolkit repo:
# https://developer.download.nvidia.com/compute/cuda/repos/fedora41/x86_64
# Ideally try and limit this to just the -devel libraries (cuda-libraries-devel, cuda-nvrtc-devel-cuda-driver-devel?)
BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

# Nvidia only offers CUDA repos for Fedora 41 so far.
ExclusiveOS: fc41
ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n VapourSynth-BilateralGPU-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/bilateralgpu.so


%changelog
%autochangelog
