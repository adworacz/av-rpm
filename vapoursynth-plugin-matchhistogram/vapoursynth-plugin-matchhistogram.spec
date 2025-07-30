Name:           vapoursynth-plugin-matchhistogram
Version:        2
Release:        %autorelease
Summary:        MatchHistogram modifies one clip's histogram to match the histogram of another clip.

License:        None
URL:            https://github.com/dubhater/vapoursynth-matchhistogram
Source0:        https://github.com/dubhater/vapoursynth-matchhistogram/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ meson
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n vapoursynth-matchhistogram-%{version}

%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc readme.rst
%{_libdir}/vapoursynth/libmatchhistogram.so

%changelog
%autochangelog
