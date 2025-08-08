Name:           cpgcdemux
Version:        0.1
Release:        %autorelease
Summary:        Linux console port of PgcDemux. A tool for demuxing a DVD PGC/VID/CELL.

License:        LGPL-2.1
URL:            http://cdslow.org.ru/en/cpgcdemux
Source0:        http://cdslow.org.ru/files/cpgcdemux/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}


%build
%cmake
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license lgpl-2.1.txt
%doc README.txt
%doc ReadmePgcDemux.txt 
%{_bindir}/*

%changelog
%autochangelog
