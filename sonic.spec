%define git 20250418
%define libname %mklibname sonic
%define devname %mklibname -d sonic

Summary:	Sonic Library for speeding up and slowing speach
Summary(pl.UTF-8):	Biblioteka Sonic do przyspieszania i spowalniania mowy
Name:		sonic
Version:	0.2.0.%{git}
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0:	https://github.com/waywardgeek/sonic/archive/release-%{version}/%{name}-%{version}.tar.gz
# Dont use source archive, bc is old and lack some core parts, needed to build. Packaging them separately is a waste of time.
# Use git clone --recursive https://github.com/waywardgeek/sonic
Source0:	sonic-0.2.0-%{git}.tar.xz
URL:		https://github.com/waywardgeek/sonic

%description
Sonic is a simple algorithm for speeding up or slowing down speech.
However, it's optimized for speed ups of over 2X, unlike previous
algorithms for changing speech rate. The Sonic library is a very
simple ANSI C library that is designed to easily be integrated into
streaming voice applications, like TTS back ends.

%description -l pl.UTF-8
Sonic to prosty algorytm do przyspieszania i spowalniania mowy. W
porównaniu do wcześniejszych algorytmów tego typu, jest
zoptymalizowany pod kątem przyspieszania ponad dwukrotnego. Biblioteka
Sonic to bardzo prosta biblioteka ANSI C, zaprojektowana do łatwej
integracji w aplikacjach przetwarzających strumienie głosu, takich jak
backendy syntezatorów mowy.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.


%package static
Summary:	Static Sonic library
Summary(pl.UTF-8):	Statyczna biblioteka Sonic
Group:		Development/Libraries
Requires:	%{libname} = %{EVRD}

%description static
Static Sonic library.

%description static -l pl.UTF-8
Statyczna biblioteka Sonic.

%prep
%autosetup -n %{name}-0.2.0-%{git} -p1

%build
%make_build

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}"

install -Dp sonic.1 $RPM_BUILD_ROOT%{_mandir}/man1/sonic.1


%files -n %{libname}
%defattr(644,root,root,755)
%doc README doc/index.md
%attr(755,root,root) %{_bindir}/sonic
%attr(755,root,root) %{_libdir}/libsonic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsonic.so.0
%{_mandir}/man1/sonic.1*

%files -n %{devname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsonic.so
%{_includedir}/sonic.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsonic.a
