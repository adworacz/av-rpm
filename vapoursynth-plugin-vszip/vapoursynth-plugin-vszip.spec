%global debug_package %{nil}

Name:           vapoursynth-plugin-vszip
Version:        9
Release:        1%{?dist}
Summary:        VapourSynth Zig Image Process

License:        MIT
URL:            https://github.com/dnjulek/vapoursynth-zip
Source0:        https://github.com/dnjulek/vapoursynth-zip/archive/refs/tags/R%{version}.tar.gz

BuildRequires:  zig >= 0.14.0
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

%description
%{summary}


%prep
%autosetup -n vapoursynth-zip-R%{version}


%build
zig build %{_zig_general_options} %{_zig_project_options} --release=fast

%install
%{__install} -pDm 755 zig-out/lib/libvszip.so %{buildroot}%{_libdir}/vapoursynth/libvszip.so


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvszip.so

%changelog
* Tue Dec 02 2025 adworacz <561689+adworacz@users.noreply.github.com> - 9-1
- Upgrade to R9

