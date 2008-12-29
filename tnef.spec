Summary:	Decodes MS-TNEF attachments
Summary(pl.UTF-8):	Dekoder załączników w formacie MS-TNEF
Summary(ru.UTF-8):	Программа для распаковки аттачментов MIME типа "application/ms-tnef"
Summary(uk.UTF-8):	Програма для розпаковки атачментів MIME типу "application/ms-tnef"
Name:		tnef
Version:	1.4.5
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/tnef/%{name}-%{version}.tar.gz
# Source0-md5:	ec46d47525c6afb928642e3edec21058
URL:		http://sourceforge.net/projects/tnef/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TNEF is a program for unpacking MIME attachments of type
"application/ms-tnef". This is a Microsoft only attachment.

Due to the proliferation of Microsoft Outlook and Exchange mail
servers, more and more mail is encapsulated into this format.

The TNEF program allows one to unpack the attachments which were
encapsulated into teh TNEF attachment. Thus alleviating the need to
use Microsoft Outlook to view the attachment.

%description -l pl.UTF-8
TNEF jest programem rozpakowującym załączniki MIME w formacie
"application/ms-tnef". Są to załączniki specyficzne dla firmy
Microsoft.

Ponieważ jest to format stosowany przez programy Microsoft Outlook i
Microsoft Exchange coraz więcej przesyłek korzysta z niego.

Program TNEF umożliwia rozpakowanie załączników opakowanych w
załącznik TNEF. Powoduje to, że nie jest konieczne użycie programu
Microsoft Outlook do odczytania załącznika.

%description -l ru.UTF-8
TNEF - это программа для распаковки аттачментов MIME типа
"application/ms-tnef". Этот тип используется исключительно
Microsoft'ом.

%description -l uk.UTF-8
TNEF - це програма для розпаковки атачментів MIME типу
"application/ms-tnef". Цей тип використовується виключно Microsoft'ом.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/tnef
%{_mandir}/man1/tnef.1*
