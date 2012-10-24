Name:       deadbeef
Version:    0.5.6
Release:    1%{?dist}
Summary:    A music player with *.cue support
Summary(ru):Музыкальный проигрыватель с поддержкой *.cue

Group:      Applications/Multimedia
License:    GPLv2
URL:        http://deadbeef.sourceforge.net
Source0:    http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  flac-devel
BuildRequires:  faad2-devel
BuildRequires:  libmms-devel
BuildRequires:  intltool gettext-devel
BuildRequires:  libcddb-devel
BuildRequires:  libcdio-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmad-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  wavpack-devel
BuildRequires:  yasm-devel
BuildRequires:  bison
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  libstdc++-static
BuildRequires:  gtk3-devel
%else
BuildRequires:  libstdc++-devel
BuildRequires:  gtk2-devel
%endif

Requires:   %{name}-plugins = %{version}-%{release}


%description
DeaDBeeF (as in 0xDEADBEEF) is an audio player for GNU/Linux systems with X11 
(though now it also runs in plain console without X, in FreeBSD, and in
OpenSolaris).

It is mainly written by Alexey Yakovenko, with contributions from a lot of
different people (see about box in the player for more details).

It is distributed under the terms of General Public License version 2.

%description -l ru
DeaDBeeF (как в 0xDEADBEEF) это аудиопроигрыватель для систем GNU/Linux с X11
(теперь может работать и в чистой консоли).

В основном написан Алексеем Яковенко, с добавлениями от многих других людей
(подробнее смотри в разделе О программе).

Распространяется под условиями General Public License version 2.


%package devel
Summary:    Static library and header files for the %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains API documentation for
developing %{name}.

%package plugins
Summary:    Plugins for %{name}
Group:      Applications/Multimedia
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description plugins
This package contains plugins for %{name}


%prep
%setup -q

%build
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
    %configure --disable-gtk2 --enable-gtk3
%else
    %configure --enable-gtk2 --disable-gtk3
%endif
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

install -dD $RPM_BUILD_ROOT%{_datadir}/pixmaps

cp $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/%{name}.png \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{name}


%files -f %{name}.lang
%doc README ChangeLog COPYING AUTHORS
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/convpresets
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*


%files devel
%{_includedir}/%{name}/*

%files plugins
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.so.*


%changelog
* Tue Oct 23 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.6-1.R
- update to 0.5.6
- switch to GTK3

* Tue Sep 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.5-2.R
- add some BR

* Thu Jun 07 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.5-1.R
- update to 0.5.5

* Sat May 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.4-1.R
- update to 0.5.4
- enable SID plugin

* Wed Mar 28 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.2-2.R
- Added APE support

* Mon Mar 26 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.2-1.R
- update to 0.5.2

* Sun Feb  5 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.5.1-4.R
- added conditions to build for EL6

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.1-3.R
- Added description in russian language

* Mon Oct 31 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.1-2.R
- Added patch to compile in F16

* Mon Jun  6 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.5.1-1.R
- update to 0.5.1

* Mon May 16 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.5.0-1.R
- update to 0.5.0
- added BR: libstdc++-static for fedora >= 14

* Tue Nov 16 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.4-1
- update to 0.4.4

* Tue Nov  2 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.3-1
- update to 0.4.3

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.2-2
- install deadbeef.png to /usr/share/pixmaps

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4.2-1
- initial build for Fedora
