#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-DataIndenter
Summary:	XML::Filter::DataIndenter - SAX2 indenter for data oriented XML
Summary(pl):	XML::Filter::DataIndenter - tworzenie wciêæ SAX2 dla XML-a z danymi
Name:		perl-XML-Filter-DataIndenter
Version:	0.1
Release:	1
# any version
License:	GPL or Artistic or BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d405dc887307d788648430075c01b47e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Machines
BuildRequires:	perl-XML-SAX-Writer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALPHA CODE ALERT: This is the first release.  Feedback and patches
welcome.

In data oriented XML, leaf elements (those which contain no elements)
contain only character content, all other elements contain only child
elements and ignorable whitespace.  This filter consumes all
whitespace not in leaf nodes and replaces it with whitespace that
indents all elements.  Character data in leaf elements is left
unmolested

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
