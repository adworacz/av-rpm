Name:           vapoursynth-plugin-dctfilter
Version:        3.1A
Release:        %autorelease
Summary:        Renewed DCT filter for VapourSynth, with arbitrary sized DCT

License:        MIT
URL:            https://github.com/AmusementClub/VapourSynth-DCTFilter
Source0:        https://github.com/AmusementClub/VapourSynth-DCTFilter/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

%description
%summary

%prep
%autosetup -n VapourSynth-DCTFilter-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libdctfilter.so

%changelog
%autochangelog
