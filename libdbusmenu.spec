#
# Conditional build:
%bcond_without	gtk2		# GTK+ 2.x version of libdbusmenu-gtk
%bcond_without	gtk3		# GTK+ 3.x version of libdbusmenu-gtk
%bcond_without	static_libs	# static libraries
%bcond_without	vala		# Vala API
%bcond_with	valgrind	# Disable json tests requiring valgrind to run

Summary:	DBus Menu Library
Summary(pl.UTF-8):	Biblioteka DBus Menu
Name:		libdbusmenu
Version:	12.10.2
Release:	4
License:	GPL v3, LGPL v2.1, LGPL v3
Group:		Libraries
Source0:	https://launchpad.net/libdbusmenu/12.10/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	e30fc986b447f62513d61225fa573a70
URL:		https://launchpad.net/libdbusmenu
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	gobject-introspection-devel >= 0.10
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.16}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-glib-devel >= 0.13.4
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
%{?with_vala:BuildRequires:	vala}
%{?with_valgrind:BuildRequires:	valgrind}
BuildRequires:	xorg-lib-libX11-devel >= 1.3
Requires:	glib2 >= 1:2.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small little library that was created by pulling out some common
code out of indicator-applet.

It passes a menu structure across DBus so that a program can create a
menu simply without worrying about how it is displayed on the other
side of the bus.

%description -l pl.UTF-8
Mała biblioteka utworzona poprzez wydobycie części wspólnego kodu z
pakietu indicator-applet.

Przekazuje strukturę menu poprzez DBus, dzięki czemu program może w
prosty sposób utworzyć menu, bez wnikania w sposób jego wyświetlania
po drugiej stronie szyny.

%package devel
Summary:	Development files for libdbusmenu-glib library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libdbusmenu-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26

%description devel
Header and other development files for libdbusmenu-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz inne programistyczne dla biblioteki
libdbusmenu-glib.

%package static
Summary:	Static libdbusmenu-glib library
Summary(pl.UTF-8):	Statyczna biblioteka libdbusmenu-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdbusmenu-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka libdbusmenu-glib.

%package -n vala-libdbusmenu
Summary:	Vala API for libdbusmenu-glib library
Summary(pl.UTF-8):	API języka Vala do biblioteki libdbusmenu-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libdbusmenu
Vala API for libdbusmenu-glib library.

%description -n vala-libdbusmenu -l pl.UTF-8
API języka Vala do biblioteki libdbusmenu-glib.

%package apidocs
Summary:	API documentation for libdbusmenu-glib library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdbusmenu-glib
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libdbusmenu-glib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdbusmenu-glib.

%package jsonloader
Summary:	Library to load JSON descriptions of menus
Summary(pl.UTF-8):	Biblioteka do wczytywania opisów menu w formacie JSON
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	json-glib >= 0.13.4

%description jsonloader
A small library to load JSON descriptions of menus. Mostly for
testing.

%description jsonloader -l pl.UTF-8
Mała biblioteka do wczytywania opisów menu w formacie JSON. Głównie do
celów testowych.

%package jsonloader-devel
Summary:	Header files for libdbusmenu-jsonloader
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdbusmenu-jsonloader
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-jsonloader = %{version}-%{release}
Requires:	json-glib-devel >= 0.13.4

%description jsonloader-devel
Header files for libdbusmenu-jsonloader.

%description jsonloader-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdbusmenu-jsonloader.

%package jsonloader-static
Summary:	Static libdbusmenu-jsonloader library
Summary(pl.UTF-8):	Statyczna biblioteka libdbusmenu-jsonloader
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description jsonloader-static
Static libdbusmenu-jsonloader library.

%description jsonloader-static -l pl.UTF-8
Statyczna biblioteka libdbusmenu-jsonloader.

%package gtk2
Summary:	libdbusmenu-gtk (GTK+ 2.x based) library
Summary(pl.UTF-8):	Biblioteka libdbusmenu-gtk (oparta na GTK+ 2.x)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.16

%description gtk2
libdbusmenu-gtk (GTK+ 2.x based) library.

%description gtk2 -l pl.UTF-8
Biblioteka libdbusmenu-gtk (oparta na GTK+ 2.x).

%package gtk2-devel
Summary:	Header files for libdbusmenu-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdbusmenu-gtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	gtk+2-devel >= 2:2.16

%description gtk2-devel
Header files for libdbusmenu-gtk library.

%description gtk2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdbusmenu-gtk.

%package gtk2-static
Summary:	Static libdbusmenu-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libdbusmenu-gtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description gtk2-static
Static libdbusmenu-gtk library.

%description gtk2-static -l pl.UTF-8
Statyczna biblioteka libdbusmenu-gtk.

%package -n vala-libdbusmenu-gtk2
Summary:	Vala API for libdbusmenu-gtk (GTK+ 2.x based) library
Summary(pl.UTF-8):	API języka Vala do biblioteki libdbusmenu-gtk (opartej na GTK+ 2.x)
Group:		Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}
Requires:	vala-libdbusmenu = %{version}-%{release}

%description -n vala-libdbusmenu-gtk2
Vala API for libdbusmenu-gtk (GTK+ 2.x based) library.

%description -n vala-libdbusmenu-gtk2 -l pl.UTF-8
API języka Vala do biblioteki libdbusmenu-gtk (opartej na GTK+ 2.x).

%package gtk3
Summary:	libdbusmenu-gtk3 library
Summary(pl.UTF-8):	Biblioteka libdbusmenu-gtk3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.0

%description gtk3
libdbusmenu-gtk3 library.

%description gtk3 -l pl.UTF-8
Biblioteka libdbusmenu-gtk3.

%package gtk3-devel
Summary:	Header files for libdbusmenu-gtk3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdbusmenu-gtk3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	gtk+3-devel >= 3.0

%description gtk3-devel
Header files for libdbusmenu-gtk3 library.

%description gtk3-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdbusmenu-gtk3.

%package gtk3-static
Summary:	Static libdbusmenu-gtk3 library
Summary(pl.UTF-8):	Statyczna biblioteka libdbusmenu-gtk3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description gtk3-static
Static libdbusmenu-gtk3 library.

%description gtk3-static -l pl.UTF-8
Statyczna biblioteka libdbusmenu-gtk3.

%package -n vala-libdbusmenu-gtk3
Summary:	Vala API for libdbusmenu-gtk3 library
Summary(pl.UTF-8):	API języka Vala do biblioteki libdbusmenu-gtk3
Group:		Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}
Requires:	vala-libdbusmenu = %{version}-%{release}

%description -n vala-libdbusmenu-gtk3
Vala API for libdbusmenu-gtk3 library.

%description -n vala-libdbusmenu-gtk3 -l pl.UTF-8
API języka Vala do biblioteki libdbusmenu-gtk3.

%package gtk-apidocs
Summary:	API documentation for libdbusmenu-gtk library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdbusmenu-gtk
Group:		Documentation

%description gtk-apidocs
API documentation for libdbusmenu-gtk library (both GTK+ 2.x and 3.x
based).

%description gtk-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdbusmenu-gtk (zarówno w wersji dla GTK+
2.x, jak i 3.x).

%prep
%setup -q

%{__sed} -i -e 's/-Werror/-Werror -Wno-error=deprecated-declarations/' \
	tools/Makefile.am \
	tools/testapp/Makefile.am

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

for gtkver in %{?with_gtk2:2} %{?with_gtk3:3} %{!?with_gtk2:%{!?with_gtk3:none}} ; do
install -d build-gtk${gtkver}
cd build-gtk${gtkver}
../%configure \
	%{!?with_gtk2:%{!?with_gtk3:--disable-gtk}} \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{!?with_vala:--disable-vala} \
	--enable-introspection \
	--with-gtk=${gtkver} \
	--with-html-dir=%{_gtkdocdir}
# --enable-gtk-doc is broken
%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for dir in build-gtk* ; do
%{__make} -C $dir install -j1 \
	DESTDIR=$RPM_BUILD_ROOT
done

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	jsonloader -p /sbin/ldconfig
%postun	jsonloader -p /sbin/ldconfig

%post	gtk2 -p /sbin/ldconfig
%postun	gtk2 -p /sbin/ldconfig

%post	gtk3 -p /sbin/ldconfig
%postun	gtk3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libdbusmenu-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-glib.so.4
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dbusmenu-bench
%attr(755,root,root) %{_libdir}/dbusmenu-dumper
%attr(755,root,root) %{_libdir}/dbusmenu-testapp
%attr(755,root,root) %{_libdir}/libdbusmenu-glib.so
%dir %{_includedir}/libdbusmenu-glib-0.4
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%{_pkgconfigdir}/dbusmenu-glib-0.4.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/json
%{_datadir}/%{name}/json/test-gtk-label.json

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdbusmenu-glib.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libdbusmenu-glib

%if %{with vala}
%files -n vala-libdbusmenu
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi
%endif

%files jsonloader
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-jsonloader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-jsonloader.so.4

%files jsonloader-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-jsonloader.so
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader
%{_pkgconfigdir}/dbusmenu-jsonloader-0.4.pc

%if %{with static_libs}
%files jsonloader-static
%defattr(644,root,root,755)
%{_libdir}/libdbusmenu-jsonloader.a
%endif

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-gtk.so.4
%{_libdir}/girepository-1.0/DbusmenuGtk-0.4.typelib

%files gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-gtk.so
%{_includedir}/libdbusmenu-gtk-0.4
%{_datadir}/gir-1.0/DbusmenuGtk-0.4.gir
%{_pkgconfigdir}/dbusmenu-gtk-0.4.pc

%if %{with static_libs}
%files gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libdbusmenu-gtk.a
%endif

%if %{with vala}
%files -n vala-libdbusmenu-gtk2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/DbusmenuGtk-0.4.vapi
%endif
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-gtk3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-gtk3.so.4
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-gtk3.so
%{_includedir}/libdbusmenu-gtk3-0.4
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%{_pkgconfigdir}/dbusmenu-gtk3-0.4.pc

%if %{with static_libs}
%files gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libdbusmenu-gtk3.a
%endif

%if %{with vala}
%files -n vala-libdbusmenu-gtk3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi
%endif
%endif

%if %{with gtk2} || %{with gtk3}
%files gtk-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libdbusmenu-gtk
%endif
