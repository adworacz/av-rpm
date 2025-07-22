Name:           vapoursynth-plugin-dfttest2-cpu
Version:        7
Release:        %autorelease
Summary:        DFTTest re-implemetation for VapourSynth (CPU + GCC versions)

%define vcl_commit a0a33986fb1fe8a5b7844e8a1b1f197ce19af35d

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-dfttest2
Source0:        https://github.com/AmusementClub/vs-dfttest2/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/vectorclass/version2/archive/%{vcl_commit}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n vs-dfttest2-%{version} -D -a 1

rm -rf cpu_source/vectorclass && mv version2-%{vcl_commit} cpu_source/vectorclass 


%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DENABLE_CPU=ON \
        -DENABLE_GCC=ON \
        -DENABLE_CUDA=OFF \
        -DENABLE_HIP=OFF
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libdfttest2_cpu.so
%{_libdir}/vapoursynth/libdfttest2_gcc.so

%changelog
%autochangelog
