Summary:	Think - Gnomified outliner
Name:		think
Version:	0.1.4
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.duke.edu/~pat4/think/%{name}-%{version}.tar.gz
URL:		http://www.duke.edu/~pat4/think/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Think is a Gnomified outliner. It doesn't do a whole lot at this
point, but can load and save outlines of text.

Think uses the Emacs outline-mode format for its files. It is a simple
format, and easily used in any text editor.. I certainly don't want to
force Emacs upon everyone else. Indeed, part of the reason I'm writing
Think is so that I won't have to have Emacs running..

Tree preferences:
- tree title
- show numbering
- show priorities
- show completed items

Node preferences:
- title
- text
- action item (produces a checkbox beside the node, in the tree)..
  this can also (for large projects) be a little meter that displays the
  percentage done
- of a node.. The percentages complete of branches are computed from
  their leaves.
- priority

Misc:
- drag & drop moving of nodes, from branch to branch
- cut & paste
- promote/demote buttons to move nodes around

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Applications

gzip -9nf ChangeLog AUTHORS NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Applications/*
