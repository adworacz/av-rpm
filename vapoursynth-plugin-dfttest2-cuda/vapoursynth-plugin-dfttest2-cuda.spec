Name:           vapoursynth-plugin-dfttest2-cuda
Version:        7
Release:        %autorelease
Summary:        DFTTest re-implemetation for VapourSynth (CUDA version)

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-dfttest2
Source0:        https://github.com/AmusementClub/vs-dfttest2/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake gcc-c++ git cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n vs-dfttest2-%{version}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DUSE_NVRTC_STATIC=ON \
        -DENABLE_CPU=OFF \
        -DENABLE_GCC=OFF \
        -DENABLE_CUDA=ON \
        -DENABLE_HIP=OFF
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libdfttest2_cuda.so
%{_libdir}/vapoursynth/libdfttest2_nvrtc.so

%changelog
%autochangelog
