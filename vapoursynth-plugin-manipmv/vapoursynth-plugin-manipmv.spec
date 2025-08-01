%global debug_package %{nil}

Name:           vapoursynth-plugin-manipmv
Version:        1.2.0
Release:        %autorelease
Summary:        A vapoursynth plugin to do potentially useful things with motion vectors that have already been generated. 

License:        LGPL-2.1
URL:            https://github.com/Mikewando/manipulate-motion-vectors
Source0:        https://github.com/Mikewando/manipulate-motion-vectors/archive/refs/tags/%{version}.tar.gz

BuildRequires:  zig >= 0.14.0
BuildRequires:  pkgconfig(vapoursynth)

%description
%{summary}


%prep
%autosetup -n manipulate-motion-vectors-%{version}


%build
zig build -Doptimize=ReleaseFast -Dtarget=native -Dcpu=baseline --build-id=sha1 --summary all --verbose

%install
%{__install} -pDm 755 zig-out/lib/libmanipmv.so %{buildroot}%{_libdir}/vapoursynth/libmanipmv.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libmanipmv.so

%changelog
%autochangelog
