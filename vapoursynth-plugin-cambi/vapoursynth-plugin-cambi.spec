%global debug_package %{nil}

Name:           vapoursynth-plugin-cambi
Version:        1.1.4
Release:        1%{?dist}
Summary:        Contrast Aware Multiscale Banding Index (CAMBI) as a VapourSynth plugin. 

License:        MIT
URL:            https://github.com/sgt0/vapoursynth-cambi
Source0:        https://github.com/sgt0/vapoursynth-cambi/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo rust cargo-rpm-macros

Requires:       pkgconfig(vapoursynth)

%description
%summary


%prep
%autosetup -n vapoursynth-cambi-%{version}


%build
%{__cargo} build --release --locked

%install
install -Dpm 0755 target/release/libcambi.so %{buildroot}%{_libdir}/vapoursynth/libcambi.so


%files
%license LICENSE.md
%doc README.md
%{_libdir}/vapoursynth/*.so



%changelog
* Sun Dec 28 2025 adworacz <561689+adworacz@users.noreply.github.com> - 1.1.4-1
- Add cambi 1.1.4
