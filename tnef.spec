Summary: Decodes MS-TNEF attachments.

Name: tnef
Version: 0.15
Release: 1
Group: Mail/Encoders
Copyright: GPL
Source: http://world.std.com/~damned/tnef-%{version}.tar.gz

%description
TNEF is a program for unpacking MIME attachments of type
"application/ms-tnef". This is a Microsoft only attachment.

Due to the proliferation of Microsoft Outlook and Exchange mail servers,
more and more mail is encapsulated into this format.

The TNEF program allows one to unpack the attachments which were
encapsulated into teh TNEF attachment.  Thus alleviating the need to use
Microsoft Outlook to view the attachment.

%prep
%setup

%build
./configure --prefix=/usr/local
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/bin/tnef
