Name:           vapoursynth-plugin-mlrt-ncnn
Version:        15.12
Release:        %autorelease
Summary:        Efficient CPU/GPU ML Runtimes for VapourSynth (NCNN)

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-mlrt
Source0:        https://github.com/AmusementClub/vs-mlrt/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-fix-cmake.patch

BuildRequires:  cmake gcc-c++ onnx-devel
BuildRequires:  pkgconfig(vapoursynth) pkgconfig(ncnn) pkgconfig(protobuf)

ExclusiveArch: x86_64

# TODO: This might not work because mlrt requires onnx to be compiled with 
# a set of featuers that fedora doesn't set.
# https://src.fedoraproject.org/rpms/onnx/blob/f42/f/onnx.spec#_77
# https://github.com/AmusementClub/vs-mlrt/blob/master/.github/workflows/linux-ncnn.yml#L77-L84

%description
%summary

%prep
%autosetup -n vs-mlrt-%{version} -p1

%build
cd vsncnn

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DVAPOURSYNTH_INCLUDE_DIRECTORY="$(pkg-config --cflags vapoursynth | sed 's|-I||g')" \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir}/vapoursynth \

%cmake_build

%install
cd vsncnn
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvsncnn.so

%changelog
%autochangelog
