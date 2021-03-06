Name:           deadbeef
Version:        0.7.2
Release:        5%{?dist}
Summary:        An audio player for GNU/Linux
Summary(ru):    Музыкальный проигрыватель для GNU/Linux

Group:          Applications/Multimedia
License:        GPLv3+ and LGPLv2+ and BSD and MIT and zlib
URL:            http://deadbeef.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.bz2
Patch:          desktop.patch

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(flac)
BuildRequires:  faad2-devel
BuildRequires:  pkgconfig(libmms)
BuildRequires:  intltool
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  libtool
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  yasm-devel
BuildRequires:  bison
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libzip)
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  pkgconfig(gtk+-3.0)
%else
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(jansson)

Requires:       hicolor-icon-theme
Requires:       %{name}-plugins%{?_isa} = %{version}-%{release}


%description
DeaDBeeF (as in 0xDEADBEEF) is an audio player for GNU/Linux systems with X11 
(though now it also runs in plain console without X, in FreeBSD, and in
OpenSolaris).

%description -l ru
DeaDBeeF (как в 0xDEADBEEF) это аудиопроигрыватель для систем GNU/Linux с X11
(теперь может работать и в чистой консоли).


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
%autosetup -p0

# Remove exec permission from source files
find . \( -name '*.cpp' -or -name '*.hpp' -or -name '*.h' \) -and -executable -exec chmod -x {} \;


%build
%configure --enable-ffmpeg --docdir=%{_defaultdocdir}/%{name}-%{version} \
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
    --disable-gtk2 --enable-gtk3 --disable-static
%else
    --enable-gtk2 --disable-gtk3 --disable-lfm --disable-static
%endif
%make_build


%install
%make_install
find %{buildroot} -name "*.la" -exec rm {} \;

install -Dpm0644 %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

sed -i -e "s!MP3!MP3;!" %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%license COPYING
%{_defaultdocdir}/%{name}-%{version}
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*


%files devel
%{_includedir}/%{name}

%files plugins
%{_libdir}/%{name}/convpresets
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/data68


%changelog
* Fri May 04 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.2-5
- Rebuild with new ffmpeg

* Tue Feb 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.2-4
- Remove unneeded scriptlet

* Tue Aug 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.2-3
- Clean spec

* Tue Jun 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.7.2-2.R
- rebuilt against new ffmpeg

* Thu Apr 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.2-1.R
- Update to 0.7.2
- Add patch for desktop-file

* Wed Mar 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.1-1.R
- Update to 0.7.1

* Tue Feb 02 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.0-2.R
- Add Icon Cache scriptlets
- Add desktop-database scriptlets
- Add libmpg123 support

* Mon Feb 01 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.0-1.R
- Update to 0.7.0

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
