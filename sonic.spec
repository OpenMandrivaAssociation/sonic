%define		gitdate 20260314
%define		libname %mklibname sonic
%define		devname %mklibname -d sonic

Summary:		Sonic Library for speeding up and slowing down speech
Name:	sonic
Version:	0.2.0-%{gitdate}
Release:	1
License:	Apache-2.0
Group:	Sound
Url:		https://github.com/waywardgeek/sonic
#Source0:	https://github.com/waywardgeek/sonic/archive/release-%%{version}/%%{name}-%%{version}.tar.gz
# Don't use the source archive, bc is old and lack some core parts, needed to build. Packaging them separately is a waste of time.
# Use git clone --recursive https://github.com/waywardgeek/sonic
Source0:	%{name}-0.2.0-%{gitdate}.tar.xz
Patch0:	sonic-0.2.0-fix-library-soname.patch
BuildRequires:		make

%description
A simple algorithm for speeding up or slowing down speech. However, it's
optimized for speed ups of over 2X, unlike previous algorithms for changing
speech rate. The library is a very simple ANSI C library that is designed to
easily be integrated into streaming voice applications, like TTS back ends.

%files
%doc README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:		Shared library for %{name}
Group:	System/Libraries

%description -n %{libname}
A simple algorithm for speeding up or slowing down speech.
This package contains the library files for %{name}.

%files -n %{libname}
%license LICENSE
%doc doc/index.md
%{_libdir}/lib%{name}.so.0*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:		Development files for %{name}
Group:	Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
A simple algorithm for speeding up or slowing down speech.
This package contains development files for %{name}.

%files -n %{devname}
%license LICENSE
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

#-----------------------------------------------------------------------------

%package static
Summary:	Static Sonic library
Group:		Development/Libraries
Requires:	%{libname} = %{EVRD}

%description static
A simple algorithm for speeding up or slowing down speech.
Static Sonic library.

%files static
%{_libdir}/lib%{name}.a

#-----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-0.2.0-%{gitdate} -p1


%build
%make_build


%install
%{__make} install \
	DESTDIR="%{buildroot}" \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}"

# Man page does not get installed by default
install -Dp sonic.1 %{buildroot}%{_mandir}/man1/sonic.1

# Fix perms
chmod -x %{buildroot}%{_libdir}/libsonic.a
chmod -x %{buildroot}%{_includedir}/%{name}.h
