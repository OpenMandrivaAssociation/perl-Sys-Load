%define module Sys-Load

Summary:	A perl5 module that indicate system load
Name:		perl-Sys-Load
Version:	0.2
Release:	%mkrel 7
Source0:	http://search.cpan.org/CPAN/authors/id/B/BA/BARABAS/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}/
License:	Artistic
Group:		Development/Perl
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
getload() returns 3 elements: representing load averages over 
the last 1, 5 and 15 minutes. On failure empty list is returned.
uptime() returns the system uptime in seconds. Returns 0 on 
failure.

%prep
%setup -q -n %{module}-%{version}

# Remove Local from path
find . -type f | xargs perl -p -i -e "s|/usr/local/|/usr/|g"

# lib64 fixes, don't add /usr/lib/X11 to linker search path
perl -pi -e "s|-L/usr/lib/X11||g;s|-L/usr/X11/lib||g;s|-L/usr/lib||g" Makefile.PL
perl -pi -e "s|(/usr/X11R6)/lib|\1/%{_lib}|g" Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
%ifnarch ppc
%{__make} test
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/auto/Sys/Load/Load.so
%{perl_vendorarch}/Sys/Load.pm
%{_mandir}/man3/*

