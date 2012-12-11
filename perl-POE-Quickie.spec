%define upstream_name    POE-Quickie
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A lazy way to wrap blocking code and programs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Filter::Stream)
BuildRequires:	perl(POE::Session)
BuildRequires:	perl(POE::Wheel::Run)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Deep)
BuildArch:	noarch

%description
If you need nonblocking access to an external program, or want to execute
some blocking code in a separate process, but you don't want to write a
wrapper module or some POE::Wheel::Run boilerplate code, then POE::Quickie
can help. You just specify what you're interested in (stdout, stderr,
and/or exit code), and POE::Quickie will handle the rest in a sensible way.

It has some convenience features, such as killing processes after a
timeout, and storing process-specific context information which will be
delivered with every event.

There is also an even lazier API which suspends the execution of your event
handler and gives control back to POE while your task is running, the same
way LWP::UserAgent::POE does. This is provided by the /FUNCTIONS functions
which are exported by default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 682143
- update to new version 0.17

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1
+ Revision: 677433
- update to new version 0.16

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 662201
- update to new version 0.14

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 660011
- update to new version 0.13

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.120.0-4
+ Revision: 658279
- rebuild
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2
+ Revision: 657810
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 624901
- import perl-POE-Quickie

