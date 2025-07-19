Name:           vapoursynth-plugin-nnedi3cl
Version:        8
Release:        %autorelease
Summary:        NNEDI3CL filter for VapourSynth

License:        MIT
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-NNEDI3CL
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-NNEDI3CL/archive/refs/tags/r%{version}.tar.gz

BuildRequires:  meson gcc-c++ boost-devel
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(OpenCL)

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
%{_datadir}/NNEDI3CL/nnedi3_weights.bin

%changelog
%autochangelog
