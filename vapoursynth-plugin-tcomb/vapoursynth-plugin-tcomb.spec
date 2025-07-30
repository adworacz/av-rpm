Name:           vapoursynth-plugin-tcomb
Version:        4
Release:        %autorelease
Summary:        Temporal comb filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-tcomb
Source0:        https://github.com/dubhater/vapoursynth-tcomb/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-tcomb-%{version}

%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libtcomb.so

%changelog
%autochangelog
