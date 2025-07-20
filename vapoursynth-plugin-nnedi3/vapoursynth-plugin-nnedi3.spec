Name:           vapoursynth-plugin-nnedi3
Version:        12^20240714g82993ff
Release:        %autorelease
Summary:        NNEDI3 filter for VapourSynth

%define commit  82993ff21cf569776fc1a7e5bb60235c00bbeea3

License:        None
URL:            https://github.com/dubhater/vapoursynth-nnedi3
Source0:        https://github.com/dubhater/vapoursynth-nnedi3/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool yasm
BuildRequires:  pkgconfig(vapoursynth)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n vapoursynth-nnedi3-%{commit}

%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libnnedi3.so
%{_datadir}/nnedi3/nnedi3_weights.bin

%changelog
%autochangelog
