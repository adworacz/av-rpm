Name:           vapoursynth-plugin-vsocr
Version:        3
Release:        %autorelease
Summary:        OCR plugin for VapourSynth

License:        MIT
URL:            https://github.com/vapoursynth/vs-ocr
Source0:        https://github.com/vapoursynth/vs-ocr/archive/refs/tags/R%{version}.tar.gz

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(tesseract)

%description
%{summary}

%prep
%autosetup -n vs-ocr-R%{version}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc docs/ocr.rst
%{_libdir}/vapoursynth/libocr.so


%changelog
%autochangelog
