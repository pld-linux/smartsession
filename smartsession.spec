Summary:	Utilities for smartcard readers
Summary(pl):	Narzêdzia do czytników kart
Name:		smartsession
Version:	1.9.11
Release:	1
License:	Consult w/ www.gemplus.com and file 'copyright'
Group:		Applications
Source0:	%{name}_%{version}.tar.gz
Patch0:		%{name}-use_gdbm.patch
URL:		http://www.gemplus.com/techno/smartsession/
BuildRequires:	pcsc-lite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for managing & creating smardcards (for autorization w/ PAM or
storing GPG/SSL keys in sim-a-like cards).

Sorry but we cannot use name of manufacturer to advertise this
package. See attached copyright file!

%description -l pl
Zabawki do zarz±dzania i formatowania kart smardcard (do autoryzacji
przy u¿yciu PAM lub przechowywania kluczy GPG/SSL w przero¶niêtych
kartach a'la SIM).

Niestety nie mo¿emy u¿ywaæ nazwy producenta czytników w celu reklamy
tego produktu. Nale¿y zapoznaæ siê z do³±czonym plikiem copyright.

%package devel
Summary:	smartsession header files
Summary(pl):	Pliki nag³ówkowe smartsession
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
smartsession header files.

%description devel -l pl
Pliki nag³ówkowe smartsession.

%package tools
Summary:	Tools
Summary(pl):	Narzêdzia
Group:		Applications
Requires:	%{name} = %{version}

%description tools
Simple tools for comunicating w/ smartcard reader.

%description tools -l pl
Proste narzêdzia do komunikacji z czytnikiem kart chipowych.

%package -n smartsession-pam
Summary:	smartsession PAM autorization module
Summary(pl):	Modu³ autoryzacji smartsession dla PAM
Group:		Libraries

%description pam
You need this in order to use cards insted of passwords.

%description -n smartsession-pam -l pl
Modu³ ten jest potrzebny, aby logowaæ siê wk³adaj±c kartê zamiast
wpisywania has³a.

%prep
%setup -qn smartsession
%patch0 -p0

%build
%{__make} -C src

%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{1,5,8},%{_sbindir},\
%{_bindir},%{_examplesdir}/%{name},%{_includedir},/lib/security}

install src/Cfs_SC/{cmkdir,cattach,cdetach,crescue}_SC $RPM_BUILD_ROOT%{_bindir}
install src/Graphic/xsst $RPM_BUILD_ROOT%{_sbindir}
install src/Locker/{autolock,smartlocker} $RPM_BUILD_ROOT%{_sbindir}
install src/Pam_Modules/pam_{smartcard,cfs_SC}.so $RPM_BUILD_ROOT/lib/security
install src/Tools/{sst,chpin,autolock_ctrl} $RPM_BUILD_ROOT%{_sbindir}
#smartsession/man/xsst.8
#smartsession/man/sst.8
#smartsession/man/autolock.8
#smartsession/man/crescue_SC.8
#smartsession/man/pam_cfs_SC.5
#smartsession/man/cfs_fstab.5
#smartsession/man/pam_smartcard.5
#smartsession/man/smartsession.5
#smartsession/man/autolock_ctrl.1
#smartsession/man/cfs_SC.1
#smartsession/man/chpin.1
#smartsession/man/smartlocker.1
install man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install Misc/{Makefile.patch,smartlocker_pam_config,README,erase_gpk8k,\
gdm.patch,get_name_in_card.sh,script_test} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}
#install src/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README copyright ChangeLog MANIFEST TODO
#%%{_libdir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_examplesdir}/%{name}

%files devel
%defattr(644,root,root,755)
#%%{_includedir}/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/cattach_SC
%attr(755,root,root) %{_bindir}/cdetach_SC
%attr(755,root,root) %{_bindir}/cmkdir_SC
%attr(755,root,root) %{_bindir}/crescue_SC
# huh, second copy???
%{_mandir}/man1/*

%files -n smartsession-pam
%defattr(644,root,root,755)
%attr(755,root,root) /lib/security/pam_cfs_SC.so
%attr(755,root,root) /lib/security/pam_smartcard.so
