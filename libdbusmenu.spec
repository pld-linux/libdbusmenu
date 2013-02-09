Summary:	DBus Menu Library
Name:		libdbusmenu
Version:	0.6.1
Release:	1
License:	GPL v3, LGPL v2.1, LGPL v3
Group:		Libraries
URL:		https://launchpad.net/dbusmenu
Source0:	http://launchpad.net/dbusmenu/0.7/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	820b6999dd1008328bfa442575d859a1
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	vala
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small little library that was created by pulling out some common
code out of indicator-applet.

It passes a menu structure across DBus so that a program can create a
menu simply without worrying about how it is displayed on the other
side of the bus.

%package devel
Summary:	libraries and headers for libdbusmenu-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdbusmenu-glib library.

%package jsonloader
Summary:	Library to load JSON descriptions of menus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description jsonloader
A small library to load JSON descriptions of menus. Mostly for
testing.

%package jsonloader-devel
Summary:	Libraries and headers for libdbusmenu-jsonloader
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-jsonloader = %{version}-%{release}

%description jsonloader-devel
Header files for libdbusmenu-jsonloader library.

%package gtk3
Summary:	libdbusmenu-gtk3 Library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk3
libdbusmenu-gtk3 Library.

%package gtk3-devel
Summary:	Libraries and headers for libdbusmenu-gtk3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}

%description gtk3-devel
Header files for libdbusmenu-gtk3 library.

%package apidocs
Summary:	%{name} API documentation
Group:		Documentation
Requires:	gtk-doc

%description apidocs
%{name} API documentation.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-introspection
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
# obsoleted by .pc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-glib.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-gtk3.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-jsonloader.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	jsonloader -p /sbin/ldconfig
%postun	jsonloader -p /sbin/ldconfig

%post	gtk3 -p /sbin/ldconfig
%postun	gtk3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/%{name}-glib.so.*.*.*
%ghost %{_libdir}/%{name}-glib.so.4
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dbusmenu-bench
%attr(755,root,root) %{_libdir}/dbusmenu-dumper
%attr(755,root,root) %{_libdir}/dbusmenu-testapp
%dir %{_includedir}/libdbusmenu-glib-0.4
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib
%{_libdir}/%{name}-glib.so
%{_pkgconfigdir}/dbusmenu-glib-0.4.pc
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/json
%{_datadir}/%{name}/json/test-gtk-label.json

%files jsonloader
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-jsonloader.so.*.*.*
%ghost %{_libdir}/%{name}-jsonloader.so.4

%files jsonloader-devel
%defattr(644,root,root,755)
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader
%{_libdir}/%{name}-jsonloader.so
%{_pkgconfigdir}/dbusmenu-jsonloader-0.4.pc

%files gtk3
%defattr(644,root,root,755)
%{_libdir}/%{name}-gtk3.so.*
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

%files gtk3-devel
%defattr(644,root,root,755)
%dir %{_includedir}/libdbusmenu-gtk3-0.4
%dir %{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/*.h
%{_libdir}/%{name}-gtk3.so
%{_pkgconfigdir}/dbusmenu-gtk3-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi

#%files apidocs
#%defattr(644,root,root,755)
#%dir %{_datadir}/gtk-doc/html/libdbusmenu-glib
#%{_datadir}/gtk-doc/html/libdbusmenu-glib/*
#%dir %{_datadir}/gtk-doc/html/libdbusmenu-gtk
#%{_datadir}/gtk-doc/html/libdbusmenu-gtk/*
