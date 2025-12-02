%global debug_package %{nil}

Name:           vapoursynth-plugin-hysteresis
Version:        1.0.6
Release:        1%{?dist}
Summary:        Hysteresis filter for VapourSynth

License:        MIT
URL:            https://github.com/sgt0/vapoursynth-hysteresis
Source0:        https://github.com/sgt0/vapoursynth-hysteresis/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo rust cargo-rpm-macros
Requires:       vapoursynth-libs

%description
%summary


%prep
%autosetup -n vapoursynth-hysteresis-%{version}


%build
%{__cargo} build --release --locked

%install
install -Dpm 0755 target/release/libhysteresis.so %{buildroot}%{_libdir}/vapoursynth/libhysteresis.so


%files
%license LICENSE.md
%doc README.md
%{_libdir}/vapoursynth/libhysteresis.so



%changelog
* Tue Dec 02 2025 adworacz <561689+adworacz@users.noreply.github.com> - 1.0.6-1
- Upgrade to 1.0.6

