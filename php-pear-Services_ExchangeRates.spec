%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	ExchangeRates
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - performs currency conversion
Summary(pl):	%{_pearname} - konwersja mi�dzy walutami
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0719b90dd9b881c4f99fd5f37b14604d
URL:		http://pear.php.net/package/Services_ExchangeRates/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extendable to work with any source that provides exchange rate data,
this class downloads exchange rates and the name of each currency (US
Dollar, Euro, Maltese Lira, etc.) and converts between any two of the
available currencies (the actual number of currencies supported
depends on the exchange rate feed used).  

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa, rozszerzalna tak, �eby dzia�a�a z dowolnymi �r�d�ami danych
o wsp�czynnikach wymiany, pobiera wsp�czynniki i nazwy ka�dej z
walut (dolara ameryka�skiego, euro, liry malta�skiej itp.) i
konwertuje pomi�dzy dwiema dowolnymi z dost�pnych walut (w�a�ciwa
liczba obs�ugiwanych walut zale�y od u�ywanych �r�de� wsp�czynnik�w
wymiany).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/example.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
