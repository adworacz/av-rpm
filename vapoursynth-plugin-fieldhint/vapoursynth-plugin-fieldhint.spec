Name:           vapoursynth-plugin-fieldhint
Version:        3
Release:        %autorelease
Summary:        fieldhint plugin for VapourSynth

License:        None
URL:            https://github.com/dubhater/vapoursynth-fieldhint
Source0:        https://github.com/dubhater/vapoursynth-fieldhint/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-fieldhint-%{version}

%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libfieldhint.so

%changelog
%autochangelog
