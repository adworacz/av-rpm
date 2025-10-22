Name:       nvenc
Version:    9.05
Release:    1%{?dist}
Summary:    Hardware encoder for Nvidia

License:    MIT
URL:        https://github.com/rigaya/NVEnc
Source0:    https://github.com/rigaya/NVEnc/archive/refs/tags/%{version}.tar.gz

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

# TODO vulkan support
#Requires:

%description
%{summary}

%prep
%autosetup -n NVEnc-%{version}
# TODO: Setup cppcodec and dtl dependencies.

%build
# Set various CUDA env vars so that nvcc (compiler) and cuda libs can be found.
# export PATH="$PATH:/usr/local/cuda/bin"
# export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"

%{set_build_flags}; %{_configure} --prefix=%{_prefix} --extra-cudaldflags="-L/usr/local/cuda/lib64/stubs"

%make_build


%install
%make_install


%check


%files
%license NVEnc_license.txt
%doc NVEncC_Options.en.md
%{_bindir}/*


%changelog
* Wed Oct 22 2025 adworacz <561689+adworacz@users.noreply.github.com> - 9.05-1
- Version 9.05


