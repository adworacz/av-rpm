%global debug_package %{nil}

Name:           subtile-ocr
Version:        0.2.6
Release:        1%{?dist}
Summary:        A Rust command line tool to convert subtitle from image to text with OCR. Started as fork of vobsubocr. 

License:        GPL-3
URL:            https://github.com/gwen-lg/subtile-ocr
Source0:        https://github.com/gwen-lg/subtile-ocr/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo rust clang cargo-rpm-macros

# Leptonica / Tesseract deps
BuildRequires:  pkgconfig(lept) pkgconfig(tesseract)

# FFmpeg the third deps
# BuildRequires: pkgconfig(libavutil) pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavdevice)
# BuildRequires: pkgconfig(libavfilter) pkgconfig(libswscale) pkgconfig(libswresample)

# Vapoursynth support
# BuildRequires: pkgconfig(vapoursynth)

# TODO: Weak dependencies on encoders/vapoursynth?

%description
%summary


%prep
%autosetup -n subtile-ocr-%{version}


%build
%{__cargo} build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}



%changelog
* Wed Feb 18 2026 adworacz <561689+adworacz@users.noreply.github.com> - 0.2.6-1
- Add subtitle-ocr


