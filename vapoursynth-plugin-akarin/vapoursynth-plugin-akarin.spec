Name:           vapoursynth-plugin-akarin
Version:        1.0.0
Release:        %autorelease
Summary:        Akarin's experimental VapourSynth plugin: (1) an enhanced LLVM-based std.Expr (aka lexpr), Select, PropExpr, Text and Tmpl. (2) DLISR. (3) DLVFX (4) CAMBI.

License:        LGPL-3.0
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/akarin-vapoursynth-plugin
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/akarin-vapoursynth-plugin/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0) 
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}

%prep
%autosetup -n akarin-vapoursynth-plugin-%{version}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libakarin.so


%changelog
* Sat Jun 21 2025 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com>
- Initial package creation.
