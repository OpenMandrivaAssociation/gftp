%define	name	gftp
%define version 2.0.18
%define release %mkrel 9

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

Source0:	http://www.gftp.org/%{name}-%{version}.tar.bz2
Source1:	%{name}.icons.tar.bz2
Patch0:		%{name}-2.0.18-datetime-fixedsort.patch
Patch1:		%{name}-2.0.18-bookmarks.patch
#(nl):	This patch fix crash of bookmarks when edited twice (Patch from gftp cvs) 
Patch2:         %{name}-2.0.18-fix-bookmark-crash.patch
#(nl):	This patch fix crash when stopping a transfert (Patch from gftp cvs)
Patch3:         gftp-2.0.18-fix-crash-download.patch
#(ea):	Fixes freeze at startup from FC7 rawhide
Patch4:		gftp-2.0.18-fix-startup-freeze.patch
#(nl)  CVE-2007-3961 and CVE-2007-3962
Patch5:         gftp-2.0.18-CVE-2007-3961-CVE-2007-3962.patch
Patch6:         gftp-2.0.18-fix-desktop-file.patch
%description
gFTP is a multithreaded FTP client for X Window written using Gtk. It features
simultaneous downloads, resuming of interrupted file transfers, file transfer
queues, downloading of entire directories, ftp proxy support, remote directory
caching, passive and non-passive file transfers, drag-n-drop, bookmarks menu,
stop button, and many more features.


%prep
%setup -q -a 1
%patch0 -p0
%patch1 -p1 -b .bookmarks
%patch2 -p1 -b .fix-bookmarks-crash
%patch3 -p1 -b .fix_calculating_bug
%patch4	-p1 -b .fix-startup-freeze
%patch5 -p1 -b .CVE_2007_3961_CVE_2007_3962
%patch6 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

# icons
install -D -m 644 %{name}-48.png $RPM_BUILD_ROOT%_liconsdir/%{name}.png
install -D -m 644 %{name}-32.png $RPM_BUILD_ROOT%_iconsdir/%{name}.png
install -D -m 644 %{name}-16.png $RPM_BUILD_ROOT%_miconsdir/%{name}.png

# locale files
%find_lang %{name}


%post
%{update_menus}

%postun
%{clean_menus}

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
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png



