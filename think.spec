Summary:	Think - Gnomified outliner
Summary(pl.UTF-8):	Think - gnomowy outliner
Name:		think
Version:	0.2.1
Release:	7.1
License:	GPL
Group:		X11/Applications
Source0:	http://primates.ximian.com/~peter/think/%{name}-%{version}.tar.gz
# Source0-md5:	cca6ebb9520f9eaa096b68f39616f70c
Patch0:		%{name}-desktop.in.patch
Patch1:		%{name}-acam_fixes.patch
URL:		http://primates.ximian.com/~peter/think/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	intltool
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Think is a Gnomified outliner. It doesn't do a whole lot at this
point, but can load and save outlines of text.

Think uses the Emacs outline-mode format for its files. It is a simple
format, and easily used in any text editor... I certainly don't want
to force Emacs upon everyone else. Indeed, part of the reason I'm
writing Think is so that I won't have to have Emacs running...

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
  percentage done of a node... The percentages complete of branches are
  computed from their leaves.
- priority

Misc:
- drag & drop moving of nodes, from branch to branch
- cut & paste
- promote/demote buttons to move nodes around

%description -l pl.UTF-8
Think to gnomowy outliner. Niewiele na razie robi, ale może wczytywać
i zapisywać zarysy tekstu.

Think używa emacsowego trybu outline do jego plików. To prosty format
i łatwy w użyciu z każdym edytorem... Nie chcę wmuszać wszystkim
Emacsa. Co więcej, jednym z powodów dla których piszę Thinka jest to,
żeby nie musieć uruchamiać Emacsa...

Własności drzewa: tytuł, pokazywanie numeracji, prioritetów i rzeczy
skończonych.

Własności węzła: tytuł, tekst, akcja (może być wskaźnikiem stopnia
ukończenia), priorytet.

Oprócz tego: przenoszenie węzłów między branchami metodą "pociągnij i
upuść", obsługa "wytnij i wklej", przyciski promote/demote do
przenoszenia liści.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

%build
%{__gettextize}
%{__libtoolize}
intltoolize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_datadir}/think
