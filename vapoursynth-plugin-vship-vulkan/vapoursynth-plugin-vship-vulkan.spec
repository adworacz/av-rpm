%global debug_package %{nil}

Name:           vapoursynth-plugin-vship-vulkan
Version:        5.0.1
Release:        1%{?dist}
Summary:        (Vulkan version) VapourSynth plugin for GPU-accelerated visual fidelity metrics, focusing on SSIMULACRA2 & Butteraugli. 

License:        GPL-3.0
URL:            https://codeberg.org/Line-fr/Vship
Source0:        https://codeberg.org/Line-fr/Vship/archive/v%{version}.tar.gz

BuildRequires:  clang vulkan-headers
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(vulkan)

Provides:       vapoursynth-plugin-vship libvship
Conflicts:      vapoursynth-plugin-vship libvship

%description
%summary

%prep
%autosetup -n vship

%build
%make_build buildVulkan

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
* Mon May 25 2026 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 5.0.1-1
- Update to 5.0.1

* Sun Jan 18 2026 adworacz <561689+adworacz@users.noreply.github.com> - 4.1.0-1
- Update to 4.1.0 and Codeberg

* Thu Dec 18 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.2-1
- Update to 4.0.2

* Fri Dec 05 2025 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.1-1
- Update to 4.0.1

