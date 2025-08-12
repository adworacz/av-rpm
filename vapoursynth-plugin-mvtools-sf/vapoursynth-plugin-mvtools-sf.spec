%define commit  38dadba1ef853a90fab51aa886c455587173630b

Name:           vapoursynth-plugin-mvtools-sf
Version:        9^20200818g38dadba
Release:        %autorelease
Summary:        Vapoursynth plugin for motion compensation and stuff (float support)

License:        None
URL:            https://github.com/IFeelBloated/vapoursynth-mvtools-sf
Source0:        https://github.com/IFeelBloated/vapoursynth-mvtools-sf/archive/%{commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(fftw3f)

%description
%{summary}

%prep
%autosetup -n vapoursynth-mvtools-sf-%{commit}


%build
sed 's|vapoursynth-mvtools-sf|mvtools_sf|g' -i "meson.build"

%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc README.md
%{_libdir}/vapoursynth/libmvtools_sf.so

%changelog
%autochangelog
