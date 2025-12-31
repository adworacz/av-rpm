Name:           vapoursynth-plugin-nnedi3cl
Version:        8
Release:        2%{?dist}
Summary:        NNEDI3CL filter for VapourSynth

License:        MIT
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-NNEDI3CL
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-NNEDI3CL/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++ boost-devel
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(OpenCL)

Requires:   vapoursynth-plugin-nnedi3-weights

%description
%summary

%prep
%autosetup -n VapourSynth-NNEDI3CL-r%{version}

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libnnedi3cl.so

%changelog
* Wed Dec 31 2025 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 8-2
- Depend on separate weights package to prevent collisions

