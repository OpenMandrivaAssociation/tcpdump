Summary:	A network traffic monitoring tool
Name:		tcpdump
Version:	3.9.8
Release:	%mkrel 1
Epoch:		2
Group:	 	Monitoring
License:	BSD
URL:		http://www.tcpdump.org/
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source1:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz.sig
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel
BuildRequires:	libtool
BuildRequires:	autoconf2.5

%description
Tcpdump is a command-line tool for monitoring network traffic.  Tcpdump can
capture and display the packet headers on a particular network interface or on
all interfaces.  Tcpdump can display all of the packet headers, or just the
ones that match particular criteria.

Install tcpdump if you need a program to monitor network traffic.

%prep

%setup -q

%build
%serverbuild
libtoolize --copy --force
%define	optflags $RPM_OPT_FLAGS -DIP_MAX_MEMBERSHIPS=20

%configure2_5x \
    --enable-ipv6

%undefine optflags

%make

# (oe) TODO: investigate the following:
#--with-user=USERNAME    drop privileges by default to USERNAME
#--with-chroot=DIRECTORY when dropping privileges, chroot to DIRECTORY

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

#install -m755 -s tcpdump ${RPM_BUILD_ROOT}%{_sbindir}
#install -m644 tcpdump.1 ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpdump.8
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES CREDITS FILES LICENSE TODO VERSION PLATFORMS
%{_sbindir}/tcpdump
%{_mandir}/man1/tcpdump.1*
