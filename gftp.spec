%define	name	gftp
%define version 2.0.19
%define release %mkrel 4

Name:		%{name}
Summary:	Multithreaded FTP client for X Windows
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	GPL
Group:		Networking/File transfer
URL:		http://www.gftp.org/
Requires:	gtk+2 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel

Source0:	http://www.gftp.org/%{name}-%{version}.tar.gz
Source1:	%{name}.icons.tar.bz2
Patch0:		%{name}-2.0.19-datetime-fixedsort.patch
Patch1:		%{name}-2.0.18-bookmarks.patch
Patch6:     gftp-2.0.19-fix-desktop-file.patch
patch7:     gftp-2.0.19-fix-crash.patch
     
%description
gFTP is a multithreaded FTP client for X Window written using Gtk. It features
simultaneous downloads, resuming of interrupted file transfers, file transfer
queues, downloading of entire directories, ftp proxy support, remote directory
caching, passive and non-passive file transfers, drag-n-drop, bookmarks menu,
stop button, and many more features.


%prep
%setup -q -a 1
%patch1 -p1 -b .bookmarks
%patch6 -p0
%patch7 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

# locale files
%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS THANKS COPYING ChangeLog README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man?/*
