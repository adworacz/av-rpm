Name:           vapoursynth-plugin-bwdif
Version:        4.1
Release:        %autorelease
Summary:        bwdif denoising filter for VapourSynth

License:        MIT
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Bwdif
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Bwdif/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

%description
%summary

%prep
%autosetup -n VapourSynth-Bwdif-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libbwdif.so

%changelog
%autochangelog
