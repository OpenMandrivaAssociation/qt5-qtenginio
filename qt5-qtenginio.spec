%define api 5
%define major 1
%define beta %nil

%define enginio %mklibname enginio 1
%define enginiod %mklibname enginio -d

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtenginio
Version:	1.6.3
Epoch:		1
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtenginio-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/5.8/5.8.0-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	2
%define qttarballdir qtenginio-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/5.6/5.6.3/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Widgets) >= %{version}

%description
Client library for accessing Enginio service from Qt and QML code.

%files
%{_qt5_prefix}/qml/Enginio
#------------------------------------------------------------------------------

%package -n	%{enginio}
Summary:	Qt%{api} Component Library
Group:		System/Libraries

%description -n %{enginio}
Qt%{api} Component Library.

%files -n %{enginio}
%{_qt5_libdir}/libEnginio.so.%{major}*

#------------------------------------------------------------------------------

%package -n	%{enginiod}
Summary:	Devel files needed to build apps based on QtEnginio
Group:		Development/KDE and Qt
Requires:	%{enginio} = %{EVRD}

%description -n %{enginiod}
Devel files needed to build apps based on QtEnginio.

%files -n %{enginiod}
%{_qt5_libdir}/libEnginio.so
%{_qt5_libdir}/libEnginio.prl
%{_qt5_libdir}/pkgconfig/Enginio.pc
%{_qt5_includedir}/Enginio
%{_qt5_prefix}/mkspecs/modules/qt_lib_enginio.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_enginio_private.pri
%{_qt5_libdir}/cmake/Qt5Enginio
%{_qt5_exampledir}/enginio

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir
%autopatch -p1

%build
%qmake_qt5
%make
#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

rm -f %{buildroot}%{_qt5_libdir}/libEnginio.la
