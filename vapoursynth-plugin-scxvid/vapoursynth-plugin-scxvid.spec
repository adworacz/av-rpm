Name:           vapoursynth-plugin-scxvid
Version:        1
Release:        %autorelease
Summary:        Scene change detection plugin for VapourSynth, using xvid 

License:        None
URL:            https://github.com/dubhater/vapoursynth-scxvid
Source0:        https://github.com/dubhater/vapoursynth-scxvid/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool xvidcore-devel
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-scxvid-%{version}

%build
./autogen.sh
%configure --disable-static --libdir %{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libscxvid.so

%changelog
%autochangelog
