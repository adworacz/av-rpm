Name:           av1an
Version:        0.4.4
Release:        %autorelease
Summary:        Cross-platform command-line AV1 / VP9 / HEVC / H264 encoding framework with per scene quality encoding

License:        GPL-3
URL:            https://github.com/rust-av/Av1an
Source0:        https://github.com/rust-av/Av1an/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust

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
* Sun Jun 29 2025 Austin Dworaczyk Wiltshire <adw.wiltshire@gmail.com>
- Initial commit.
