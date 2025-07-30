Name:           vapoursynth-plugin-chickendream
Version:        2

Release:        %autorelease
Summary:        Realistic film grain generator, plug-in for Vapoursynth and Avisynth+

License:        WTFPL
URL:            https://gitlab.com/EleonoreMizo/chickendream
Source0:        https://gitlab.com/EleonoreMizo/chickendream/-/archive/r%{version}/chickendream-r%{version}.tar.gz

#TODO: Try getting it to build with clang. I was having some issues.
BuildRequires:  gcc-c++ autoconf automake libtool
BuildRequires:  pkgconfig(vapoursynth)

%description
%summary

%prep
%autosetup -n chickendream-r%{version}

%build
cd build/unix
chmod +x autogen.sh
./autogen.sh
%configure --disable-static --libdir=%{_libdir}/vapoursynth 
%make_build

%install
cd build/unix
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.md
%{_libdir}/vapoursynth/libchickendream.so

%changelog
%autochangelog
