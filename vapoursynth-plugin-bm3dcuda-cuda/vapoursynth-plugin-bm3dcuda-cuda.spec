Name:           vapoursynth-plugin-bm3dcuda-cuda
Version:        2.15
Release:        1%{?dist}
Summary:        BM3D denoising filter for VapourSynth, CUDA version.

#%%define commit  200250b3864d50f0eb5f738686d06d9db3b1fbd3

License:        GPL-2.0
URL:            https://github.com/WolframRhodium/VapourSynth-BM3DCUDA/
Source0:        https://github.com/WolframRhodium/VapourSynth-BM3DCUDA/archive/refs/tags/R%{version}.tar.gz
# Source0:        https://github.com/WolframRhodium/VapourSynth-BM3DCUDA/archive/%{commit}.tar.gz

BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-BM3DCUDA-R%{version}
#%%autosetup -n VapourSynth-BM3DCUDA-%{commit}


%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%cmake \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir}/vapoursynth \
        -DCMAKE_BUILD_TYPE=Release \
        -DVAPOURSYNTH_INCLUDE_DIRECTORY="$(pkg-config --cflags vapoursynth | sed 's|-I||g')" \
        -DUSE_NVRTC_STATIC=ON \
        -DENABLE_CPU=OFF \
        -DENABLE_CUDA=ON \
        -DCMAKE_CUDA_FLAGS='--threads 0 --use_fast_math -fpic' \
        -DCMAKE_CUDA_ARCHITECTURES=all-major
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libbm3dcuda.so
%{_libdir}/vapoursynth/libbm3dcuda_rtc.so

%changelog
* Tue Oct 21 2025 adworacz <561689+adworacz@users.noreply.github.com> - 2.15-1
- Upgrade to v2.15
