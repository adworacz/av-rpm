Name:           vapoursynth-plugin-nlm-ispc
Version:        2
Release:        %autorelease
Summary:        Non-local means denoise filter (CPU only), drop-in replacement of the KNLMeansCL for VapourSynth

License:        GPL-3.0
URL:            https://github.com/AmusementClub/vs-nlm-ispc
Source0:        https://github.com/AmusementClub/vs-nlm-ispc/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake gcc-c++ ispc
BuildRequires:  pkgconfig(vapoursynth)

%ifarch x86_64
%define ins_sets sse2-i32x4;avx1-i32x4;avx2-i32x16
%elifarch aarch64
%define ins_sets neon-i32x4;
%endif

%description
%summary

%prep
%autosetup -n vs-nlm-ispc-%{version}

%build

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_ISPC_INSTRUCTION_SETS="%{ins_sets}" \
        -DCMAKE_ISPC_FLAGS="--opt=fast-math" \
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license LICENSE
%doc README.md
%{_libdir}/vapoursynth/libvsnlm_ispc.so

%changelog
%autochangelog
