%define		status		beta
%define		pearname	Services_ExchangeRates
Summary:	%{pearname} - performs currency conversion
Summary(pl.UTF-8):	%{pearname} - konwersja między walutami
Name:		php-pear-%{pearname}
Version:	0.8.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	4b19b31222496c465fc3bdedc414bfbd
URL:		http://pear.php.net/package/Services_ExchangeRates/
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Cache_Lite
Requires:	php-pear-HTTP_Request2
Requires:	php-pear-XML_Serializer >= 0.20.0
Requires:	php-pear-XML_Tree >= 2.0.0-0.RC2
Obsoletes:	php-pear-Services_ExchangeRates-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extendable to work with any source that provides exchange rate data,
this class downloads exchange rates and the name of each currency (US
Dollar, Euro, Maltese Lira, etc.) and converts between any two of the
available currencies (the actual number of currencies supported
depends on the exchange rate feed used).

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta klasa, rozszerzalna tak, żeby działała z dowolnymi źródłami danych
o współczynnikach wymiany, pobiera współczynniki i nazwy każdej z
walut (dolara amerykańskiego, euro, liry maltańskiej itp.) i
konwertuje pomiędzy dwiema dowolnymi z dostępnych walut (właściwa
liczba obsługiwanych walut zależy od używanych źródeł współczynników
wymiany).

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

install -d examples
mv docs/%{pearname}/*.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/*.php
%{php_pear_dir}/Services/ExchangeRates
%{php_pear_dir}/data/Services_ExchangeRates
%{_examplesdir}/%{name}-%{version}
