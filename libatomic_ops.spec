Summary:	Atomic operations implementation
Summary(pl.UTF-8):	Implementacja operacji atomowych
Name:		libatomic_ops
Version:	7.8.2
Release:	1
License:	MIT-like (libatomic_ops), GPL v2+ (libatomic_ops_gpl)
Group:		Libraries
#Source0Download: https://github.com/ivmai/libatomic_ops/wiki/Download
Source0:	https://github.com/ivmai/libatomic_ops/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d07b3d8369d7f9efdca59f7501dd1117
URL:		https://github.com/ivmai/libatomic_ops/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides implementations for atomic memory update operations on a
number of architectures. This allows direct use of these in reasonably
portable code. Unlike earlier similar packages, this one explicitly
considers memory barrier semantics, and allows the construction of
code that involves minimum overhead across a variety of architectures.

%description -l pl.UTF-8
Pakiet udostępnia implementacja atomowych operacji uaktualnień pamięci
dla wielu architektur. Pozwala to na ich bezpośrednie wykorzystanie we
w miarę przenośnym kodzie. W przeciwieństwie do innych podobnych
pakietów ten uwzględnia semantykę barier pamięciowych i pozwala na
konstruowanie kodu na wielu różnych architekturach z minimalnym
narzutem.

%package devel
Summary:	Header files for libatomic_ops libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libatomic_ops
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libatomic_ops libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libatomic_ops.

%package static
Summary:	Static libatomic_ops libraries
Summary(pl.UTF-8):	Statyczne biblioteki libatomic_ops
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libatomic_ops libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libatomic_ops.

%prep
%setup -q

%build
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatomic*.la
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libatomic_ops/{AUTHORS,COPYING,ChangeLog,LICENSE,README.md,README*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.md README_details.txt README_malloc.txt README_stack.txt
%attr(755,root,root) %{_libdir}/libatomic_ops.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatomic_ops.so.1
%attr(755,root,root) %{_libdir}/libatomic_ops_gpl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatomic_ops_gpl.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatomic_ops.so
%attr(755,root,root) %{_libdir}/libatomic_ops_gpl.so
%{_includedir}/atomic_ops*.h
%{_includedir}/atomic_ops
%{_pkgconfigdir}/atomic_ops.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libatomic_ops.a
%{_libdir}/libatomic_ops_gpl.a
