%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	ExchangeRates
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - performs currency conversion
Summary(pl):	%{_pearname} - konwersja miêdzy walutami
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	2.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0719b90dd9b881c4f99fd5f37b14604d
URL:		http://pear.php.net/package/Services_ExchangeRates/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Ta klasa, rozszerzalna tak, ¿eby dzia³a³a z dowolnymi ¼ród³ami danych
o wspó³czynnikach wymiany, pobiera wspó³czynniki i nazwy ka¿dej z
walut (dolara amerykañskiego, euro, liry maltañskiej itp.) i
konwertuje pomiêdzy dwiema dowolnymi z dostêpnych walut (w³a¶ciwa
liczba obs³ugiwanych walut zale¿y od u¿ywanych ¼róde³ wspó³czynników
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
