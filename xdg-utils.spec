# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       xdg-utils

# >> macros
# << macros

Summary:    Desktop integration utilities from freedesktop.org
Version:    1.1.0~rc3+git20150119
Release:    1
Group:      System/Base
License:    MIT
BuildArch:  noarch
URL:        http://portland.freedesktop.org/
Source0:    http://portland.freedesktop.org/download/%{name}-1.1.0-rc3+git20150119.tar.gz
Source100:  xdg-utils.yaml
Patch0:     lca_support.patch
Patch1:     lca_protocol_handling.patch
Patch2:     do_not_generate_scripts.patch
Requires:   coreutils
Requires:   desktop-file-utils
Requires:   which
#BuildRequires: libxslt

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



%prep
%setup -q -n %{name}

# lca_support.patch
%patch0 -p1
# lca_protocol_handling.patch
%patch1 -p1
# do_not_generate_scripts.patch
%patch2 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%doc LICENSE README TODO
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings
%{_mandir}/man1/xdg-desktop-icon.*
%{_mandir}/man1/xdg-desktop-menu.*
%{_mandir}/man1/xdg-email.*
%{_mandir}/man1/xdg-icon-resource.*
%{_mandir}/man1/xdg-mime.*
%{_mandir}/man1/xdg-open.*
%{_mandir}/man1/xdg-screensaver.*
%{_mandir}/man1/xdg-settings.*
# >> files
# << files
