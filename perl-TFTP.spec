
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	TFTP
Summary:	TFTP - Pure perl TFTP implementation
Name:		perl-TFTP
Version:	1.0b3
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	0c62ec431f745ca177ab01df3292c803
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a perl module (completely implemented in perl) to
provide the client functionality of the TFTP protocol as described in
rfc783. A class, TFTP, is available which encapsulates the persistent
aspects of a TFTP connection and from which the basic TFTP operations
(get,put) can be initiated.


%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/TFTP.pm
%{_mandir}/man3/*
