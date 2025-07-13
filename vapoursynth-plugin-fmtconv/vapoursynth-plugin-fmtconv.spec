Name:           vapoursynth-plugin-fmtconv
Version:        30^20250531g259b702e
Release:        %autorelease
Summary:        Format conversion tools for Vapoursynth

%define commit  259b702e4e3c1e2fc6d7b2c8e83d95b612519e89

License:        WTFPL
URL:            https://gitlab.com/EleonoreMizo/fmtconv/
Source0:        https://gitlab.com/EleonoreMizo/fmtconv/-/archive/%{commit}/fmtconv-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description


%prep
%autosetup -n fmtconv-%{commit}


%build
pushd build/unix
./autogen.sh
%configure --disable-static --libdir %{_libdir}/vapoursynth
%make_build
popd


%install
pushd build/unix
%make_install
popd 
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license doc/license.txt
%doc doc/*
%{_libdir}/vapoursynth/libfmtconv.so


%changelog
%autochangelog
