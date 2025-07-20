Name:           vapoursynth-plugin-dpid
Version:        6
Release:        %autorelease
Summary:        Rapid, Detail-Preserving Image Downscaler for VapourSynth 

License:        BSD-3
URL:            https://github.com/WolframRhodium/VapourSynth-dpid
Source0:        https://github.com/WolframRhodium/VapourSynth-dpid/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n VapourSynth-dpid-r%{version}

%build
cd Source
%meson
%meson_build

%install
cd Source
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/vapoursynth/libdpid.so

%changelog
%autochangelog
