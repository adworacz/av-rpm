Name:           vapoursynth-plugin-eedi3
Version:        7
Release:        2%{?dist}
Summary:        Renewed EEDI3 filter for VapourSynth

# %%define commit  d11bdb37c7a7118cd095b53d9f8fbbac02a06ac0

License:        GPL-2.0
URL:            https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI3
Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI3/archive/refs/tags/r%{version}.tar.gz
#Source0:        https://github.com/HomeOfVapourSynthEvolution/VapourSynth-EEDI3/archive/%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(vapoursynth)
Requires:       vapoursynth-libs

# Only seems buildable on x86_64...
ExclusiveArch: x86_64

%description
%{summary}


%prep
#%%autosetup -n VapourSynth-EEDI3-%{commit}
%autosetup -n VapourSynth-EEDI3-r%{version}


%build
%meson
%meson_build


%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libeedi3m.so

%changelog
* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 7-2
- Actually upgrade to r7, remove OpenCL deps and eedi3cl no longer exists

* Sat Nov 29 2025 adworacz <561689+adworacz@users.noreply.github.com> - 7-1
- Update to 7

%autochangelog
