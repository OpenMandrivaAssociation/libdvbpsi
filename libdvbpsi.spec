%define major		4
%define oname		%{name}%major
%define mdkversion		%(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandrake-release)
%if %mdkversion >= 910
%define lib_name	%mklibname dvbpsi %{major}
%define lib_name_devel  %mklibname dvbpsi %{major} -d
%else
%define lib_name	libdvbpsi%{major}
%define lib_name_devel  libdvbpsi%{major}-devel
%endif
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}


Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Name:		libdvbpsi
Version:	0.1.5
Release:	%mkrel 3
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

%package -n %{lib_name}
Summary:	A library for decoding and generating MPEG 2 and DVB PSI sections
Group:		System/Libraries
Provides:	%name

%description -n %{lib_name}
libdvbpsi is a simple library designed for decoding and generating
MPEG 2 TS and DVB PSI tables. The important features are:
 * PAT decoder and generator.
 * PMT decoder and generator.

%package -n %lib_name_devel
Summary:	Development tools for programs which will use the libdvbpsi library
Group:		Development/C
Provides:	%name-devel
Requires:	%{lib_name} = %{version}

%description -n %lib_name_devel
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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc AUTHORS README COPYING ChangeLog
%{_libdir}/*.so.*

%files -n %lib_name_devel
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*a
%{_libdir}/*.so
%{_includedir}/*
