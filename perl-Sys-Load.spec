%define upstream_name    Sys-Load
%define upstream_version 0.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	A perl5 module that indicate system load
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BA/BARABAS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
getload() returns 3 elements: representing load averages over 
the last 1, 5 and 15 minutes. On failure empty list is returned.
uptime() returns the system uptime in seconds. Returns 0 on 
failure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
