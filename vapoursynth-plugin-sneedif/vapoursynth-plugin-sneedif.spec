Name:           vapoursynth-plugin-sneedif
Version:        3
Release:        %autorelease
Summary:        S.N.E.E.D.I.F. Setsugen No Ensemble of Edge Directed Interpolation Functions 

License:        None
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-SNEEDIF
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/vapoursynth-SNEEDIF/archive/refs/tags/R%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(OpenCL)
Requires:       vapoursynth-libs

Patch0: 0001-fix-meson-build.patch

# Only seems buildable on x86_64...
ExclusiveArch: x86_64

%description
%{summary}


%prep
%autosetup -n vapoursynth-SNEEDIF-R%{version}


%build
%meson --libdir=%{_libdir}/vapoursynth
%meson_build


%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libsneedif.so

%changelog
%autochangelog
