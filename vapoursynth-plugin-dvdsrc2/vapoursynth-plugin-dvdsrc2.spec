%global debug_package %{nil}

%define commit  905e86be29adaa8adbbbd7c3675a3cec4942e057
%define dvdread_commit c7f373951bae9642e1ce1fbb2cd02f92c09756e0 


Name:           vapoursynth-plugin-dvdsrc2
Version:        0.2^20260227g905e86b
Release:        1%{?dist}
Summary:        DVD source plugin for VapourSynth

License:        GPL-2
URL:            https://github.com/jsaowji/dvdsrc2
Source0:        https://github.com/jsaowji/dvdsrc2/archive/%{commit}.tar.gz
Source1:        https://code.videolan.org/videolan/libdvdread/-/archive/%{dvdread_commit}/libdvdread-%{dvdread_commit}.tar.gz

BuildRequires:  cargo rust cargo-rpm-macros liba52-devel libmpeg2-devel libdvdread-devel meson
Requires:       vapoursynth-libs

%description
%summary


%prep
%autosetup -n dvdsrc2-%{commit}

%setup -n dvdsrc2-%{commit} -T -D -a 1

rm -rf vendored_libdvdread/dvdread && mv libdvdread-%{dvdread_commit} vendored_libdvdread/dvdread
ls -al vendored_libdvdread/dvdread


%build
%{__cargo} build --release --locked
ls target/release

%install
install -Dpm 0755 target/release/libdvdsrc2.so %{buildroot}%{_libdir}/vapoursynth/libdvdsrc2.so


%files
%doc README.txt
%{_libdir}/vapoursynth/libdvdsrc2.so



%changelog
* Mon Mar 02 2026 adworacz <561689+adworacz@users.noreply.github.com> - 0.2^20260227g905e86b-1
- Update to 0.2
