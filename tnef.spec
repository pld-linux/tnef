Summary:	Decodes MS-TNEF attachments
Summary(pl):	Dekoder za��cznik�w w formacie MS-TNEF
Summary(ru):	��������� ��� ���������� ����������� MIME ���� "application/ms-tnef"
Summary(uk):	�������� ��� ���������� �������Ԧ� MIME ���� "application/ms-tnef"
Name:		tnef
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/tnef/%{name}-%{version}.tar.gz
# Source0-md5:	db3abfbd0ddec0e141afec1f503171c6
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
TNEF jest programem rozpakowuj�cym za��czniki MIME w formacie
"application/ms-tnef". S� to za��czniki specyficzne dla firmy
Microsoft.

Poniewa� jest to format stosowany przez programy Microsoft Outlook i
Microsoft Exchange coraz wi�cej przesy�ek korzysta z niego.

Program TNEF umo�liwia rozpakowanie za��cznik�w opakowanych w
za��cznik TNEF. Powoduje to, �e nie jest konieczne u�ycie programu
Microsoft Outlook do odczytania za��cznika.

%description -l ru
TNEF - ��� ��������� ��� ���������� ����������� MIME ����
"application/ms-tnef". ���� ��� ������������ �������������
Microsoft'��.

%description -l uk
TNEF - �� �������� ��� ���������� �������Ԧ� MIME ����
"application/ms-tnef". ��� ��� ����������դ���� �������� Microsoft'��.

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
%{_mandir}/man1/*
