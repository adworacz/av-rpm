%global debug_package %{nil}

Name:           vapoursynth-plugin-manipmv
Version:        1.2.1
Release:        %autorelease
Summary:        A vapoursynth plugin to do potentially useful things with motion vectors that have already been generated. 

License:        LGPL-2.1
URL:            https://github.com/Mikewando/manipulate-motion-vectors
Source0:        https://github.com/Mikewando/manipulate-motion-vectors/archive/refs/tags/%{version}.tar.gz

BuildRequires:  zig >= 0.14.0
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(vapoursynth)

%description
%{summary}


%prep
%autosetup -n manipulate-motion-vectors-%{version}


%build
zig build %{_zig_general_options} %{_zig_project_options} --release=fast

%install
%{__install} -pDm 755 zig-out/lib/libmanipmv.so %{buildroot}%{_libdir}/vapoursynth/libmanipmv.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libmanipmv.so

%changelog
%autochangelog
