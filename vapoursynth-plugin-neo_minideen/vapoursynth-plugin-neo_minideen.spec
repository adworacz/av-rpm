Name:           vapoursynth-plugin-neo_minideen
Version:        11
Release:        1%{?dist}
Summary:        Spatial denoising filter - thresholded average

License:        MIT
URL:            https://github.com/HomeOfAviSynthPlusEvolution/MiniDeen
Source0:        https://github.com/HomeOfAviSynthPlusEvolution/MiniDeen/archive/refs/tags/r%{version}.tar.gz
Patch0:         0001-fix-version.patch

BuildRequires:  gcc-c++ cmake
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n MiniDeen-r%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
#%%cmake_install
ls -r %{__cmake_builddir}
%{__install} -Dm755 %{__cmake_builddir}/libneo-minideen.so %{buildroot}%{_libdir}/vapoursynth/libneo-minideen.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libneo-minideen.so

%changelog
* Thu Jul 09 2026 adworacz <561689+adworacz@users.noreply.github.com> - 11-1
- Build r11

