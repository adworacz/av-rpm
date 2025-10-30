%global debug_package %{nil}

# Reference: https://src.fedoraproject.org/rpms/rocfft/blob/f42/f/rocfft.spec
%global toolchain rocm
 
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2/-Xarch_host -mtls-dialect=gnu2/')

Name:           vapoursynth-plugin-vship-hip
Version:        3.0.1
Release:        %autorelease
Summary:        (AMD HIP version) VapourSynth plugin for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ rocm-hip-devel rocm-cmake rocm-rpm-macros hipfft-devel
BuildRequires:  pkgconfig(vapoursynth)

Provides:       vapoursynth-plugin-vship
Conflicts:      vapoursynth-plugin-vship

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n Vship-%{version}

%build
%make_build buildall

%install
# %%make_install
%{__install} -p -Dm 755 vship.so %{buildroot}%{_libdir}/vapoursynth/vship.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/vship.so

%changelog
%autochangelog
