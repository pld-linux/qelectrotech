Summary:	QElectroTech helps you to design electric schematics
Summary(hu.UTF-8):	QElectroTech-hel elektromos áramköröket tervezhetsz
Name:		qelectrotech
Version:	0.2
Release:	0.3
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://download.tuxfamily.org/qet/tags/20090627/%{name}-%{version}-src.tar.gz
# Source0-md5:	615d2463178689741cd2791c6e3deacd
Patch0:		%{name}-prefix.patch
URL:		http://qelectrotech.org/
BuildRequires:	QtCore-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QElectroTech helps you to design electric schematics.

%description -l hu.UTF-8
QElectroTech-hel elektromos áramköröket tervezhetsz.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%{__sed} -i -e "/QET_MAN_PATH/ s,man/,share/man, ;\
	/QET_MIME/ s,../,," %{name}.pro

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/qelectrotech \
       $RPM_BUILD_ROOT%{_mandir}/fr.ISO8859-1 \
       $RPM_BUILD_ROOT%{_mandir}/fr
mv $RPM_BUILD_ROOT%{_mandir}/fr.UTF-8 $RPM_BUILD_ROOT%{_mandir}/fr

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/lang/qt_*.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDIT README examples
%attr(755,root,root) %{_bindir}/*
%lang(fr) %{_mandir}/fr/man1/%{name}.*
%{_mandir}/man1/%{name}.*
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/mime
%dir %{_datadir}/mime/application
%{_datadir}/mime/application/x-qet-*.xml
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/x-qet-*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/elements
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/lang
