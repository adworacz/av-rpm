%global debug_package %{nil}

Name:           vapoursynth-plugin-resize2
Version:        0.3.3
Release:        %autorelease
Summary:        vapoursynth resize2

License:        None
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-resize2
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-resize2/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(vapoursynth)

Requires:       vapoursynth-libs

# https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-resize2/issues/12
Patch0: 0001-remove-no-format.patch
Patch1: 0002-remove-static-linking.patch

%description
%{summary}


%prep
%autosetup -p1 -n vapoursynth-resize2-%{version}

meson subprojects download


%build
%meson
%meson_build

%install
%meson_install


%files
%doc ReadMe.md
%{_libdir}/vapoursynth/libresize2.so

%changelog
%autochangelog
