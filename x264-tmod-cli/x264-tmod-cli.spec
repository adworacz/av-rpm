Name:           x264-tmod-cli
Version:        r3214
Release:        %autorelease
Summary:        (CLI only) x264 with tmod patches

License:        GPL-2.0
URL:            https://github.com/jpsdr/x264
Source0:        https://github.com/jpsdr/x264/archive/refs/tags/r3214.tar.gz

BuildRequires:  gcc-c++ nasm
BuildRequires:  pkgconfig(libswscale) pkgconfig(libavformat)
BuildRequires:  gpac-devel ffms2-devel
BuildRequires:  l-smash-devel

%description
%summary

%prep
%autosetup -n x264-%{version}

%build
%configure \
        --enable-pic \
        --enable-lto \
        --disable-avs \
        --disable-audio \
        --disable-lsmash \

%make_build

%install
%{__make} DESTDIR=%{buildroot} install-cli

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%{_bindir}/*

%changelog
%autochangelog
