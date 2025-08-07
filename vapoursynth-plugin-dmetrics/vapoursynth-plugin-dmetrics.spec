Name:           vapoursynth-plugin-dmetrics
Version:        1^20250402gadec0f3
Release:        %autorelease
Summary:        Attaches the match metrics calculated by Telecide (decomb package) to frames as properties

%define commit adec0f3cdf76030e71686cea744187b66e22ea0d

License:        GPL-2.0
URL:            https://github.com/vapoursynth/dmetrics
Source0:        https://github.com/vapoursynth/dmetrics/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

%description
%{summary}

%prep
%autosetup -n dmetrics-%{commit}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license Copying
%doc README.md
%{_libdir}/vapoursynth/libdmetrics.so


%changelog
%autochangelog
