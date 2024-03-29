Summary:	Xpresent extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia Xpresent
Name:		xorg-lib-libXpresent
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXpresent-%{version}.tar.xz
# Source0-md5:	bdd3ec17c6181fd7b26f6775886c730d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-proto-presentproto-devel >= 1.0
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xpresent extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia Xpresent.

%package devel
Summary:	Header files for libXpresent library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXpresent
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-proto-presentproto-devel >= 1.0
Requires:	xorg-proto-xproto-devel

%description devel
Xpresent extension library.

This package contains the header files needed to develop programs that
use libXpresent.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia Xpresent.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXpresent.

%package static
Summary:	Static libXpresent library
Summary(pl.UTF-8):	Biblioteka statyczna libXpresent
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xpresent extension library.

This package contains the static libXpresent library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia Xpresent.

Pakiet zawiera statyczną bibliotekę libXpresent.

%prep
%setup -q -n libXpresent-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXpresent.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXpresent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXpresent.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXpresent.so
%{_includedir}/X11/extensions/Xpresent.h
%{_pkgconfigdir}/xpresent.pc
%{_mandir}/man3/XPresent*.3*
%{_mandir}/man3/Xpresent.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXpresent.a
