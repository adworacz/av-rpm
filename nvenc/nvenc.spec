%global debug_package %{nil}

%define cppcodec_commit bd6ddf95129e769b50ef63e0f558fa21364f3f65
%define dtl_commit b83e617aab99ae85e5be4e3b2074a5ca873fbb8b

Name:       nvenc
Version:    9.07
Release:    1%{?dist}
Summary:    Hardware encoder for Nvidia

License:    MIT
URL:        https://github.com/rigaya/NVEnc
Source0:    https://github.com/rigaya/NVEnc/archive/refs/tags/%{version}.tar.gz
Source1:    https://github.com/tplgy/cppcodec/archive/%{cppcodec_commit}.tar.gz
Source2:    https://github.com/cubicdaiya/dtl/archive/%{dtl_commit}.tar.gz

BuildRequires: gcc-c++ cuda-toolkit

# FFmpeg lib dependencies
BuildRequires: pkgconfig(libavutil) pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter) pkgconfig(libswresample)

# Vapoursynth support
BuildRequires: pkgconfig(vapoursynth)

# Dovi
BuildRequires: pkgconfig(dovi)

# Placebo
BuildRequires: pkgconfig(libplacebo)

# VMAF
BuildRequires: pkgconfig(libvmaf)

# ASS
BuildRequires: pkgconfig(libass)

%description
%{summary}

%prep
%autosetup -n NVEnc-%{version}

%setup -n NVEnc-%{version} -T -D -a 1
%setup -n NVEnc-%{version} -T -D -a 2

rm -rf cppcodec && mv cppcodec-%{cppcodec_commit} cppcodec
rm -rf dtl && mv dtl-%{dtl_commit} dtl

%build
%{set_build_flags}; %{_configure} --prefix=%{buildroot}%{_prefix} --extra-cudaldflags="-L/usr/local/cuda/lib64/stubs"

%make_build


%install
%make_install


%check


%files
%license NVEnc_license.txt
%doc NVEncC_Options.en.md
%{_bindir}/*


%changelog
* Sun Nov 09 2025 adworacz <561689+adworacz@users.noreply.github.com> - 9.07-1
- Update to 9.07

* Fri Oct 31 2025 adworacz <561689+adworacz@users.noreply.github.com> - 9.06-1
- Update to 9.06

* Wed Oct 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 9.05-1
- Version 9.05


