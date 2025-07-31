%define real_version Pre_01

Name:           vapoursynth-plugin-eedi2cuda
Version:        0.1
Release:        %autorelease
Summary:        Enhanced Edge Directed Interpolation implemented in CUDA 

License:        GPL-2.0
URL:            https://github.com/hooke007/VapourSynth-EEDI2CUDA
Source0:        https://github.com/hooke007/VapourSynth-EEDI2CUDA/archive/refs/tags/%{real_version}.tar.gz
Patch0:         0001-fix-cmake.patch

BuildRequires:  cmake gcc-c++ cuda-toolkit boost-devel
BuildRequires:  pkgconfig(vapoursynth)

# WIP - needs to fix boost "sync" includes.
# Ref: https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=foosynth-plugin-eedi2cuda-git

%description
%summary

%prep
%autosetup -n VapourSynth-EEDI2CUDA-%{real_version} -p1

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DENABLE_AVISYNTHPLUS_BINDING=OFF \
        -DCMAKE_CUDA_FLAGS='--threads 0 --use_fast_math -fpic' \
        -DCMAKE_CUDA_ARCHITECTURES=all-major
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libeedi2cuda.so

%changelog
%autochangelog
