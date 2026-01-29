# originally imported from here: https://gitlab.com/shadowblue/allthetools/-/blob/main/pueue/pueue.spec?ref_type=heads
# Full credit goes to the original authors. I'm just forking it to avoid the
# need to use their entire repo and allow customization for my own needs.
%global debug_package %{nil}

Name:           pueue
Version:        4.0.2
Release:        2%{?dist}
Summary:        Manage your shell commands.

License:        MIT OR Apache-2.0
URL:            https://github.com/Nukesor/%{name}
Source:         https://github.com/Nukesor/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  systemd-rpm-macros

%description
Pueue is a command-line task management tool for sequential and
parallel execution of long-running tasks.

Simply put, it's a tool that processes a queue of shell commands.
On top of that, there are a lot of convenient features and abstractions.

Since Pueue is not bound to any terminal, you can control your tasks
from any terminal on the same machine. The queue will be continuously processed
even if you no longer have any active ssh sessions.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

# Change from the overly verbose debug logging to just normal verbosity
sed -i 's/-vv/-v/' utils/pueued.service

mkdir generated_completions
./target/release/%{name} completions bash generated_completions/
./target/release/%{name} completions fish generated_completions/
./target/release/%{name} completions zsh generated_completions/

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
install -Dpm 0755 target/release/pueued -t %{buildroot}%{_bindir}/
install -Dpm 0644 utils/pueued.service -t %{buildroot}/%{_userunitdir}/
install -Dpm 0644 generated_completions/%{name}.bash -t %{buildroot}/%{bash_completions_dir}/%{name}
install -Dpm 0644 generated_completions/%{name}.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 generated_completions/_%{name} -t %{buildroot}/%{zsh_completions_dir}/

%post
%systemd_user_post pueued.service

%preun
%systemd_user_preun pueued.service

%postun
%systemd_user_postun_with_restart pueued.service

%files
%license LICENSE.MIT
%license LICENSE.APACHE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_bindir}/pueued
%{_userunitdir}/pueued.service
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
* Thu Jan 29 2026 adworacz <561689+adworacz@users.noreply.github.com> - 4.0.2-2
- Decrease the pueued service logging verbosity

* Tue Dec 30 2025 Andrey Brusnik <dev@shdwchn.io> - 4.0.2-1
- chore(pueue): Bump to 4.0.2

* Mon Mar 17 2025 Andrey Brusnik <dev@shdwchn.io> - 4.0.0-1
- chore(pueue): Bump to 4.0.0

* Fri Dec 27 2024 Andrey Brusnik <dev@shdwchn.io> - 3.4.1-3
- fix(pueue): Fix license

* Sat Sep 07 2024 Andrey Brusnik <dev@shdwchn.io> - 3.4.1-2
- fix(pueue): Fix bash completions path

* Tue Jun 18 2024 Andrey Brusnik <dev@shdwchn.io> - 3.4.1-1
- feat: Added pueue package
