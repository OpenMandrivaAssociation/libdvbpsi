%define major	10
%define libname	%mklibname dvbpsi %{major}
%define devname %mklibname -d dvbpsi

Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Name:		libdvbpsi
Version:	1.3.3
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.videolan.org/libdvbpsi/
Source0:	http://www.videolan.org/pub/videolan/libdvbpsi/%{version}/%{name}-%{version}.tar.bz2

%description
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %{libname}
Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %{devname}
Summary:	Development tools for programs which will use the libdvbpsi library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the header files and development libraries
necessary for developing programs which will manipulate MPEG 2 and DVB PSI
information using the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--enable-release \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdvbpsi.so.%{major}*

%files -n %{devname}
%doc AUTHORS README COPYING ChangeLog
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}.pc

