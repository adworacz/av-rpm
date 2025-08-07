Name:           vapoursynth-plugin-subtext
Version:        R5^20240527g397b80d
Release:        %autorelease
Summary:        Subtext (subtitle) plugin for VapourSynth

%define commit 397b80d0e9bf6e6ca1c8828e8c2eeffacd9e1938

License:        MIT
URL:            https://github.com/vapoursynth/subtext
Source0:        https://github.com/vapoursynth/subtext/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavutil) pkgconfig(libass)

%description
%{summary}

%prep
%autosetup -n subtext-%{commit}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc docs/subtext.rst
%{_libdir}/vapoursynth/libsubtext.so


%changelog
%autochangelog
