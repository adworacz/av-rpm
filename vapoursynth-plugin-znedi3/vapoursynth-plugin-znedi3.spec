%global debug_package %{nil}

%define commit  47e7698f481577ac325567bb553134520939f1ff
%define vsxx_commit de38f0e128c85782494ae00565698a2b25e87869
%define graphengine_commit f06d7cb4d589ea4657f01b13613efb7437c8ecda

Name:           vapoursynth-plugin-znedi3
Version:        2.1^20250517g47e7698
Release:        %autorelease

Summary:        nnedi3 filter for vapoursynth

License:        None
URL:            https://github.com/sekrit-twc/znedi3
Source0:        https://github.com/sekrit-twc/znedi3/archive/%{commit}.tar.gz
Source1:        https://github.com/sekrit-twc/vsxx/archive/%{vsxx_commit}.tar.gz
Source2:        https://github.com/sekrit-twc/graphengine/archive/%{graphengine_commit}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

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
ls
%{__install} -pDm755 vsznedi3.so %{buildroot}%{_libdir}/vapoursynth/libvsznedi3.so
%{__install} -pDm755 nnedi3_weights.bin %{buildroot}%{_datadir}/nnedi3/nnedi3_weights.bin

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license gpl2.txt
%doc readme.rst
%{_libdir}/vapoursynth/libvsznedi3.so
%{_datadir}/nnedi3/nnedi3_weights.bin


%changelog
%autochangelog
