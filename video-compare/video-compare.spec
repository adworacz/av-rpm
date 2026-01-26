Name:       video-compare
Version:    20260121
Release:    1%{?dist}
Summary:    Split screen video comparison tool using FFmpeg and SDL2 

License:    GPL-2.0
URL:        https://github.com/pixop/video-compare
Source0:    https://github.com/pixop/video-compare/archive/refs/tags/%{version}.tar.gz

BuildRequires: make gcc-c++
BuildRequires: pkgconfig(sdl2) pkgconfig(SDL2_ttf)
BuildRequires: pkgconfig(libavutil) pkgconfig(libavcodec) pkgconfig(libavformat)
BuildRequires: pkgconfig(libavfilter) pkgconfig(libswresample) pkgconfig(libswscale)

%description
%{summary}


%prep
%autosetup


%build
%make_build


%install
%{__install} -Dm755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE.md
%doc README.md
%{_bindir}/*


%changelog
* Mon Jan 26 2026 adworacz <561689+adworacz@users.noreply.github.com> - 20260121-1
- Initial commit



