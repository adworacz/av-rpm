Name:   vapoursynth-plugin-edgemasks
Version:    3.1
Release:    2%{?dist}
Summary:    EdgeMasks filter for VapourSynth

License:    MIT
URL:        https://github.com/HolyWu/VapourSynth-EdgeMasks/
Source0:    https://github.com/HolyWu/VapourSynth-EdgeMasks/archive/refs/tags/r%{version}.tar.gz

BuildRequires: meson gcc-c++ pkgconfig(vapoursynth)

# https://github.com/HolyWu/VapourSynth-EdgeMasks/issues/5
ExclusiveArch: x86_64

%description
%{summary}


%prep
%autosetup -n VapourSynth-EdgeMasks-r%{version}


%build
%meson
%meson_build


%install
%meson_install



%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/edgemasks.so


%changelog
* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 3.1-2
- Limit to x86_64 for now

* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 3.1-1
- Initial commit


