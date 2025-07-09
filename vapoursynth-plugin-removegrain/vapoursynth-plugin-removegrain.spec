Name:           vapoursynth-plugin-removegrain
Version:        R1^20221028g89ca38a
Release:        %autorelease
Summary:        VapourSynth port of RemoveGrain and Repair plugins from Avisynth

%define commit 89ca38a6971e371bdce2778291393258daa5f03b

License:        MIT
URL:            https://github.com/vapoursynth/vs-removegrain
Source0:        https://github.com/vapoursynth/vs-removegrain/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  vapoursynth-devel
Requires:       vapoursynth-libs

%description
%{summary}

%prep
%autosetup -n vs-removegrain-%{commit}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc docs/rgvs.rst
%{_libdir}/vapoursynth/libremovegrain.so


%changelog
%autochangelog
