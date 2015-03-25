Summary:	A network traffic monitoring tool
Name:		tcpdump
Version:	4.6.2
Release:	1
Epoch:		2
Group:	 	Monitoring
License:	BSD
URL:		http://www.tcpdump.org/
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source1:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz.sig
Patch9:		0009-Do-more-bounds-checking-and-length-checking.patch
Patch10:	0010-Do-bounds-checking-and-length-checking.patch
Patch11:	0011-Add-initial-bounds-check-get-rid-of-union-aodv.patch
Patch12:	0012-Clean-up-error-message-printing.patch
Patch13:	0013-Further-cleanups.patch
Patch14:	0014-Not-using-offsetof-any-more-so-no-need-for-stddef.h.patch
Patch15:	0015-Report-a-too-long-unreachable-destination-list.patch
Patch16:	tcpdump-4.6.2-CVE-2014-9140.patch
Patch17:	tcpdump-4.6.2-CVE-2015-0261.patch
Patch18:	tcpdump-4.6.2-CVE-2015-2153.patch
Patch19:	tcpdump-4.6.2-CVE-2015-2154.patch
Patch20:	tcpdump-4.6.2-CVE-2015-2155.patch
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
%configure2_5x \
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


