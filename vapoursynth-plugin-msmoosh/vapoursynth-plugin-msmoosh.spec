Name:           vapoursynth-plugin-msmoosh
Version:        1.1
Release:        %autorelease
Summary:        MSharpen and MSmooth plugin for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-msmoosh
Source0:        https://github.com/dubhater/vapoursynth-msmoosh/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-msmoosh-%{version}

%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libmsmoosh.so

%changelog
%autochangelog
