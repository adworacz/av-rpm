Name:           wobbly
Version:        9
Release:        %autorelease
Summary:        IVTC assistant for VapourSynth, similar to Yatta 

License:        None
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/Wobbly
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/Wobbly/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)
# GUI requirements
BuildRequires:  qt5-qtbase-devel

%description
%summary

%prep
%autosetup -n Wobbly-%{version}

%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
