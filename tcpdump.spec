Summary:	A network traffic monitoring tool
Name:		tcpdump
Version:	4.1.0
Release:	%mkrel 1
Epoch:		2
Group:	 	Monitoring
License:	BSD
URL:		http://www.tcpdump.org/
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source1:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz.sig
BuildRequires:	pcap-devel >= 1.0.0-3
BuildRequires:	openssl-devel
BuildRequires:	libsmi-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tcpdump is a command-line tool for monitoring network traffic.  Tcpdump can
capture and display the packet headers on a particular network interface or on
all interfaces.  Tcpdump can display all of the packet headers, or just the
ones that match particular criteria.

Install tcpdump if you need a program to monitor network traffic.

%prep

%setup -q -n %{name}-4.1

%build
%serverbuild
libtoolize --copy --force
%define	optflags $RPM_OPT_FLAGS -DIP_MAX_MEMBERSHIPS=20

export LIBS="-lcrypto"

%configure2_5x \
    --enable-ipv6

cat >> config.h << EOF
#define HAVE_LIBCRYPTO 1
#define HAVE_OPENSSL_EVP_H 1
EOF

%undefine optflags

%make

# (oe) TODO: investigate the following:
#--with-user=USERNAME    drop privileges by default to USERNAME
#--with-chroot=DIRECTORY when dropping privileges, chroot to DIRECTORY

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

%makeinstall_std

# cleanup (wtf?)
rm -f %{buildroot}%{_sbindir}/tcpdump.%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES CREDITS LICENSE
%{_sbindir}/tcpdump
%{_sbindir}/tcpdump.4.1
%{_mandir}/man1/tcpdump.1*
