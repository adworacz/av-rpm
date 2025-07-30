%global debug_package %{nil}

%define commit  6d4c31ff5ce84ec9aab57300e5eeac6b963c8192 

Name:           vapoursynth-plugin-dvdsrc2
Version:        0.1^20250725g6d4c31f
Release:        %autorelease
Summary:        DVD source plugin for VapourSynth

License:        None
URL:            https://github.com/jsaowji/dvdsrc2
Source0:        https://github.com/jsaowji/dvdsrc2/archive/%{commit}.tar.gz

BuildRequires:  cargo rust cargo-rpm-macros liba52-devel libmpeg2-devel libdvdread-devel
Requires:       vapoursynth-libs

%description
%summary


%prep
%autosetup -n dvdsrc2-%{commit}


%build
%{__cargo} build --release --locked
ls target/release

%install
install -Dpm 0755 target/release/libdvdsrc2.so %{buildroot}%{_libdir}/vapoursynth/libdvdsrc2.so


%files
%doc README.txt
%{_libdir}/vapoursynth/libdvdsrc2.so



%changelog
%autochangelog
