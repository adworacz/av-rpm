Name:           vapoursynth-plugin-knlmeanscl
Version:        1.1.1^20230105gca424fa
Release:        %autorelease
Summary:        An optimized OpenCL implementation of the Non-local means de-noising algorithm

%define commit  ca424fa91d1e16ec011f7db9c3ba0d1e76ed7850

License:        None
URL:            https://github.com/Khanattila/KNLMeansCL
Source0:        https://github.com/Khanattila/KNLMeansCL/archive/%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(OpenCL)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n KNLMeansCL-%{commit}


%build
%meson
%meson_build


%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libknlmeanscl.so

%changelog
%autochangelog
