Name:           vapoursynth-plugin-descale
Version:        11
Release:        %autorelease
Summary:        VapourSynth plugin to undo upscaling 

License:        LGPL-3.0
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-descale
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-descale/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%{summary}

%prep
%autosetup -n vapoursynth-descale-r%{version}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libdescale.so


%changelog
%autochangelog
