Summary:	Pretty version of df(1) command
Summary(pl):	�adna wersja polecenia df(1)
Name:		discus
Version:	0.2.9
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Console
Source0:	http://www.raincrazy.com/software/discus/%{name}-%{version}.tar.gz
# Source0-md5:	bcc4a08d03a0952b0b744655c45b04b8
URL:		http://www.raincrazy.com/software/discus/
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Discus aims to make df prettier, with features such as color, graphs,
and smart formatting of numbers (automatically choosing the most
suitable size from kilobytes, megabytes, gigabytes, or terabytes). If
you don't want Discus deciding the best sizes, you can also choose
your own increments, along with specifying the number of decimal
places you'd like to see.

%description -l pl
Discus zamierza uczyni� df pi�kniejszym, poprzez kolor, wykresy i
eleganckie formatowanie liczb (automatycznie wybieraj�c najbardziej
odpowiedni� wielko�� z kilobajt�w, megabajt�w, gigabajt�w lub
terabajt�w). Je�eli nie chcesz, �eby Discus decydowa� o najlepszej
wielko�ci, mo�esz te� wybra� w�asne przyrosty, po przez podanie
liczby miejsc dziesi�tnych, kt�re chcia�by� widzie�.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}rc	$RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS changelog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/*
