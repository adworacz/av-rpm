# Project requires clang:
# https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr/blob/main/meson.build#L28-L34
%global toolchain clang

Name:       vapoursynth-plugin-llvmexpr
Version:    3.3
Release:    1%{?dist}
Summary:    Fast, enhanced and Turing complete Vapoursynth Expr base on LLVM JIT 

License:    GPL-3.0
URL:        https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr
Source0:    https://github.com/Sunflower-Dolls/Vapoursynth-llvmexpr/archive/refs/tags/R%{version}.tar.gz

BuildRequires: meson clang llvm-devel pkgconfig(vapoursynth)

%description
%{summary}

%prep
%autosetup -n Vapoursynth-llvmexpr-R%{version}

meson subprojects download


%build
%meson
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/llvmexpr.so


%changelog
* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com>
- Add llvmexpr R3.3


