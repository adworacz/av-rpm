Name:   vapoursynth-plugin-removedirt
Version:    1.1
Release:    1%{?dist}
Summary:    Vapoursynth plugin for removing dirt from film clips.

License:    GPL-2.0
URL:        https://github.com/pinterf/RemoveDirt
Source0:    https://github.com/pinterf/RemoveDirt/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++ cmake pkgconfig(vapoursynth)

%description
%summary


%prep
%autosetup -n RemoveDirt-%{version}


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
#%%cmake_install
%{__install} -Dm755 %{__cmake_builddir}/RemoveDirt/libremovedirt.so %{buildroot}%{_libdir}/vapoursynth/libremovedirt.so


%files
%license LICENSE
%doc README.md RemoveDirt/documentation/*.htm
%{_libdir}/vapoursynth/*.so


%changelog
* Tue Feb 03 2026 adworacz <561689+adworacz@users.noreply.github.com> - 1.1-1
- Initial commit


