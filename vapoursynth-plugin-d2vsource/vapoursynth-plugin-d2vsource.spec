Name:           vapoursynth-plugin-d2vsource
Version:        1.3
Release:        %autorelease
Summary:        D2V parser and decoder for VapourSynth

License:        LGPL-2.1
URL:            https://github.com/dwbuiten/d2vsource
Source0:        https://github.com/dwbuiten/d2vsource/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n d2vsource-%{version}


%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%files
%doc README
%{_libdir}/vapoursynth/libd2vsource.so


%changelog
%autochangelog
