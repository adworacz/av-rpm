Name:           tsMuxer
Version:        2.7.0
Release:        %autorelease
Summary:        tsMuxer is a transport stream muxer for remuxing/muxing elementary

License:        LGPL-2.1
URL:            https://github.com/justdan96/tsMuxer
Source0:        https://github.com/justdan96/tsMuxer/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc-c++ cmake freetype-devel zlib-ng-devel
# GUI requirements
BuildRequires:  qt5-qttools-devel qt5-qtmultimedia-devel

%description
tsMuxer is a transport stream muxer for remuxing/muxing elementary
streams, EVO/VOB/MPG, MKV/MKA, MP4/MOV, TS, M2TS to TS to M2TS.
Supported video codecs H.264/AVC, H.265/HEVC, VC-1, MPEG2. Supported
audio codecs AAC, AC3 / E-AC3(DD+), DTS/ DTS-HD. 

%prep
%autosetup -n %{name}-%{version}



%build
# Fix warnings about CMake 3.1 deprecation.
sed 's|VERSION 3.1|VERSION 3.10|g' -i CMakeLists.txt
sed 's|VERSION 3.1|VERSION 3.10|g' -i libmediation/CMakeLists.txt
sed 's|VERSION 3.1|VERSION 3.10|g' -i tsMuxer/CMakeLists.txt
sed 's|VERSION 3.1|VERSION 3.10|g' -i tsMuxerGUI/CMakeLists.txt

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DTSMUXER_GUI=ON \
    -DTSMUXER_RELEASE=ON \
    -DTSMUXER_VERSION=%{version} \
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%changelog
%autochangelog
