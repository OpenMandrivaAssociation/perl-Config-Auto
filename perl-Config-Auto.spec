%define upstream_name    Config-Auto
%define upstream_version 0.44
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Magical config file parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Config::IniFiles)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
This module was written after having to write Yet Another Config File
Parser for some variety of colon-separated config. I decided "never again".

Config::Auto aims to be the most 'DWIM' config parser available, by
detecting configuration styles, include paths and even config filenames
automagically.

See the the HOW IT WORKS manpage section below on implementation details.

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
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.360.0-1mdv2011.0
+ Revision: 688738
- update to new version 0.36

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.340.0-1
+ Revision: 653906
- import perl-Config-Auto



