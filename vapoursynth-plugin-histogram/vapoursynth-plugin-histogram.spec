Name:           vapoursynth-plugin-histogram
Version:        2^20220805gc4861d6
Release:        %autorelease
Summary:        Histogram filter for VapourSynth

%define commit  c4861d63d496fa0eb873a6f949937be8c9c1dc13

License:        None
URL:            https://github.com/dubhater/vapoursynth-histogram
Source0:        https://github.com/dubhater/vapoursynth-histogram/archive/%{commit}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-histogram-%{commit}

%build
./autogen.sh
%configure --disable-static --libdir %{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libhistogram.so

%changelog
%autochangelog
