Name:           av-scenechange
Version:        0.22.1
Release:        2%{?dist}
Summary:        Scenechange detection tool written in Rust

License:        MIT
URL:            https://github.com/rust-av/av-scenechange
Source0:        https://github.com/rust-av/av-scenechange/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo rust clang cargo-rpm-macros

# ASM dep
BuildRequires:  nasm

# ffms2 dep
BuildRequires: pkgconfig(ffms2)

# FFmpeg the third deps
BuildRequires: pkgconfig(libavutil) pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter) pkgconfig(libswscale) pkgconfig(libswresample)

# Vapoursynth support
BuildRequires: pkgconfig(vapoursynth)

# Limiting to x86_64, as aarch64 seems to produce the following error for now
# Compiling av-decoders v0.9.0
# error[E0308]: mismatched types
#    --> /builddir/build/BUILD/av-scenechange-0.22.1-build/av-scenechange-0.22.1/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/av-decoders-0.9.0/src/helpers/ffms2.rs:640:18
#     |
# 640 |     err.Buffer = buffer_ptr;
#     |     ----------   ^^^^^^^^^^ expected `*mut u8`, found `*mut i8`
#     |     |
#     |     expected due to the type of this binding
#     |
#     = note: expected raw pointer `*mut u8`
#                found raw pointer `*mut i8` 
ExclusiveArch: x86_64

%description
%summary

Built with ffmpeg, ffms2, and vapoursynth features enabled.


%prep
%autosetup -n %{name}-%{version}


%build
%{__cargo} build --release --locked --features ffmpeg,ffms2,vapoursynth


%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}



%changelog
* Wed Feb 11 2026 adworacz <561689+adworacz@users.noreply.github.com> - 0.22.1-2
- Disable non-x86_64 builds

* Wed Feb 11 2026 adworacz <561689+adworacz@users.noreply.github.com> - 0.22.1-1
- Initial commit


