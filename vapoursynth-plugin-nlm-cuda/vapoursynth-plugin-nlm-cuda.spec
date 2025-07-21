Name:           vapoursynth-plugin-nlm-cuda
Version:        1
Release:        %autorelease
Summary:        Non-local means denoise filter in CUDA, drop-in replacement of the KNLMeansCL for VapourSynth

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-nlm-cuda
Source0:        https://github.com/AmusementClub/vs-nlm-cuda/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vs-nlm-cuda-%{version}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_CUDA_FLAGS='--threads 0 --use_fast_math -fpic' \
        -DCMAKE_CUDA_ARCHITECTURES=all-major
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvsnlm_cuda.so

%changelog
%autochangelog
