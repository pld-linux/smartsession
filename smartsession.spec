# $Revision: 1.1 $
Summary:	Utilities for GemPlus(R) smartcard readers
Summary(pl):	Narzêdzia do czytników kart GemPlus(R)
Name:		smartsession
Version:	1.9.11
Release:	1
License:	Consult w/ www.gemplus.com and file 'copyright'
Group:		Utilities 
Source0:	%{name}_%{version}.tar.gz
Patch0:		%{name}-use_gdbm.patch
URL:		http://www.gemplus.com/techno/smartsession
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#BuildRequires:	pcsc-lite-devel
Requires:	pcsc-lite

%description

See attached copyright file !

%description -l pl

Zapoznaj siê z do³±czonym plikiem copyright.

%package -n smartsession-devel
Summary:    smartsession header files
Summary(pl):    nag³ówki smartsession
Group:      Libraries

%description -n smartsession-devel
smartsession header files

%description -n smartsession-devel -l pl
nag³ówki smartsession 

%package -n smartsession-tools
Summary:	Tools
Summary(pl):	fajowe zabawki
Group:		Applications/Utilities
Requires: smartsession

%description -n smartsession-tools
Simple tools for comunicating w/ smartcard reader.

%description -n smartsession-tools -l pl
Proste narzêdzia do komunikacji z czytnikiem kart chip.

%prep
%setup -qn smartsession
%patch0 -p0

%build

cd src
%{__make}
cd ../man
gzip -9nf *.[0-9]

%install
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{1,5,8},%{_sbindir},\
%{_bindir},%{_examplesdir}/%{name},/usr/include,\
%{_sysconfdir}/pam.d}

install src/Cfs_SC/{cmkdir,cattach,cdetach,crescue}_SC $RPM_BUILD_ROOT%{_bindir}
install src/Graphic/xsst  $RPM_BUILD_ROOT%{_sbindir}
install src/Locker/{autolock,smartlocker}  $RPM_BUILD_ROOT%{_sbindir}
install src/Pam_Modules/pam_{smartcard,cfs_SC}.so $RPM_BUILD_ROOT/etc/pam.d
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
install man/*.8.gz $RPM_BUILD_ROOT%{_mandir}/man8
install man/*.5.gz $RPM_BUILD_ROOT%{_mandir}/man5
install man/*.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
install Misc/{Makefile.patch,smartlocker_pam_config,README,erase_gpk8k,\
gdm.patch,get_name_in_card.sh,script_test} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}
#install src/*.h $RPM_BUILD_ROOT/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%post -n smartsession-devel
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc INSTALL README copyright ChangeLog MANIFEST TODO 
#%{_libdir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_examplesdir}/%{name}

%files -n smartsession-devel
%defattr(644,root,root,755)
#/usr/include/*

%files -n smartsession-tools
%defattr(644,root,root,755)
%{_sbindir}/*
%{_mandir}/man1/*
