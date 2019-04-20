#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Fennec-Lite
Version  : 0.004
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Fennec-Lite-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Fennec-Lite-0.004.tar.gz
Summary  : 'Minimalist Fennec, the commonly used bits.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Fennec::Lite - Minimalist Fennec, the commonly used bits.
DESCRIPTION
Fennec does a ton, but it may be hard to adopt it all at once. It also
is a large project, and has not yet been fully split into component
projects. Fennec::Lite takes a minimalist approach to do for Fennec what
Mouse does for Moose.

%package dev
Summary: dev components for the perl-Fennec-Lite package.
Group: Development
Provides: perl-Fennec-Lite-devel = %{version}-%{release}

%description dev
dev components for the perl-Fennec-Lite package.


%prep
%setup -q -n Fennec-Lite-0.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Fennec/Lite.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Fennec::Lite.3
