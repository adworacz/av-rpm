%global debug_package %{nil}

Name:           vapoursynth-plugin-zsmooth
Version:        0.15
Release:        1%{?dist}
Summary:        Cross-platform, cross-architecture video smoothing functions for Vapoursynth, written in Zig

License:        MIT
URL:            https://github.com/adworacz/zsmooth
Source0:        https://github.com/adworacz/zsmooth/archive/refs/tags/%{version}.tar.gz

BuildRequires:  zig >= 0.15.2
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n zsmooth-%{version}


%build
zig build %{_zig_general_options} %{_zig_project_options} --release=fast

%install
%{__install} -pDm 755 zig-out/lib/libzsmooth.so %{buildroot}%{_libdir}/vapoursynth/libzsmooth.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libzsmooth.so

%changelog
* Mon Dec 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 0.15-1
- Upgrade to 0.15

* Mon Dec 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 0.14-1
- Upgrade to 0.14

* Mon Dec 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 0.13-1
- Upgrade to 0.13

