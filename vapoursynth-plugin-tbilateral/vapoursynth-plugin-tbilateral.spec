Name:           vapoursynth-plugin-tbilateral
Version:        4
Release:        %autorelease
Summary:        Bilateral spatial denoising filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-tbilateral
Source0:        https://github.com/dubhater/vapoursynth-tbilateral/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-tbilateral-%{version}

%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libtbilateral.so

%changelog
%autochangelog
