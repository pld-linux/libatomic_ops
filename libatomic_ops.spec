Summary:	Atomic operations implementation
Summary(pl.UTF-8):	Implementacja operacji atomowych
Name:		libatomic_ops
# NOTE: 7.4.0 is considered experimental (as of Nov 2013)
Version:	7.2e
Release:	2
License:	MIT-like (libatomic_ops), GPL v2+ (libatomic_ops_gpl)
Group:		Development/Libraries
#Source0Download http://www.hpl.hp.com/research/linux/atomic_ops/download.php4
Source0:	http://www.hpl.hp.com/research/linux/atomic_ops/download/%{name}-%{version}.tar.gz
# Source0-md5:	7035692fec4db2659b06485040829e43
URL:		http://www.hpl.hp.com/research/linux/atomic_ops/
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
