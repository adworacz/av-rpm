Name:           vapoursynth-plugin-neo_fft3d
Version:        11^20250524g780dcdf
Release:        %autorelease
Summary:        A 3D frequency domain denoiser for VapourSynth

%define commit  780dcdfb477c3e5195b1418b15a8b7eed89507ac

License:        GPL-2.0
URL:            https://github.com/HomeOfAviSynthPlusEvolution/neo_FFT3D
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_FFT3D/archive/%{commit}.tar.gz
Patch0:         0001-fix-version.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tbb)

%description
%{summary}

%prep
%autosetup -n neo_FFT3D-%{commit} -p1


%build
# Remove the vs headers, since we want it to use the system headers.
rm -r "include/"vapour*

%cmake
%cmake_build

%install
%{__install} -pDm755 %{__cmake_builddir}/libneo-fft3d.so %{buildroot}%{_libdir}/vapoursynth/libneo-fft3d.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libneo-fft3d.so


%changelog
%autochangelog
