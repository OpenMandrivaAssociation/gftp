Name:		gftp
Summary:	Multithreaded FTP client for X Windows
Version:	2.9.1b
Release:	1
License:	GPL
Group:		Networking/File transfer
URL:		https://www.gftp.org/
Requires:	gtk+2 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
Source0:	https://github.com/masneyb/gftp/releases/download/%{version}/gftp-%{version}.tar.xz
# Source1:	%{name}.icons.tar.bz2
Patch0:		%{name}-2.0.19-datetime-fixedsort.patch
Patch1:		%{name}-2.0.18-bookmarks.patch
Patch6:     gftp-2.0.19-fix-desktop-file.patch
patch7:     gftp-2.0.19-fix-crash.patch
Patch8:	    gftp-stropts.patch
     
%description
gFTP is a multithreaded FTP client for X Window written using Gtk. It features
simultaneous downloads, resuming of interrupted file transfers, file transfer
queues, downloading of entire directories, ftp proxy support, remote directory
caching, passive and non-passive file transfers, drag-n-drop, bookmarks menu,
stop button, and many more features.


%prep
%setup -q -a 1
%patch 1 -p1 -b .bookmarks
%patch 6 -p0
%patch 7 -p0
%patch 8 -p1

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

# locale files
%find_lang %{name}

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.19-6mdv2011.0
+ Revision: 610848
- rebuild

* Wed Apr 21 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:2.0.19-5mdv2010.1
+ Revision: 537285
- reubuild for new openssl

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1:2.0.19-4mdv2010.0
+ Revision: 437673
- rebuild

* Thu Feb 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:2.0.19-3mdv2009.1
+ Revision: 345336
- rebuild for new readline

* Sun Dec 21 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:2.0.19-2mdv2009.1
+ Revision: 317079
- Fix crash at gftp start

* Mon Dec 01 2008 Funda Wang <fwang@mandriva.org> 1:2.0.19-1mdv2009.1
+ Revision: 308693
- New version 2.0.19
- rediff patches

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1:2.0.18-11mdv2009.0
+ Revision: 245955
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 23 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:2.0.18-9mdv2008.1
+ Revision: 156948
- Add fix for CVE-2007-3961-CVE-2007-3962
  Fix desktop file

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Feb 24 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.18-9mdv2007.0
+ Revision: 125440
- add patch4 to fix freeze at startup

* Sat Aug 12 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1:2.0.18-8mdv2007.0
+ Revision: 55696
- Rebuild

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - fix buildrequires

* Fri Jul 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1:2.0.18-7mdv2007.0
+ Revision: 42305
- Increase release 2.0.18-7mdv2007.0
- Add patch 3: Fix crash when stopping transfert
- Fix crash when editing bookmarks (ticket #10138)

* Sat Jul 01 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1:2.0.18-6mdv2007.0
+ Revision: 38270
- Increase release
- Fix for xdg menu
- import gftp-2.0.18-5mdk

* Thu Nov 17 2005 Thierry Vignaud <tvignaud@mandriva.com> 2.0.18-5mdk
- fix build
- rebuild against openssl-0.9.8a

* Mon Aug 01 2005 Marcel Pol <mpol@mandriva.org> 2.0.18-4mdk
- P1: fix alphabetical order

* Mon Aug 01 2005 Marcel Pol <mpol@mandriva.org> 2.0.18-3mdk
- add Mandriva iso (devel and Official), SRPMS and Old to bookmarks

* Tue Jun 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.18-2mdk
- use %%debug_package
- %%mkrel

* Mon Feb 28 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.0.18-1mdk
- from Tom Ph <tpgww@onepost.net> : 
	- updated icons, including svg
	- requires
	- new version
	- patches reconciled
	- updated icons
	- desktop files directory

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.17-5mdk
- rebuild for new readline

* Wed Oct 13 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.0.17-4mdk
- put back extra 64-bit fixes

* Sat Aug 21 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.17-3mdk
- fix typo in menu entry

* Sat Aug 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0.17-2mdk
- REbuild with new menu

* Thu Apr 08 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.17-1mdk
- new release
- drop patch 2 (merged upstream)
- redo patch 3
