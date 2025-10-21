Name:           vapoursynth-plugin-bm3dcuda-cpu
Version:        2.15
Release:        1%{?dist}
Summary:        BM3D denoising filter for VapourSynth, CPU version.

#%%define commit  200250b3864d50f0eb5f738686d06d9db3b1fbd3

License:        GPL-2.0
URL:            https://github.com/WolframRhodium/VapourSynth-BM3DCUDA/
Source0:        https://github.com/WolframRhodium/VapourSynth-BM3DCUDA/archive/refs/tags/R%{version}.tar.gz
# Source0:        https://github.com/WolframRhodium/VapourSynth-BM3DCUDA/archive/%{commit}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires:  pkgconfig(vapoursynth)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n VapourSynth-BM3DCUDA-R%{version}
#%%autosetup -n VapourSynth-BM3DCUDA-%{commit}


%build
%cmake \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir}/vapoursynth \
        -DCMAKE_BUILD_TYPE=Release \
        -DVAPOURSYNTH_INCLUDE_DIRECTORY="$(pkg-config --cflags vapoursynth | sed 's|-I||g')" \
        -DENABLE_CPU=ON \
        -DENABLE_CUDA=OFF \
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libbm3dcpu.so

%changelog
* Tue Oct 21 2025 adworacz <561689+adworacz@users.noreply.github.com> - 2.15-1
- Upgrade to v2.15

