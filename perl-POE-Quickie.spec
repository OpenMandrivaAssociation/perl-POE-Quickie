%define upstream_name    POE-Quickie
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A lazy way to wrap blocking code and programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Filter::Stream)
BuildRequires: perl(POE::Session)
BuildRequires: perl(POE::Wheel::Run)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


