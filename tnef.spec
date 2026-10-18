#
# Conditional build:
%bcond_without	tests		# build with tests

Summary:	Decodes MS-TNEF attachments
Summary(pl.UTF-8):	Dekoder załączników w formacie MS-TNEF
Summary(ru.UTF-8):	Программа для распаковки аттачментов MIME типа "application/ms-tnef"
Summary(uk.UTF-8):	Програма для розпаковки атачментів MIME типу "application/ms-tnef"
Name:		tnef
Version:	1.4.18
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	https://github.com/verdammelt/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c18c0166aaf5d19355394515978480e6
Patch0:		%{name}-attr_read-prototype.patch
Patch1:		%{name}-CVE-2026-103678.patch
Patch2:		%{name}-CVE-2026-103679.patch
Patch3:		%{name}-CVE-2026-103680.patch
URL:		https://github.com/verdammelt/%{name}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%if %{with tests}
BuildRequires:	diffutils
%endif
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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%if %{with tests}
# tests share one working directory, so they cannot run in parallel
%{__make} -j1 check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README.md THANKS doc/{FAQ,file-format.txt}
%attr(755,root,root) %{_bindir}/tnef
%{_mandir}/man1/tnef.1*
