Name:           vapoursynth-plugin-removegrain-sf
Version:        5
Release:        %autorelease
Summary:        RemoveGrain Single Precision

License:        WTFPL
URL:            https://github.com/IFeelBloated/RGSF
Source0:        https://github.com/IFeelBloated/RGSF/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
RemoveGrain package for single (actually double) precision float processing.

%prep
%autosetup -n RGSF-r%{version}


%build
%{set_build_flags}

%{__cxx} -c -std=gnu++11 %{build_cxxflags} -fPIC -I. $(pkg-config --cflags vapoursynth) -o Clense.o Clense.cpp
%{__cxx} -c -std=gnu++11 %{build_cxxflags} -fPIC -I. $(pkg-config --cflags vapoursynth) -o RGVS.o RGVS.cpp
%{__cxx} -c -std=gnu++11 %{build_cxxflags} -fPIC -I. $(pkg-config --cflags vapoursynth) -o RemoveGrain.o RemoveGrain.cpp
%{__cxx} -c -std=gnu++11 %{build_cxxflags} -fPIC -I. $(pkg-config --cflags vapoursynth) -o Repair.o Repair.cpp
%{__cxx} -c -std=gnu++11 %{build_cxxflags} -fPIC -I. $(pkg-config --cflags vapoursynth) -o VerticalCleaner.o VerticalCleaner.cpp

%{__cxx} %{build_cxxflags} %{build_ldflags} -shared -fPIC -o librgsf.so Clense.o RGVS.o RemoveGrain.o Repair.o VerticalCleaner.o

%install
%{__install} -p -Dm 755 librgsf.so %{buildroot}%{_libdir}/vapoursynth/librgsf.so

%files
%{_libdir}/vapoursynth/librgsf.so

%changelog
%autochangelog
