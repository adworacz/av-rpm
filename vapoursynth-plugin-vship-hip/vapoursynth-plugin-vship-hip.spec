%global debug_package %{nil}

# Reference: https://src.fedoraproject.org/rpms/rocfft/blob/f42/f/rocfft.spec
%global toolchain rocm
 
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2/-Xarch_host -mtls-dialect=gnu2/')

Name:           vapoursynth-plugin-vship-hip
Version:        4.0.2
Release:        1%{?dist}
Summary:        (AMD HIP version) VapourSynth plugin for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://github.com/Line-fr/Vship
Source0:        https://github.com/Line-fr/Vship/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ rocm-hip-devel rocm-cmake rocm-rpm-macros hipfft-devel
BuildRequires:  pkgconfig(vapoursynth)

Provides:       vapoursynth-plugin-vship libvship
Conflicts:      vapoursynth-plugin-vship libvship

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n Vship-%{version}

%build
%make_build buildall

%install
# %%make_install
%{__install} -p -Dm 755 libvship.so %{buildroot}%{_libdir}/libvship.so
%{__mkdir_p} %{buildroot}%{_libdir}/vapoursynth
%{__ln_s} ../libvship.so %{buildroot}%{_libdir}/vapoursynth/libvship.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/libvship.so
%{_libdir}/vapoursynth/libvship.so

%changelog
* Thu Dec 18 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.2-1
- Update to 4.0.2

* Fri Dec 05 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.1-1
- Update to 4.0.1

