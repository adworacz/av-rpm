# Akarin claims this plugin is much faster when built
# with clang
# https://github.com/AmusementClub/VapourSynth-FFT3DFilter/releases/tag/R2.AC3
%global toolchain clang

Name:           vapoursynth-plugin-fft3dfilter
Version:        2.AC3^20240814ge105871
Release:        %autorelease
Summary:        FFT3DFilter for VapourSynth

%define commit  e1058717e066ef7390575a17f0c884a80189abf2

License:        GPL
URL:            https://github.com/AmusementClub/VapourSynth-FFT3DFilter
Source0:        https://github.com/AmusementClub/VapourSynth-FFT3DFilter/archive/%{commit}.tar.gz

BuildRequires:  meson clang
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

%description
%summary

%prep
%autosetup -n VapourSynth-FFT3DFilter-%{commit}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%{_libdir}/vapoursynth/libfft3dfilter.so

%changelog
%autochangelog
