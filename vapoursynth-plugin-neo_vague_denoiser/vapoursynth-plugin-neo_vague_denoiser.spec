%define commit  5716b33ec4e50d92171d01a47da8dff173acca97

Name:           vapoursynth-plugin-neo_vague_denoiser
Version:        10^20231214g5716b33
Release:        %autorelease
Summary:        A wavelet based denoiser filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfAviSynthPlusEvolution/neo_vague_denoiser
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_vague_denoiser/archive/%{commit}.tar.gz
Patch0:         0001-fix-cmake.patch

BuildRequires:  cmake gcc-c++  
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tbb)

ExclusiveArch:  x86_64

%description
%{summary}

%prep
%autosetup -n neo_Vague_Denoiser-%{commit}

%build
%cmake
%cmake_build

%install
%{__install} -pDm755 %{__cmake_builddir}/libneo-vague-denoiser.so %{buildroot}%{_libdir}/vapoursynth/libneo-vague-denoiser.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libneo-vague-denoiser.so


%changelog
%autochangelog
