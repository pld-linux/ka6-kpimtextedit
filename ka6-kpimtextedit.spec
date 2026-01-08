#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	25.12.1
%define		kf_ver		6.3.0
%define		qt_ver		6.6.0
%define		kaname		kpimtextedit
Summary:	KPIMTextedit - a textedit with PIM-specific features
Summary(pl.UTF-8):	KPIMTextedit - pole edycji tekstu z funkcjami specyficznymi dla PIM
Name:		ka6-%{kaname}
Version:	25.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5d4d769525f3a864a645f8741e88a384
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
%if %{with tests}
BuildRequires:	Qt6Test-devel >= %{qt_ver}
%endif
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-kcodecs-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-ktextaddons-devel >= 1.8.0
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf6-sonnet-devel >= %{kf_ver}
BuildRequires:	kf6-syntax-highlighting-devel >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	kf6-kcodecs >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kiconthemes >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-ktextaddons >= 1.8.0
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-kxmlgui >= %{kf_ver}
Requires:	kf6-sonnet >= %{kf_ver}
Requires:	kf6-syntax-highlighting >= %{kf_ver}
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-kpimtextedit < 24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPIMTextedit provides a textedit with PIM-specific features.

%description -l pl.UTF-8
KPIMTextedit dostarcza pole edycji tekstu z funkcjami specyficznymi
dla PIM.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf6-ktextaddons-devel >= 1.5.4
Obsoletes:	ka5-kpimtextedit-devel < 24

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang libkpimtextedit6

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libkpimtextedit6.lang
%defattr(644,root,root,755)
%{_libdir}/libKPim6TextEdit.so.*.*
%ghost %{_libdir}/libKPim6TextEdit.so.6
%{_datadir}/qlogging-categories6/kpimtextedit.categories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKPim6TextEdit.so
%{_includedir}/KPim6/KPIMTextEdit
%{_libdir}/cmake/KPim6TextEdit
