#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	TFTP
Summary:	TFTP - pure Perl TFTP implementation
Summary(pl):	TFTP - czysto perlowa implementacja TFTP
Name:		perl-TFTP
Version:	1.0b3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	0c62ec431f745ca177ab01df3292c803
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl module (completely implemented in Perl) to provide the
client functionality of the TFTP protocol as described in RFC 783. A
class, TFTP, is available which encapsulates the persistent aspects of
a TFTP connection and from which the basic TFTP operations (get, put)
can be initiated.

%description -l pl
To jest modu³ Perla (zaimplementowany ca³kowicie w Perlu)
dostarczaj±cy funkcjonalno¶æ klienta protoko³u TFTP opisanego w RFC
783. Zawiera klasê TFTP opakowuj±c± sta³e aspekty po³±czenia TFTP,
która mo¿e zapocz±tkowywaæ podstawowe operacje TFTP (get, put).

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/TFTP.pm
%{_mandir}/man3/*
