%global debug_package %{nil}

#%%define commit  15f1a6d2364f536d75cdc2c3c1798c75f807defd

Name:           vapoursynth-plugin-resize2
Version:        0.3.4
Release:        1%{?dist}
Summary:        vapoursynth resize2

License:        None
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-resize2
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-resize2/archive/refs/tags/%{version}.tar.gz
# Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-resize2/archive/%{commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

# Required to download submodules
BuildRequires:  git 

%description
%{summary}

%prep
%autosetup -n vapoursynth-resize2-%{version}
# %%autosetup -n vapoursynth-resize2-%{commit}

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
* Sun Dec 28 2025 adworacz <561689+adworacz@users.noreply.github.com> - 0.3.4-1
- Update to 0.3.4

