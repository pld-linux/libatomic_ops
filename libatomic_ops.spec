Summary:	Atomic operations implementation
Summary(pl.UTF-8):	Implementacja operacji atomowych
Name:		libatomic_ops
# NOTE: 7.4.x used to be considered experimental until ~2014; see DEVEL branch for now
Version:	7.2g
Release:	1
License:	MIT-like (libatomic_ops), GPL v2+ (libatomic_ops_gpl)
Group:		Development/Libraries
#Source0Download: https://github.com/ivmai/libatomic_ops/wiki/Download
Source0:	http://www.ivmaisoft.com/_bin/atomic_ops/%{name}-%{version}.tar.gz
# Source0-md5:	e6d1c85c90563555f1fde7a0980d41ab
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

%prep
%setup -q -n %{name}-7.2

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/libatomic_ops/{COPYING,LICENSING.txt,README*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README doc/{LICENSING.txt,README.txt,README_malloc.txt,README_stack.txt}
%{_libdir}/libatomic_ops.a
%{_libdir}/libatomic_ops_gpl.a
%{_includedir}/atomic_ops*.h
%{_includedir}/atomic_ops
%{_pkgconfigdir}/atomic_ops.pc
