Name:           vapoursynth-plugin-dedot
Version:        1
Release:        %autorelease
Summary:        Temporal rainbow and dotcrawl filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-dedot
Source0:        https://github.com/dubhater/vapoursynth-dedot/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-dedot-%{version}

%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libdedot.so

%changelog
%autochangelog
