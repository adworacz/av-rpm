Name:       linux-firewire-utils
Version:    0.5.1
Release:    1%{?dist}
Summary:    Linux FireWire bus inspection and configuration tools

License:    GPLv2
URL:    https://git.kernel.org/pub/scm/utils/ieee1394/linux-firewire-utils.git/
Source0: https://git.kernel.org/pub/scm/utils/ieee1394/linux-firewire-utils.git/snapshot/%{name}-%{version}.tar.gz

BuildRequires: meson gcc
Requires: bash glibc

%description
%summary


%prep
%autosetup -n %{name}-%{version}


%build
%meson
%meson_build


%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license COPYING
%doc README.rst
%{_bindir}/*
%{_mandir}/*


%changelog
* Wed Nov 18 2026 adworacz <561689+adworacz@users.noreply.github.com> - 0.5.1-1
- Provide 0.5.1-1


