Name:           vapoursynth-plugin-mlrt-openvino
Version:        15.12
Release:        %autorelease
Summary:        Efficient CPU/GPU ML Runtimes for VapourSynth (OpenVINO)

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-mlrt
Source0:        https://github.com/AmusementClub/vs-mlrt/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-fix-cmake.patch

BuildRequires:  cmake gcc-c++ onnx-devel
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(openvino) pkgconfig(protobuf)

ExclusiveArch: x86_64

%description
%summary

%prep
%autosetup -n vs-mlrt-%{version} -p1

%build
cd vsov

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DVAPOURSYNTH_INCLUDE_DIRECTORY="$(pkg-config --cflags vapoursynth | sed 's|-I||g')" \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir}/vapoursynth \

%cmake_build

%install
cd vsov
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvsov.so

%changelog
%autochangelog
