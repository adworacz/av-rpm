# TODO: Hopefully this can be removed in future releases, as 0.5.0 used '0.5' as their tag.
%define version_tag 0.5

Name:           av1an
Version:        0.5.0
Release:        1%{?dist}
Summary:        Cross-platform command-line AV1 / VP9 / HEVC / H264 encoding framework with per scene quality encoding

License:        GPL-3
URL:            https://github.com/rust-av/Av1an
Source0:        https://github.com/rust-av/Av1an/archive/refs/tags/%{version_tag}.tar.gz

BuildRequires:  cargo rust clang cargo-rpm-macros

# Rav1e dep
BuildRequires:  nasm

# FFmpeg the third deps
BuildRequires: pkgconfig(libavutil) pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter) pkgconfig(libswscale) pkgconfig(libswresample)

# Vapoursynth support
BuildRequires: pkgconfig(vapoursynth)

# TODO: Weak dependencies on encoders/vapoursynth?

%description
%summary


%prep
%autosetup -n Av1an-%{version_tag}


%build
%{__cargo} build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/


%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}



%changelog
* Wed Dec 03 2025 adworacz <561689+adworacz@users.noreply.github.com> - 0.5.0-1
- Upgrade to 0.5.0

