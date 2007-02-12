%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	ExchangeRates
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - performs currency conversion
Summary(pl.UTF-8):   %{_pearname} - konwersja między walutami
Name:		php-pear-%{_pearname}
Version:	0.5.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3291031e24c722f2a2bb566db20f94c6
URL:		http://pear.php.net/package/Services_ExchangeRates/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Cache_Lite
Requires:	php-pear-HTTP_Request
Requires:	php-pear-XML_Tree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extendable to work with any source that provides exchange rate data,
this class downloads exchange rates and the name of each currency (US
Dollar, Euro, Maltese Lira, etc.) and converts between any two of the
available currencies (the actual number of currencies supported
depends on the exchange rate feed used).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa, rozszerzalna tak, żeby działała z dowolnymi źródłami danych
o współczynnikach wymiany, pobiera współczynniki i nazwy każdej z
walut (dolara amerykańskiego, euro, liry maltańskiej itp.) i
konwertuje pomiędzy dwiema dowolnymi z dostępnych walut (właściwa
liczba obsługiwanych walut zależy od używanych źródeł współczynników
wymiany).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
