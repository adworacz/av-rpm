# Project requires clang:
# https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr/blob/main/meson.build#L28-L34
%global toolchain clang

%define     commit  badbc42e58327cd9f2a41c6a88431d02abcc4ffd

Name:       vapoursynth-plugin-llvmexpr
Version:    3.3^20251204gbadbc42
Release:    1%{?dist}
Summary:    Fast, enhanced and Turing complete Vapoursynth Expr base on LLVM JIT 

License:    GPL-3.0
URL:        https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr
#Source0:    https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr/archive/refs/tags/R%{version}.tar.gz
Source0:    https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr/archive/%{commit}.tar.gz

BuildRequires: meson clang llvm-devel pkgconfig(vapoursynth)

%description
%{summary}

%prep
#%%autosetup -n Vapoursynth-llvmexpr-R%{version}
%autosetup -n Vapoursynth-llvmexpr-%{commit}

meson subprojects download


%build
%meson
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libllvmexpr.so


%changelog
* Thu Dec 04 2025 adworacz <561689+adworacz@users.noreply.github.com> - 3.3^20251204gbadbc42-1
- Update to latest commit so compiles work on Fedora 42

* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com>
- Add llvmexpr R3.3


