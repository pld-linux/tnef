Summary:	Decodes MS-TNEF attachments
Summary(pl):	Dekoder za³±czników w formacie MS-TNEF
Name:		tnef
Version:	0.16
Release:	2
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	http://world.std.com/~damned/%{name}-%{version}.tar.gz
URL:		http://world.std.com/~damned/software.html
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
TNEF jest programem rozpakowuj±cym za³±czniki MIME w formacie
"application/ms-tnef". S± to za³±czniki specyficzne dla firmy
Microsoft.

Poniewa¿ jest to format stosowany przez programy Microsoft Outlook i
Microsoft Exchange coraz wiecej przesylek korzysta z niego.

Program TNEF umo¿liwia rozpakowanie za³±czników opakowanych w
za³±cznik TNEF. Powoduje to, ¿e nie jest konieczne u¿ycie programu
Microsoft Outlook do odczytania za³±cznika.

%prep
%setup -q

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README BUGS ChangeLog NEWS TODO
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/file-format.tex tests/*.tnef
%attr(755,root,root) %{_bindir}/tnef
