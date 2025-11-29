Name:   vapoursynth-plugin-awarp
Version:    2
Release:    1%{?dist}
Summary:    AWarp filter for VapourSynth

License:    MIT
URL:        https://github.com/HolyWu/VapourSynth-AWarp/
Source0:    https://github.com/HolyWu/VapourSynth-AWarp/archive/refs/tags/r%{version}.tar.gz

BuildRequires: meson gcc-c++ pkgconfig(vapoursynth)

%description
%{summary}


%prep
%autosetup -n VapourSynth-AWarp-r%{version}


%build
%meson
%meson_build


%install
%meson_install



%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/awarp.so


%changelog
* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 2-2
- Initial commit


