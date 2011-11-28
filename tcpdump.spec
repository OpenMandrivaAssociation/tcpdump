Summary:	A network traffic monitoring tool
Name:		tcpdump
Version:	4.2.0
Release:	%mkrel 1
Epoch:		2
Group:	 	Monitoring
License:	BSD
URL:		http://www.tcpdump.org/
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source1:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz.sig
Patch0:		tcpdump-4.2.0-missing_ppi_header.diff
BuildRequires:	pcap-devel >= 1.2.0
BuildRequires:	openssl-devel
BuildRequires:	libsmi-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tcpdump is a command-line tool for monitoring network traffic.  Tcpdump can
capture and display the packet headers on a particular network interface or on
all interfaces.  Tcpdump can display all of the packet headers, or just the
ones that match particular criteria.

Install tcpdump if you need a program to monitor network traffic.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
export CFLAGS="%{optflags} -I. -DIP_MAX_MEMBERSHIPS=20"
%configure2_5x \
    --enable-ipv6

%make

# (oe) TODO: investigate the following:
#--with-user=USERNAME    drop privileges by default to USERNAME
#--with-chroot=DIRECTORY when dropping privileges, chroot to DIRECTORY

%install
rm -rf %{buildroot}

%makeinstall_std
# (misc) remove the binary, has this only pollutes completion
# and take useless space in the rpm
rm -f %{buildroot}/%_sbindir/%name.%version

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES CREDITS LICENSE
%{_sbindir}/%{name}
%{_mandir}/man1/tcpdump.1*
