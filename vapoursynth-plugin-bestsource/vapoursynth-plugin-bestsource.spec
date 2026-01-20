Name:           vapoursynth-plugin-bestsource
Version:        16
Release:        1%{?dist}

%define libp2p_commit 1e3818bd7277165819f659d410873fe5dab37af6 

Summary:        A super great audio/video source and FFmpeg wrapper for Vapoursynth

License:        MIT
URL:            https://github.com/vapoursynth/bestsource
Source0:        https://github.com/vapoursynth/bestsource/archive/refs/tags/R%{version}.tar.gz
Source1:        https://github.com/sekrit-twc/libp2p/archive/%{libp2p_commit}.tar.gz

Patch0:         0001-remove-avisynth.patch

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%summary

%prep
%autosetup -n bestsource-R%{version} -D -a 1

# Rename p2p directory to match bestsource meson.build's expectations.
rm -rf libp2p && mv libp2p-%{libp2p_commit} libp2p

%build
# Setup default_library so that we produce a single, self-contained library that we can place inside 
# the vapoursynth plugin directory.
# vs-plugin-build does the same thing: https://github.com/Stefan-Olt/vs-plugin-build/blob/main/plugins/bs.json#L1046
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove the static artifacts, pkgconfig, and header files since this isn't a *-devel package.
#find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.pc' -exec rm -f {} ';'
find %{buildroot} -name '*.h' -exec rm -f {} ';'

%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/*.so
#%%{_includedir}/bestsource/*


%changelog
* Fri Jan 09 2026 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 16-1
- Update to R16

* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 15-1
- Update to R15
