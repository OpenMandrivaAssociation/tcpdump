Summary:	A network traffic monitoring tool
Name:		tcpdump
Version:	4.9.3
Release:	1
Epoch:		2
Group:	 	Monitoring
License:	BSD
URL:		http://www.tcpdump.org/
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
BuildRequires:	pcap-devel >= 1.2.0
BuildRequires:	openssl-devel
BuildRequires:	libsmi-devel

%description
Tcpdump is a command-line tool for monitoring network traffic.  Tcpdump can
capture and display the packet headers on a particular network interface or on
all interfaces.  Tcpdump can display all of the packet headers, or just the
ones that match particular criteria.

Install tcpdump if you need a program to monitor network traffic.

%prep
%setup -q
%apply_patches

%build
%serverbuild
export CFLAGS="%{optflags} -I. -DIP_MAX_MEMBERSHIPS=20"
%configure \
    --enable-ipv6

%make

%install
%makeinstall_std
# (misc) remove the binary, has this only pollutes completion
# and take useless space in the rpm
rm -f %{buildroot}/%{_sbindir}/%{name}.%{version}

%files
%doc README.md CHANGES CREDITS LICENSE
%{_sbindir}/%{name}
%{_mandir}/man1/tcpdump.1*
