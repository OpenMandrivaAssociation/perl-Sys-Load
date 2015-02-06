%define upstream_name    Sys-Load
%define upstream_version 0.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.200.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-3mdv2011.0
+ Revision: 556152
- rebuild for perl 5.12

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.200.0-2mdv2010.0
+ Revision: 430548
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2-7mdv2009.0
+ Revision: 258423
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2009.0
+ Revision: 246487
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2008.1
+ Revision: 152318
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.2-3mdv2008.0
+ Revision: 23836
- rebuild


* Mon Nov 14 2005 Nicolas Chipaux <chipaux@mandriva.com> 0.2-1mdk
- initial mdv version

