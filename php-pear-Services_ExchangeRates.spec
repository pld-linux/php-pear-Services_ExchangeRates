%include	/usr/lib/rpm/macros.php
%define         _class          Services
%define         _subclass       ExchangeRates
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Performs currency conversion
Summary(pl):	%{_pearname} - Konwersja miêdzy walutami
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5c5de2af32bc09938418cf16872c0919
URL:		http://pear.php.net/package/Services_ExchangeRates/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extendable to work with any source that provides exchange rate data,
this class downloads exchange rates and the name of each currency (US
Dollar, Euro, Maltese Lira, etc.) and converts between any two of the
available currencies (the actual number of currencies supported depends
on the exchange rate feed used).  

This class has in PEAR status: %{_status}.

%description -l pl
...

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
%doc %{_pearname}-%{version}/docs
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
