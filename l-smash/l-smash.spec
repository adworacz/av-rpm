Name:           l-smash
Version:        2.18.0^20241028g30270d0
Release:        %autorelease
Summary:        Vimeo L-SMASH

%define commit 30270d0d8b551b36b6f46c43bd3ffe997f13e157

License:        ISC
URL:            https://github.com/vimeo/l-smash
Source0:        https://github.com/vimeo/l-smash/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  obuparse-devel
Patch:          allow-fedora-configure-options.patch

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
# Note that --enable-debug is set to ensure debug symbols are generated
# so that a corresponding debuginfo package can be properly created.
# Alternatively we could set the global "debug_package" to nill.
# Ref: https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/#_useless_or_incomplete_debuginfo_packages_due_to_other_reasons
%configure --disable-static --enable-debug
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license LICENSE
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so


%changelog
%autochangelog
