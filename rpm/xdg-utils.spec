Name:       xdg-utils
Summary:    Desktop integration utilities from freedesktop.org
Version:    1.1.3
Release:    1
License:    MIT
BuildArch:  noarch
URL:        http://portland.freedesktop.org/
Source0:    https://portland.freedesktop.org/download/%{name}-%{version}.tar.gz
Patch0:     0001-Pre-generate-txt-files.patch
Patch1:     0002-Pre-generate-man-pages.patch
Patch2:     0003-Disable-doc-generation.patch
Patch3:     0004-lca-support.patch
Requires:   coreutils
Requires:   desktop-file-utils
Requires:   which
# Needed by for example xdg-mime
Requires:   awk

%description
%{name} contains utilities for integrating applications with the
desktop environment, regardless of which desktop environment is used.
They are part of freedesktop.org's Portland project.

The following utilities are included:
 * xdg-desktop-menu - Install desktop menu items
 * xdg-desktop-icon - Install icons on the user's desktop
 * xdg-icon-resource - Install icon resources
 * xdg-mime - Gather MIME information about a file
 * xdg-open - Open a URL in the user's preferred application that
              handles the respective URL or file type
 * xdg-email - Open the user's preferred email client, potentially with
               subject and other info filled in
 * xdg-screensaver - Enable, disable, or suspend the screensaver
 * xdg-settings - get various settings (default web browser) from
                  the desktop environment

%package doc
Summary: Documentation of %{name}

%description doc
%{name} documentation package including man packages.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings

%files doc
%doc README TODO
%{_mandir}/man1/xdg-desktop-icon.*
%{_mandir}/man1/xdg-desktop-menu.*
%{_mandir}/man1/xdg-email.*
%{_mandir}/man1/xdg-icon-resource.*
%{_mandir}/man1/xdg-mime.*
%{_mandir}/man1/xdg-open.*
%{_mandir}/man1/xdg-screensaver.*
%{_mandir}/man1/xdg-settings.*
