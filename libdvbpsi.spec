%define major		7
%define oname		%{name}

%define libname %mklibname dvbpsi %{major}
%define develname %mklibname -d dvbpsi

Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Name:		libdvbpsi
Version:	0.2.2
Release:	2
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.videolan.org/libdvbpsi/
Source:		http://www.videolan.org/pub/videolan/libdvbpsi/%{version}/%{oname}-%{version}.tar.bz2

%description
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %{libname}
Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Group:		System/Libraries
Provides:	%{name}

%description -n %{libname}
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %{develname}
Summary:	Development tools for programs which will use the libdvbpsi library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d dvbpsi 4} < 0.2.2

%description -n %{develname}
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate MPEG 2 and DVB PSI
information using the %{name} library.

If you are going to develop programs which will manipulate MPEG 2 and DVB PSI
information you should install %{name}-devel.  You'll also need to have
the %{name} package installed.


%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x \
	--enable-release \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS README COPYING ChangeLog
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Nov 03 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.2-1mdv2012.0
+ Revision: 716270
- update to new version 0.2.2

* Thu Sep 01 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.1-1
+ Revision: 697687
- update to new version 0.2.1

* Thu May 05 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.0-1
+ Revision: 669496
- new version
- new major

* Fri Sep 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.7-1mdv2011.0
+ Revision: 577042
- new version
- new major
- update file list

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.6-4mdv2010.0
+ Revision: 429724
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.1.6-3mdv2009.0
+ Revision: 248642
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.6-1mdv2008.1
+ Revision: 101139
- new version
- new major
- new devel name

  + Thierry Vignaud <tv@mandriva.org>
    - s/Mandrake/Mandriva/

* Mon Jul 30 2007 David Walluck <walluck@mandriva.org> 0.1.5-3mdv2008.0
+ Revision: 56758
- rebuild to fix %%mkrel
- Import libdvbpsi



* Thu Jul  7 2005 Götz Waschk <waschk@mandriva.org> 0.1.5-2mdk
- backport support

* Thu Jul  7 2005 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdk
- reenable libtoolize
- major 4
- New release 0.1.5

* Thu Feb 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.4-2mdk
- support mdk 9.0

* Sun Jan  4 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.4-1mdk
- spec fixes
- don't libtoolize
- major 3
- new version

* Wed Jul 30 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.3-1mdk
- throw out packager tag
- mklibname fixes
- new version

* Fri Jul 11 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.2-5mdk
- fix description (thanks to Adam Williamson)

* Thu Jul 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.2-4mdk
- autoconf 2.5 macro
- mklibname macro

* Wed Jan 08 2003 Yves Duret <yves@zarb.org> 0.1.2-3mdk
- rebuild.

* Fri Dec 13 2002 Yves Duret <yves@zarb.org> 0.1.2-2mdk
- s#Copyright#License#
- include the libtool .la files.
- use macros.
- update URL: tag.

* Fri Oct 11 2002 Samuel Hocevar <sam@zoy.org>
- 0.1.2 release.

* Sat May 18 2002 Arnaud de Bossoreille de Ribou <bozo@via.ecp.fr>
- 0.1.1 release.

* Mon Apr 8 2002 Arnaud de Bossoreille de Ribou <bozo@via.ecp.fr>
- split into two separate packages.

* Thu Apr 4 2002 Jean-Paul Saman <saman@natlab.research.philips.com>
- first version of package for redhat systems.
