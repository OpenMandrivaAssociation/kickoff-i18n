Name: kickoff-i18n
Summary: Kickoff translations
Version: 1.0
Release: 8
Group: System/Internationalization
License: GPL
URL: https://www.mandriva.com
Source0: %name-%version.tar.bz2
Patch0:  kickoff-i18n-1.0-uz-po.patch
BuildRoot: %_tmppath/%name-%version-%release-buildroot
BuildArch: noarch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires: kdelibs-devel

%description
kickoff translations

%prep
%setup -q
%patch0 -p1

%build
./configure \
    --prefix=%_prefix \
    --datadir=%_datadir

make clean
%make

%install
rm -fr %buildroot
%makeinstall_std

%find_lang kickoff

%clean
rm -fr %buildroot

%files -f kickoff.lang
%defattr(-,root,root,-)
