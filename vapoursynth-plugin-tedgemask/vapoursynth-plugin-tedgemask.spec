Name:           vapoursynth-plugin-tedgemask
Version:        1
Release:        %autorelease
Summary:        Edge detection filter for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-tedgemask
Source0:        https://github.com/dubhater/vapoursynth-tedgemask/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-tedgemask-%{version}

%build
%meson --libdir=%{_libdir}/vapoursynth/
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libtedgemask.so

%changelog
%autochangelog
