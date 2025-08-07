%define commit  363d4e93f34730e9ef7ad8c74fda7e8c58802289

Name:           vapoursynth-plugin-mlrt-trt
Version:        15.13g20250806g363d4e9
Release:        %autorelease
Summary:        Efficient CPU/GPU ML Runtimes for VapourSynth (CUDA TensorRT)

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-mlrt
Source0:        https://github.com/AmusementClub/vs-mlrt/archive/%{commit}.tar.gz
Patch0:         0001-fix-cmake.patch

BuildRequires:  cmake gcc-c++ cuda-toolkit tensorrt-devel libnvinfer-devel
BuildRequires:  pkgconfig(vapoursynth)

# Apparently Nvidia doesn't provide tensorrt or nvinfer libraries for other arches.
ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n vs-mlrt-%{commit} -p1

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

cd vstrt

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DVAPOURSYNTH_INCLUDE_DIRECTORY="$(pkg-config --cflags vapoursynth | sed 's|-I||g')" \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir}/vapoursynth \

%cmake_build

%install
cd vstrt
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvstrt.so

%changelog
%autochangelog
