%define commit 665c8fbd8e078868c3509f17a53b2970fad83520

Name:           obuparse
Version:        0^20250828g665c8fb
Release:        1%{?dist}
Summary:        A simple and portable single file AV1 OBU parser written in mostly C89 with a tiny bit of C99, with a permissive license.

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
%{_libdir}/libobuparse.so*

%files devel
%doc README.md
%{_includedir}/obuparse.h
%{_libdir}/libobuparse.so*


%changelog
* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com> - 0^20250828g665c8fb-1
- Upgrade to 20250828 commit.
