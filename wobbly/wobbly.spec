Name:           wobbly
Version:        9
Release:        2%{?dist}
Summary:        IVTC assistant for VapourSynth, similar to Yatta 

License:        None
URL:            https://github.com/Jaded-Encoding-Thaumaturgy/Wobbly
Source0:        https://github.com/Jaded-Encoding-Thaumaturgy/Wobbly/archive/refs/tags/v%{version}.tar.gz
Source1:        wobbly.desktop
Source2:        wibbly.desktop

BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)
# GUI requirements
BuildRequires:  qt5-qtbase-devel
# Desktop file install
BuildRequires: desktop-file-utils

%description
%summary

%prep
%autosetup -n Wobbly-%{version}

%build
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth
%make_build

%install
%make_install 

desktop-file-install                                    \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{SOURCE1}

desktop-file-install                                    \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{SOURCE2}

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_bindir}/*
%{_datadir}/applications/*

%changelog
* Sat Aug 09 2025 Austin Dworaczyk Wiltshire <561689+adworacz@users.noreply.github.com> - 9-2
- Add desktop files

