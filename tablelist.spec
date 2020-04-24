#
# spec file for package tablelist
#

Name:           tablelist
BuildRequires:  tcl >= 8.6
Version:        6.9
Release:        0
Summary:        The implementation of the tablelist mega-widget for Tcl/Tk
Url:            http://www.nemethi.de/
License:        MIT
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tcl >= 8.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://www.nemethi.de/tablelist/%{name}%{version}.tar.gz

%description
A tablelist is a multi-column listbox and tree widget.
This package is the implementation of the tablelist mega-widget.

%prep
%setup -q -n %{name}%{version}

%build

%install
dir=%buildroot%tcl_noarchdir/%name%version
mkdir -m755 -p $dir
chmod a-x *.tcl
cp -a *.tcl scripts $dir
chmod a-x demos/*.tcl

%files
%defattr(-,root,root)
%doc demos doc
%tcl_noarchdir

%changelog

