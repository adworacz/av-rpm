# Reference: https://src.fedoraproject.org/rpms/rocfft/blob/f42/f/rocfft.spec
%global toolchain rocm
 
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

Name:           vapoursynth-plugin-dfttest2-hip
Version:        7
Release:        %autorelease
Summary:        DFTTest re-implemetation for VapourSynth (HIP version)

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-dfttest2
Source0:        https://github.com/AmusementClub/vs-dfttest2/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake gcc-c++ rocm-hip-devel rocm-cmake rocm-rpm-macros hipfft-devel
BuildRequires:  pkgconfig(vapoursynth)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n vs-dfttest2-%{version}

%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DENABLE_CPU=OFF \
        -DENABLE_GCC=OFF \
        -DENABLE_CUDA=OFF \
        -DENABLE_HIP=ON
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libdfttest2_hip.so
%{_libdir}/vapoursynth/libdfttest2_hiprtc.so

%changelog
%autochangelog
