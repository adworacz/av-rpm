#%%define commit  ec0d9473fc6652a22068966ddfef097253dd0256

Name:           vapoursynth-plugin-neo_dfttest
Version:        11
Release:        1%{?dist}
Summary:        A 2D/3D frequency domain denoiser for VapourSynth

License:        GPL-2.0
URL:            https://github.com/HomeOfAviSynthPlusEvolution/neo_dfttest
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_dfttest/archive/refs/tags/r%{version}.tar.gz
#Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_dfttest/archive/%{commit}.tar.gz
Patch0:         0001-fix-version.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tbb)

# Builds with SSE/AVX instructions, so NEON doesn't work at this time.
ExclusiveArch: x86_64

%description
%{summary}

%prep
%autosetup -n neo_DFTTest-r%{version} -p1
#%%autosetup -n neo_DFTTest-%{commit} -p1


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
* Thu Dec 18 2025 adworacz <561689+adworacz@users.noreply.github.com> - 11-1
- Update to r11

* Thu Dec 04 2025 adworacz <561689+adworacz@users.noreply.github.com> - 9^20251203gec0d947-1
- Update to r9, commit ec0d947

