Name:           vapoursynth-plugin-bm3d
Version:        9
Release:        %autorelease
Summary:        BM3D denoising filter for VapourSynth

License:        MIT
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-BM3D
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-BM3D/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

%description
%summary

%prep
%autosetup -n VapourSynth-BM3D-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libbm3d.so

%changelog
%autochangelog
