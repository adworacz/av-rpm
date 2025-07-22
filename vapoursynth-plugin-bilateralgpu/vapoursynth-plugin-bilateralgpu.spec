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
# Ideally try and limit this to just the -devel libraries (cuda-libraries-devel, cuda-nvrtc-devel, cuda-driver-devel?)
# ^Except that nvidia doesn't offer meta-packages for those, only per-version..versions.
BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-BilateralGPU-%{commit}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DUSE_NVRTC_STATIC=ON \
        -DCMAKE_CUDA_FLAGS='--threads 0 --use_fast_math -fpic' \
        -DCMAKE_CUDA_ARCHITECTURES=all-major
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libbilateralgpu.so
%{_libdir}/vapoursynth/libbilateralgpu_rtc.so


%changelog
%autochangelog
