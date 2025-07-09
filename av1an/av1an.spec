Name:           av1an
Version:        0.4.4
Release:        %autorelease
Summary:        Cross-platform command-line AV1 / VP9 / HEVC / H264 encoding framework with per scene quality encoding

License:        GPL-3
URL:            https://github.com/rust-av/Av1an
Source0:        https://github.com/rust-av/Av1an/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang

# Rav1e dep
BuildRequires:  nasm

# FFmpeg the third deps
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libswresample)

# TODO: Weak dependencies on encoders/vapoursynth?

%description
%summary


%prep
%autosetup -n Av1an-%{version}


%build
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/


%files
%license LICENSE.md
%doc README.md



%changelog
%autochangelog
