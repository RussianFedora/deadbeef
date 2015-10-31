%define rev 20151030git91154c

Name:       deadbeef
Version:    0.6.2
Release:    4.%{rev}%{?dist}
Summary:    A music player with *.cue support
Summary(ru):Музыкальный проигрыватель с поддержкой *.cue

Group:      Applications/Multimedia
License:    GPLv2
URL:        http://deadbeef.sourceforge.net
Source0:    %{name}-%{version}-%{rev}.tar.xz
Patch1:     deadbeef-0.6.2-valid-desktop-file.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  automake, autoconf, libtool
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
BuildRequires:  imlib2-devel
BuildRequires:  libzip-devel
BuildRequires:  jansson-devel
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  gtk3-devel
%else
BuildRequires:  libstdc++-devel
BuildRequires:  gtk2-devel
%endif
BuildRequires:  desktop-file-utils

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
%setup -q -n deadbeef-0.6.2
%patch1 -p1 -b .valid

# https://code.google.com/p/ddb/issues/detail?id=999
find plugins -name "[^.]*" -type f \
    | while read f ;
    do
        sed -i -e "s!Foundation, Inc., 59.*!Foundation,\ Inc.,\ 51\ Franklin Street,\ Fifth\ Floor,\ Boston,\ MA!" "$f" ;
    done
sed -i -e "s!Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.!Foundation,\ Inc.,\ 51\ Franklin Street,\ Fifth\ Floor,\ Boston,\ MA!" "plugins/sid/sidplay-libs/libsidplay/src/reloc65.c" ;
sed -i -e "s!Boston, MA!Boston, MA\\\n\"!" "plugins/adplug/plugin.c" ;
sed -i -e "s!Boston, MA!Boston, MA\\\n\"!" "plugins/mms/mmsplug.c" ;

%build
if ! test -x configure; then ./autogen.sh; fi;
  %configure --enable-ffmpeg --docdir=%{_defaultdocdir}/%{name}-%{version} \
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
    --disable-gtk2 --enable-gtk3 --disable-static --disable-gme
%else
    --enable-gtk2 --disable-gtk3 --disable-lfm --disable-static
%endif
make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -name "*.la" -exec rm {} \;
find %{buildroot} -name "*.a" -exec rm {} \;

install -dD %{buildroot}%{_datadir}/pixmaps

cp %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png \
    %{buildroot}%{_datadir}/pixmaps

#https://code.google.com/p/ddb/issues/detail?id=1001
sed -i -e 's!Play Shortcut Group!X-Play Shortcut Group!' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i -e 's!Pause Shortcut Group!X-Pause Shortcut Group!' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i -e 's!Stop Shortcut Group!X-Stop Shortcut Group!' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i -e 's!Next Shortcut Group!X-Next Shortcut Group!' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i -e 's!Prev Shortcut Group!X-Prev Shortcut Group!' %{buildroot}%{_datadir}/applications/%{name}.desktop
head -n 43 %{buildroot}%{_datadir}/applications/%{name}.desktop > %{buildroot}%{_datadir}/applications/%{name}.desktop2
mv %{buildroot}%{_datadir}/applications/%{name}.desktop2 %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc README ChangeLog COPYING AUTHORS
%{_defaultdocdir}/%{name}-%{version}
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*
%{_libdir}/%{name}/data68/*


%files devel
%{_includedir}/%{name}/*

%files plugins
%{_libdir}/%{name}/convpresets
%{_libdir}/%{name}/*.so


%changelog
* Fri Oct 30 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.6.2-4.20151030git91154c.R
- update to last snapshot

* Tue Nov 18 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.6.2-3.R
- Bump rebuild for new ffmpeg

* Fri Oct 03 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.6.2-2.R
- Bump rebuild for new cdio

* Thu Aug 07 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.6.2-1.R
- update to 0.6.2

* Mon Feb 03 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.6.1-1.R
- update to 0.6.1

* Tue Nov 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.6.0-2.R
- correct FSF address and other errors and warnings

* Tue Nov 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.6.0-1.R
- update to 0.6.0

* Wed Apr 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.6-5.R
- bump release for update dependencies

* Tue Nov 06 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.6-4.R
- added documentation to help menu

* Fri Oct 26 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.6-3.R
- correct compile for >= F18

* Thu Oct 25 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.6-2.R
- added plugins artwork, ffmpeg, vfs_zip

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
