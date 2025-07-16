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
BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n VapourSynth-BilateralGPU-%{commit}

%build
# Set various CUDA env vars.
# https://www.if-not-true-then-false.com/2018/install-nvidia-cuda-toolkit-on-fedora/#fedora-4140-1
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

# Force compiling with PIE to prevent errors like:
# main.cu.o: relocation R_X86_64_32 against `.bss' can not be used when making a PIE object; recompile with -fPIE
# export CFLAGS="$CFLAGS -fPIE"
# export CXXFLAGS="$CXXFLAGS -fPIE"

# I think this can also be the compute capabilities, so 5.0+, as in 50, 60, 70...
# Separated by semicolons per https://cmake.org/cmake/help/latest/envvar/CUDAARCHS.html#envvar:CUDAARCHS
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vapoursynth-plugin-bilateralgpu-git#n39

# Using an env var since using a commandline option doesn't seem to be working for some reason.
# https://cmake.org/cmake/help/latest/envvar/CUDAFLAGS.html#envvar:CUDAFLAGS
export CUDAFLAGS="--threads 0 --use_fast_math -pic"

%cmake -DCMAKE_CUDA_ARCHITECTURES='50;60;70;80;90;100;120'
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
