%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
AutoReqProv: no

Summary: Programmer's text editor written in Java
Name: jedit
Version: 5.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://www.jedit.org/
Source1:  https://sourceforge.net/projects/jedit/files/jedit/%{version}/jedit%{version}install.jar
Source2: jedit
Source3: jeditbg.sh
Source4: jedit.props
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: java >= 1.6
Requires: java >= 1.6
Requires: desktop-file-utils

%description
jEdit is an Open Source, cross platform text editor written in Java. It
has an extensive feature set that includes syntax highlighting, auto indent,
folding, word wrap, abbreviation expansion, multiple clipboards, powerful
search and replace, and much more.

Futhermore, jEdit is extremely customizable, and extensible, using either
macros written in the BeanShell scripting language, or plugins written
in Java.


%prep


%build


%install
install -dm 755 %{buildroot}%{_datadir}/java/%{name}
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_datadir}/man/man1

java -jar %{SOURCE1} auto \
    "%{buildroot}/%{_datadir}/java/jedit/" \
    unix-script="%{buildroot}/%{_bindir}/" \
    unix-man="%{buildroot}/%{_datadir}/man/man1/"
  

install -Dm755 %{SOURCE2} "%{buildroot}%{_bindir}/jedit"
install -Dm755 %{SOURCE3} "%{buildroot}%{_bindir}/jeditbg"
install -Dm644 %{SOURCE4} "%{buildroot}%{_datadir}/jedit/default.props"
install -Dm644 "%{buildroot}%{_datadir}/java/jedit/doc/jedit.png" \
    "%{buildroot}%{_datadir}/pixmaps/jedit.png"


# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=jedit
GenericName=jedit
Comment=Text editor for programmers, written in Java
Icon=/usr/share/pixmaps/jedit.png
Type=Application
Categories=GTK;Utility;TextEditor;
Exec=jedit
StartupNotify=false
Terminal=false
EOF

chmod a+x %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/java/jedit/
%{_bindir}/jeditbg
%{_datadir}/%{name}/default.props
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/jedit.1.gz


%changelog

* Mon Jul 03 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 5.4.0-1
- Updated to 5.4.0

* Wed Mar 30 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 5.3.0-1
- Updated to 5.3.0

* Thu Oct 01 2015 David Vasquez <davidjeremias82 AT gmail DOT com> - 5.1.0-2
- Updated to 5.2.0

* Mon Sep 23 2013 David Vasquez <davidjeremias82 AT gmail DOT com> - 5.1.0-2
- Initial build for Fedora
- Inspirated in PKGBUILD Arch Linux 
