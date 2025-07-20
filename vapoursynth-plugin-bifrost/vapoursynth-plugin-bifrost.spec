Name:           vapoursynth-plugin-bifrost
Version:        3.0
Release:        %autorelease
Summary:        Bifrost plugin for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-bifrost
Source0:        https://github.com/dubhater/vapoursynth-bifrost/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-bifrost-%{version}

%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libbifrost.so

%changelog
%autochangelog
