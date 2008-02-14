%define snap	20071221

Summary:	H323 Auto Caller plugin for Nagios
Name:		h323ac
Version:	1.0.5
Release:	%mkrel 0.%{snap}.2
License:	MPL
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://sourceforge.net/projects/h323ac/
Source0:	%{name}-%{snap}.tar.lzma
# Add some includes to h323ac.h that used to be in upstream pwlib
# headers but aren't any more - AdamW 2007/12
Patch0:		h323ac-1.0.5-includes.patch
BuildRequires:	openh323-devel
BuildRequires:	pwlib-devel

%description
This application is a simple OpenH323-based WAV file player: you
use it to call a H.323 telephone and it will play a WAV file to
the remote telephone over the H.323 connection. It has many uses,
examples include using it as a Voice Pager in Nagios to notify
techs of system problems, using it as a wakeup service with cron,
or using it to Voice Spam audio advertisements to phones. If you
put it to other interesting uses, please email me to let me know
what you have thought up.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .includes

%build
%make \
    OPENH323DIR="%{_datadir}/openh323" \
    PWLIBDIR="%{_datadir}/pwlib" \
    OH323_INCDIR="%{_includedir}/openh323" \
    OH323_LIBDIR="%{_libdir}" \
    CFLAGS="%{optflags} -DLDAP_DEPRECATED" \
    CXXFLAGS="%{optflags} -DLDAP_DEPRECATED" \
    opt

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d -m0755 %{buildroot}%{_libdir}/nagios/plugins
install -m0755 obj_linux_*/h323ac %{buildroot}%{_libdir}/nagios/plugins/


%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_libdir}/nagios/plugins/h323ac

