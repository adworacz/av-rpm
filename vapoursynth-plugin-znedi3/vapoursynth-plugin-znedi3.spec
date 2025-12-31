%global debug_package %{nil}

%define commit  47e7698f481577ac325567bb553134520939f1ff
%define vsxx_commit de38f0e128c85782494ae00565698a2b25e87869
%define graphengine_commit f06d7cb4d589ea4657f01b13613efb7437c8ecda

Name:           vapoursynth-plugin-znedi3
Version:        2.1^20250517g47e7698
Release:        2%{?dist}

Summary:        nnedi3 filter for vapoursynth

License:        None
URL:            https://github.com/sekrit-twc/znedi3
Source0:        https://github.com/sekrit-twc/znedi3/archive/%{commit}.tar.gz
Source1:        https://github.com/sekrit-twc/vsxx/archive/%{vsxx_commit}.tar.gz
Source2:        https://github.com/sekrit-twc/graphengine/archive/%{graphengine_commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

Requires:   vapoursynth-plugin-nnedi3-weights

%description
%summary

%prep
%autosetup -n znedi3-%{commit}
%setup -n znedi3-%{commit} -T -D -a 1
%setup -n znedi3-%{commit} -T -D -a 2

rm -rf vsxx && mv vsxx-%{vsxx_commit} vsxx
rm -rf graphengine && mv graphengine-%{graphengine_commit} graphengine

%build
%make_build

%install
%{__install} -pDm755 vsznedi3.so %{buildroot}%{_libdir}/vapoursynth/libvsznedi3.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license gpl2.txt
%doc readme.rst
%{_libdir}/vapoursynth/libvsznedi3.so


%changelog
* Wed Dec 31 2025 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 2.1^20250517g47e7698-2
- Depend on separate weights package to prevent collisions

