Name:           vapoursynth-plugin-eedi3
Version:        4^20190929gd11bdb3
Release:        %autorelease
Summary:        Renewed EEDI3 filter for VapourSynth (includes OpenCL version)

%define commit  d11bdb37c7a7118cd095b53d9f8fbbac02a06ac0

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI3
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI3/archive/%{commit}.zip

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(OpenCL)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n VapourSynth-EEDI3-%{commit}


%build
%meson
%meson_build


%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libeedi3m.so

%changelog
%autochangelog
