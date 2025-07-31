Name:           vapoursynth-plugin-vsnoise
Version:        4
Release:        %autorelease
Summary:        Generates film like noise for VapourSynth

License:        GPL-3.0
URL:            https://github.com/wwww-wwww/vs-noise
Source0:        https://github.com/wwww-wwww/vs-noise/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vs-noise-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libaddnoise.so

%changelog
%autochangelog
