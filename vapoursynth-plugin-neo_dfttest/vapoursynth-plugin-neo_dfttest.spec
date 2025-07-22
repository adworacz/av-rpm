Name:           vapoursynth-plugin-neo_dfttest
Version:        8^20250524ge359539
Release:        %autorelease
Summary:        A 2D/3D frequency domain denoiser for VapourSynth

%define commit  e359539659e0d72359d269bf49cf09892d9e37ca

License:        GPL-2.0
URL:            https://github.com/HomeOfAviSynthPlusEvolution/neo_dfttest
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_dfttest/archive/%{commit}.tar.gz
Patch0:         0001-fix-version.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tbb)

# Builds with SSE/AVX instructions, so NEON doesn't work at this time.
ExclusiveArch: x86_64

%description
%{summary}

%prep
%autosetup -n neo_DFTTest-%{commit} -p1


%build
# Remove the vs headers, since we want it to use the system headers.
rm -r "include/"vapour*

%cmake
%cmake_build

%install
%{__install} -pDm755 %{__cmake_builddir}/libneo-dfttest.so %{buildroot}%{_libdir}/vapoursynth/libneo-dfttest.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libneo-dfttest.so


%changelog
%autochangelog
