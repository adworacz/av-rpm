Name:           obuparse
Version:        0^20250608g8acb519
Release:        %autorelease
Summary:        A simple and portable single file AV1 OBU parser written in mostly C89 with a tiny bit of C99, with a permissive license.

%define commit 8acb5193a64e5c8281c9f22805f75f044f5931f7

License:        ISC
URL:            https://github.com/dwbuiten/obuparse
Source0:        https://github.com/dwbuiten/obuparse/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
#Requires:       
Patch:          fix-makefile-lib64.patch

%description
%{summary}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
%make_build


%install
export PREFIX=%{buildroot}%{_prefix}
# Default "make install" installs static artifacts, which we don't want,
# so we override it.
%{__make} install-shared DESTDIR=%{?buildroot} INSTALL="%{__install} -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license LICENSE
%doc README.md
%{_libdir}/libobuparse.so
%{_libdir}/libobuparse.so.1

%files devel
%doc README.md
%{_includedir}/obuparse.h
%{_libdir}/libobuparse.so
%{_libdir}/libobuparse.so.1


%changelog
%autochangelog
