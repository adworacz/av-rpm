%global debug_package %{nil}

Name:           vapoursynth-plugin-adaptivegrain
Version:        0.3.2
Release:        %autorelease
Summary:        Reimplementation of the adaptive_grain mask as a Vapoursynth plugin. 

License:        GPL-3
URL:            https://github.com/kageru/adaptivegrain
Source0:        https://github.com/kageru/adaptivegrain/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo rust
Requires:       vapoursynth-libs

%description
%summary


%prep
%autosetup -n adaptivegrain-%{version}


%build
cargo build --release

%install
install -Dpm 0755 target/release/libadaptivegrain_rs.so %{buildroot}%{_libdir}/vapoursynth/libadaptivegrain_rs.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libadaptivegrain_rs.so



%changelog
%autochangelog
