Summary:	Utilities for smartcard readers
Summary(pl):	Narzêdzia do czytników kart procesorowych
Name:		smartsession
Version:	1.9.11
Release:	1
License:	BSD-like + restricted vendor's name usage (see copyright file)
Group:		Applications
Source0:	http://www.gemplus.com/techno/smartsession/download/%{name}_%{version}.tar.gz
Patch0:		%{name}-use_gdbm.patch
URL:		http://www.gemplus.com/techno/smartsession/
BuildRequires:	gtk+-devel
BuildRequires:	pam-devel
BuildRequires:	pcsc-lite-devel
Obsoletes:	%{name}-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SmartSession is a set of binaries and modules able to secure a Linux
session using smartcards (authenticate, store CFS secret passphrase).

%description -l pl
SmartSession to zestaw programów i modu³ów umo¿liwiaj±cych ochronê
sesji z Linuksem przy u¿yciu kart procesorowych (uwierzytelnianie,
przechowywanie kodów dostêpu do szyfrowanych systemów plików).

%package xsst
Summary:	X Smart Session tool
Summary(pl):	Narzêdzie Smart Session pod X
Group:		X11/Applications
Requires:	%{name} = %{version}

%description xsst
X Smart Session tool: manages smartsession smartcard and pam_smartcard
PAM module.

%description xsst -l pl
Narzêdzie Smart Session pod X - zarz±dzaj±ce kartami procesorowymi i
modu³em PAM pam_smartcard.

%package pam
Summary:	smartsession PAM autorization module
Summary(pl):	Modu³ autoryzacji smartsession dla PAM
Group:		Libraries

%description pam
You need this in order to use cards insted of passwords.

%description pam -l pl
Modu³ ten jest potrzebny, aby logowaæ siê wk³adaj±c kartê zamiast
wpisywania has³a.

%prep
%setup -qn smartsession
%patch0 -p0

%build
%{__make} -C src \
	FLAGS="%{rpmcflags} -Wall -fPIC"

%install
install -d $RPM_BUILD_ROOT{%{_mandir}/man{1,5,8},%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_examplesdir}/%{name},/lib/security}

install src/Cfs_SC/{cmkdir,cattach,cdetach,crescue}_SC $RPM_BUILD_ROOT%{_bindir}
install src/Graphic/xsst $RPM_BUILD_ROOT%{_sbindir}
install src/Locker/{autolock,smartlocker} $RPM_BUILD_ROOT%{_sbindir}
install src/Pam_Modules/pam_{smartcard,cfs_SC}.so $RPM_BUILD_ROOT/lib/security
install src/Tools/{sst,chpin,autolock_ctrl} $RPM_BUILD_ROOT%{_sbindir}

install man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo '.so cfs_SC.1' > $RPM_BUILD_ROOT%{_mandir}/man1/cattach_SC.1
echo '.so cfs_SC.1' > $RPM_BUILD_ROOT%{_mandir}/man1/cdetach_SC.1
echo '.so cfs_SC.1' > $RPM_BUILD_ROOT%{_mandir}/man1/cmkdir_SC.1

install Misc/{Makefile.patch,smartlocker_pam_config,README,erase_gpk8k,\
gdm.patch,get_name_in_card.sh,script_test} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO copyright
%attr(755,root,root) %{_sbindir}/autolock*
%attr(755,root,root) %{_sbindir}/chpin
%attr(755,root,root) %{_sbindir}/smartlocker
%attr(755,root,root) %{_sbindir}/sst
%attr(755,root,root) %{_bindir}/cattach_SC
%attr(755,root,root) %{_bindir}/cdetach_SC
%attr(755,root,root) %{_bindir}/cmkdir_SC
%attr(755,root,root) %{_bindir}/crescue_SC
%{_mandir}/man1/*.1*
%{_mandir}/man5/cfs_fstab.5*
%{_mandir}/man5/smartsession.5*
%{_mandir}/man8/autolock*.8*
%{_mandir}/man8/crescue_SC.8*
%{_mandir}/man8/sst.8*
%{_examplesdir}/%{name}

%files xsst
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/xsst
%{_mandir}/man8/xsst.8*

%files pam
%defattr(644,root,root,755)
%attr(755,root,root) /lib/security/pam_cfs_SC.so
%attr(755,root,root) /lib/security/pam_smartcard.so
%{_mandir}/man5/pam_cfs_SC.5*
%{_mandir}/man5/pam_smartcard.5*
