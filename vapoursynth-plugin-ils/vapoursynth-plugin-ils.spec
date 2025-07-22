Name:           vapoursynth-plugin-ils
Version:        0^20230706gaab4783
Release:        %autorelease
Summary:        CUDA implentation of real time iterative least squares smoothing for VapourSynth

%define commit  aab4783b3acdf4eb05a64a99bcfc104f9e1eac3a

License:        MIT
URL:            https://github.com/WolframRhodium/VapourSynth-ILS
Source0:        https://github.com/WolframRhodium/VapourSynth-ILS/archive/%{commit}.tar.gz

BuildRequires:  cmake gcc-c++ cuda-toolkit
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-ILS-%{commit}

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
export PATH="$PATH:/usr/local/cuda/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_SKIP_RPATH=ON \
        -DVAPOURSYNTH_INCLUDE_DIRECTORY="$(pkg-config --cflags vapoursynth | sed 's|-I||g')" \
        -DCMAKE_CUDA_FLAGS='--threads 0 --use_fast_math -fpic' \
        -DCMAKE_CUDA_ARCHITECTURES=all-major
%cmake_build

%install
%{__install} -pDm755 %{__cmake_builddir}/libils.so %{buildroot}%{_libdir}/vapoursynth/libils.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libils.so

%changelog
%autochangelog
