#%%define     commit  badbc42e58327cd9f2a41c6a88431d02abcc4ffd

Name:       vapoursynth-plugin-eedi3vk
Version:    1.2
Release:    1%{?dist}
Summary:    Renewed EEDI3 filter for VapourSynth, implemented in Vulkan

License:    GPL-3.0
URL:        https://github.com/Sunflower-Dolls/Vapoursynth-EEDI3VK
Source0:    https://github.com/Sunflower-Dolls/Vapoursynth-EEDI3VK/archive/refs/tags/R%{version}.tar.gz
# Source0:    https://github.com/Sunflower-Dolls/Vapoursynth-EEDI3VK/archive/%{commit}.tar.gz

BuildRequires: meson gcc-c++ vulkan-headers vulkan-volk-devel git glslc
BuildRequires: pkgconfig(vapoursynth)

%description
%{summary}

%prep
%autosetup -n Vapoursynth-EEDI3VK-R%{version}
#%%autosetup -n Vapoursynth-EEDI3VK-%{commit}

meson subprojects download


%build
%meson
%meson_build

%install
%meson_install


%files
#%%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/*.so


%changelog
* Mon Dec 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 1.2-1
- Add eedi3vk 1.2


