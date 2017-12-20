%define name	phantomjs
%define version	2.1.1
%define release 1%{?dist}

Summary:	a headless WebKit with JavaScript API
Name:		%{name}
Version:	%{version}
License:	BSD
Release:	%{release}
Packager:	Travis Groth <tgroth@gmail.com>
Group:		Utilities/Misc
BuildRoot:  %{_topdir}/BUILDROOT/
Source:		%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: flex
BuildRequires: bison
BuildRequires: gperf
BuildRequires: ruby
BuildRequires: openssl-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libicu-devel
BuildRequires: sqlite-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: git

%if %{?el6}
BuildRequires: python-argparse
%endif

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%build
./build.py --confirm --release --git-clean-qtbase --git-clean-qtwebkit 

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp bin/%{name} %{buildroot}%{_bindir}/%{name}
cp examples/* %{buildroot}%{_datadir}/%{name}/examples/
cp CONTRIBUTING.md %{buildroot}%{_datadir}/%{name}/
cp ChangeLog %{buildroot}%{_datadir}/%{name}/
cp LICENSE.BSD %{buildroot}%{_datadir}/%{name}/
cp README.md %{buildroot}%{_datadir}/%{name}/

%files
%defattr(0444,root,root)
%attr(0555,root,root)%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Tue Nov 29 2016 Travis Groth <tgroth@gmail.com>
- Updated to 2.1.1
- Add more BuildRequires

* Sat May 9 2015 Frankie Dintino <fdintino@gmail.com>
- updated to version 2.0, added BuildRequires directives

* Fri Apr 18 2014 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Tue Apr 30 2013 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Wed Apr 24 2013 Robin Helgelin <lobbin@gmail.com>
- updated to version 1.9

* Thu Jan 24 2013 Matthew Barr <mbarr@snap-interactive.com>
- updated to version 1.8

* Thu Nov 15 2012 Jan Schaumann <jschauma@etsy.com>
- first rpm version
