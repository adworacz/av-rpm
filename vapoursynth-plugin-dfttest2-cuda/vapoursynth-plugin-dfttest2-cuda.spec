#%%define commit  3fe2c1a68460022d9196ddb2a8200baedaba67c1

Name:           vapoursynth-plugin-dfttest2-cuda
Version:        10
Release:        1%{?dist}
Summary:        DFTTest re-implemetation for VapourSynth (CUDA version)

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-dfttest2
Source0:        https://github.com/AmusementClub/vs-dfttest2/archive/refs/tags/v%{version}.tar.gz
# Source0:        https://github.com/AmusementClub/vs-dfttest2/archive/%{commit}.tar.gz

BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
#%%autosetup -n vs-dfttest2-%{commit}
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
        -DENABLE_HIP=OFF \
        -DCMAKE_CUDA_FLAGS='--threads 0 --use_fast_math' \
        -DCMAKE_CUDA_ARCHITECTURES=all-major
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
* Wed Jan 21 2026 adworacz <561689+adworacz@users.noreply.github.com> - 10-1
- Update to v10

* Wed Jan 21 2026 adworacz <561689+adworacz@users.noreply.github.com> - 9-1
- Update to v9

* Tue Oct 21 2025 adworacz <561689+adworacz@users.noreply.github.com> - 8-1
- Upgrade to v8

