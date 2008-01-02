%define major		5
%define oname		%{name}%major

%define libname %mklibname dvbpsi %major
%define develname %mklibname -d dvbpsi

Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Name:		libdvbpsi
Version:	0.1.6
Release:	%mkrel 1
License:	GPL
URL:		http://www.videolan.org/libdvbpsi/
Group:		System/Libraries
Source:		http://www.videolan.org/pub/videolan/libdvbpsi/%{version}/%{oname}-%{version}.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %{libname}
Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Group:		System/Libraries
Provides:	%name

%description -n %{libname}
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %develname
Summary:	Development tools for programs which will use the libdvbpsi library
Group:		Development/C
Provides:	%name-devel = %version-%release
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d dvbpsi 4

%description -n %develname
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate MPEG 2 and DVB PSI
information using the %{name} library.

If you are going to develop programs which will manipulate MPEG 2 and DVB PSI
information you should install %{name}-devel.  You'll also need to have
the %name package installed.


%prep
%setup -q -n %oname-%version

%build
%if %mdkversion <= 1000
%define __libtoolize true
%endif
%configure2_5x --enable-release
%make 

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS README COPYING ChangeLog
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*a
%{_libdir}/*.so
%{_includedir}/*
