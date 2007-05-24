Name: kickoff-i18n
Summary: kickoff translations
Version: 1.0
Release: %mkrel 1
Group: System/Internationalization
License: GPL
URL: http://www.mandriva.com
Source0: %name-%version.tar.bz2
BuildRoot: %_tmppath/%name-%version-%release-buildroot
BuildArch: noarch
BuildRequires: kdelibs-devel

%description
kickoff translations

%prep
%setup -q

%build
./configure \
    --prefix=%_prefix \
    --datadir=%_datadir

make clean
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,-)
%_datadir/locale/*/*/*


