%define _unpackaged_files_terminate_build 1

Name: alterator-interface-legacy
Version: 0.1.0
Release: alt1

Summary: legacy interface
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-interface-legacy

Source0: %name-%version.tar

%description
legacy interface for alterator operating via D-Bus.

%prep
%setup

%install
mkdir -p %buildroot%{_datadir}/dbus-1/interfaces
mkdir -p %buildroot%{_sysconfdir}/polkit-1/rules.d
mkdir -p %buildroot%{_datadir}/alterator/backends

install -v -p -m 644 -D ru.basealt.alterator.legacy.xml %buildroot%{_datadir}/dbus-1/interfaces
install -v -p -m 644 -D 49-alterator-interface-legacy.rules %buildroot%{_sysconfdir}/polkit-1/rules.d
install -v -p -m 644 -D legacy.backend %buildroot%{_datadir}/alterator/backends

%files
%{_datadir}/alterator/backends/legacy.backend
%{_datadir}/dbus-1/interfaces/ru.basealt.alterator.applications.xml
%{_sysconfdir}/polkit-1/rules.d/49-alterator-module-application.rules

%changelog
* Thu Oct 24 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.0-alt1
- initial build
