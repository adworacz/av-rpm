%global debug_package %{nil}

Name:           vapoursynth-plugin-zscene
Version:        0.1
Release:        1%{?dist}
Summary:        Scene change detection for Vapoursynth

License:        MIT
URL:            https://github.com/adworacz/zscene
Source0:        https://github.com/adworacz/zscene/archive/refs/tags/%{version}.tar.gz

#BuildRequires:  zig >= 0.15.2
BuildRequires:  zig >= 0.14.1
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n zscene-%{version}


%build
zig build %{_zig_general_options} %{_zig_project_options} --release=fast

%install
%{__install} -pDm 755 zig-out/lib/libzscene.so %{buildroot}%{_libdir}/vapoursynth/libzscene.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/*

%changelog
* Wed Dec 31 2025 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 0.1-1
- Add version 0.1


