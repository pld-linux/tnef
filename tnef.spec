Summary:	Decodes MS-TNEF attachments
Summary(pl):	Dekoder zaЁ╠cznikСw w formacie MS-TNEF
Summary(ru):	Программа для распаковки аттачментов MIME типа "application/ms-tnef"
Summary(uk):	Програма для розпаковки атачмент╕в MIME типу "application/ms-tnef"
Name:		tnef
Version:	1.2.3.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/tnef/%{name}-%{version}.tar.gz
# Source0-md5:	bc0ae13cc68f1595fb8a9c6f706c1e08
URL:		http://sourceforge.net/projects/tnef/
BuildRequires:	autoconf
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

%description -l pl
TNEF jest programem rozpakowuj╠cym zaЁ╠czniki MIME w formacie
"application/ms-tnef". S╠ to zaЁ╠czniki specyficzne dla firmy
Microsoft.

Poniewa© jest to format stosowany przez programy Microsoft Outlook i
Microsoft Exchange coraz wiЙcej przesyЁek korzysta z niego.

Program TNEF umo©liwia rozpakowanie zaЁ╠cznikСw opakowanych w
zaЁ╠cznik TNEF. Powoduje to, ©e nie jest konieczne u©ycie programu
Microsoft Outlook do odczytania zaЁ╠cznika.

%description -l ru
TNEF - это программа для распаковки аттачментов MIME типа
"application/ms-tnef". Этот тип используется исключительно
Microsoft'ом.

%description -l uk
TNEF - це програма для розпаковки атачмент╕в MIME типу
"application/ms-tnef". Цей тип використову╓ться виключно Microsoft'ом.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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
%doc README BUGS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/tnef
%{_mandir}/man1/*
