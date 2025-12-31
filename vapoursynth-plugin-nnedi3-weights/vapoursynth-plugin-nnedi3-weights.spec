%global debug_package %{nil}

Name:           vapoursynth-plugin-nnedi3-weights
Version:        12
Release:        1%{?dist}
Summary:        Weights for NNEDI3-based Vapoursynth filters (nnedi3, znedi3, nnedi3cl), as well as ffmpeg filter.

License:        None
URL:            https://github.com/dubhater/vapoursynth-nnedi3
Source0:        https://github.com/dubhater/vapoursynth-nnedi3/archive/refs/tags/v%{version}.tar.gz

%description
%summary

%prep
%autosetup -n vapoursynth-nnedi3-%{version}

%build

%install
%{__install} -pDm755 src/nnedi3_weights.bin %{buildroot}%{_datadir}/nnedi3/nnedi3_weights.bin

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_symlinks
%{__install} -d %{buildroot}%{_libdir}/vapoursynth
%{__ln_s} %{_datadir}/nnedi3/nnedi3_weights.bin %{buildroot}%{_libdir}/vapoursynth/nnedi3_weights.bin

%files
%{_libdir}/vapoursynth/*
%{_datadir}/nnedi3/nnedi3_weights.bin

%changelog
* Wed Dec 31 2025 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 12-1
- Initial commit

