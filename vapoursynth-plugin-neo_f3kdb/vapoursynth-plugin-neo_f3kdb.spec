Name:           vapoursynth-plugin-neo_f3kdb
Version:        10
Release:        %autorelease
Summary:        Deband filter for VapourSynth

License:        GPL-3.0
URL:            https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  cmake gcc-c++  
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tbb)

%description
%{summary}

%prep
%autosetup -n neo_f3kdb-r%{version}

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
