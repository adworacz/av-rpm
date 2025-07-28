Name:           vapoursynth-plugin-neo_f3kdb
Version:        10^20250723g37cd2fc
Release:        %autorelease
Summary:        Deband filter for VapourSynth

%define commit  37cd2fc7c068c94ce98ce158a5d4105e8a27b326

License:        GPL-3.0
URL:            https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb
#Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb/archive/refs/tags/r%{version}.tar.gz
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb/archive/%{commit}.tar.gz

BuildRequires:  cmake gcc-c++  
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tbb)

%description
%{summary}

%prep
#%%autosetup -n neo_f3kdb-r%{version}
%autosetup -n neo_f3kdb-%{commit}

%build
%cmake
%cmake_build

%install
%{__install} -pDm755 %{__cmake_builddir}/libneo-f3kdb.so %{buildroot}%{_libdir}/vapoursynth/libneo-f3kdb.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libneo-f3kdb.so


%changelog
%autochangelog
