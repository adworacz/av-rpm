# Use version components because the extracted tarball doesn't exactly match
# the version name (uses a `-` instead of a `+` for the patch num)
%define api 165
%define subversion 3223
%define patchnum 18

Name:           x264-patman
Version:        0.%{api}.%{subversion}+%{patchnum}
Release:        1%{?dist}
Summary:        (CLI only) x264 with Patman's patches to support Vapoursynth, extended Y4M and improved progress bar

License:        GPL-2.0
URL:            https://github.com/Patman86
Source0:        https://github.com/Patman86/x264-Mod-by-Patman/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc-c++ nasm
BuildRequires:  pkgconfig(libswscale) pkgconfig(libavformat) pkgconfig(vapoursynth)
BuildRequires:  gpac-devel ffms2-devel l-smash-devel

%description
%summary

%prep
%autosetup -n x264-Mod-by-Patman-0.%{api}.%{subversion}-%{patchnum}

%build
chmod +x configure
%configure \
        --enable-pic \
        --enable-lto \
        --disable-avs \

%make_build

%install
# TODO: Potentially install the cli under a different name to prevent collisions, like x264-patman?
%{__make} DESTDIR=%{buildroot} install-cli

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%{_bindir}/*

%changelog
* Thu Feb 05 2026 adworacz <561689+adworacz@users.noreply.github.com> - 0.165.3223+18-1
- Initial commit

