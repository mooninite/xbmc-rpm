%global PRERELEASE Gotham_beta3
#%%global DIRVERSION %{version}
# use the line below for pre-releases
%global DIRVERSION %{version}-%{PRERELEASE}
%global _hardened_build 1

Name: xbmc
Version: 13.0
Release: 0.9.Gotham_beta3%{?dist}
URL: http://www.xbmc.org/

Source0: %{name}-%{DIRVERSION}-patched.tar.xz
# xbmc contains code that we cannot ship, as well as redundant private
# copies of upstream libraries that we already distribute.  Therefore
# we use this script to remove the code before shipping it.
# Invoke this script while in the directory where the tarball is located:
# ./xbmc-generate-tarball-xz.sh
Source1: xbmc-generate-tarball-xz.sh

# filed ticket, but patch still needs work
# http://trac.xbmc.org/ticket/9658
Patch1: xbmc-13.0-dvdread.patch

# need to file trac ticket, this patch just forces external hdhomerun
# functionality, needs to be able fallback internal version
Patch2: xbmc-13.0-hdhomerun.patch

# Avoid segfault during goom's configure
# https://bugzilla.redhat.com/1069079
Patch3: xbmc-13.0-libmysqlclient.patch

# External ffmpeg patches
Patch100: 0001-Revert-drop-support-for-external-ffmpeg.patch
Patch101: 0002-Revert-linux-link-ffmpeg-statically.patch
Patch102: 0003-makefile-include.patch

# Optional deps (not in EPEL)
%if 0%{?fedora}
# (libbluray in EPEL 6 is too old.)
%global with_libbluray 1
%global with_cwiid 1
%global with_libssh 1
%global with_libcec 1
%global with_external_ffmpeg 1
%endif

%ifarch x86_64 i686
%global with_crystalhd 1
%global with_hdhomerun 1
%endif

ExcludeArch: ppc64
Summary: Media center
License: GPLv2+ and GPLv3+
Group: Applications/Multimedia
BuildRequires: desktop-file-utils
BuildRequires: dbus-devel
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: fontconfig-devel
BuildRequires: fribidi-devel
BuildRequires: glibc-devel
BuildRequires: glew-devel
BuildRequires: libstdc++-devel
BuildRequires: glib2-devel
BuildRequires: libjasper-devel
%if 0%{?el6}
BuildRequires: libjpeg-devel
%else
BuildRequires: libjpeg-turbo-devel
%endif
BuildRequires: libogg-devel
BuildRequires: libpng-devel
BuildRequires: libstdc++-devel
BuildRequires: e2fsprogs-devel
BuildRequires: libvorbis-devel
BuildRequires: lzo-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: tre-devel
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: freetype-devel
BuildRequires: libXinerama-devel
BuildRequires: fontconfig-devel
BuildRequires: mysql-devel
BuildRequires: jasper-devel
BuildRequires: enca-devel
BuildRequires: cmake
BuildRequires: gperf
BuildRequires: nasm
BuildRequires: libXmu-devel
BuildRequires: pcre-devel
BuildRequires: gcc-c++
BuildRequires: sqlite-devel
BuildRequires: curl-devel
BuildRequires: libcdio-devel
BuildRequires: flex
BuildRequires: libmad-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsmbclient-devel
BuildRequires: libmms-devel
BuildRequires: libXtst-devel
BuildRequires: libvdpau-devel
BuildRequires: desktop-file-utils
BuildRequires: python-devel
BuildRequires: wavpack-devel
BuildRequires: a52dec-devel
BuildRequires: libmpeg2-devel
BuildRequires: libmpcdec-devel
BuildRequires: flac-devel
BuildRequires: avahi-devel
BuildRequires: libtool
BuildRequires: libtiff-devel
BuildRequires: libvdpau-devel
BuildRequires: libdvdread-devel
%if 0%{with_external_ffmpeg}
BuildRequires: ffmpeg-devel
%endif
BuildRequires: faad2-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libdca-devel
BuildRequires: libass-devel >= 0.9.7
%if 0%{with_hdhomerun}
BuildRequires: hdhomerun-devel
%endif
%if 0%{with_crystalhd}
BuildRequires: libcrystalhd-devel
%endif
BuildRequires: libmodplug-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: expat-devel
BuildRequires: zip
BuildRequires: pkgconfig(libudev)
# for AirPlay support
BuildRequires: libplist-devel
%if 0%{?el6}
BuildRequires: gettext-devel
%else
BuildRequires: gettext-autopoint
%endif
BuildRequires: librtmp-devel
%if 0%{with_libbluray}
BuildRequires: libbluray-devel
#BuildRequires: libbluray-devel >= 0.2.1
%endif
BuildRequires: yajl-devel
BuildRequires: bluez-libs-devel
BuildRequires: tinyxml-devel
%if 0%{with_cwiid}
BuildRequires: cwiid-devel
%endif
BuildRequires: taglib-devel >= 1.8
BuildRequires: swig
BuildRequires: java-devel
BuildRequires: lame-devel
%if 0%{with_libssh}
BuildRequires: libssh-devel
%endif
BuildRequires: libcap-devel
%if 0%{with_libcec}
BuildRequires: libcec-devel
%endif
BuildRequires: libxml-devel
BuildRequires: libxslt-devel
BuildRequires: trousers-devel

# nfs-utils-lib-devel package currently broken
#BuildRequires: nfs-utils-lib-devel
BuildRequires: afpfs-ng-devel
BuildRequires: libva-devel

# need explicit requires for these packages
# as they are dynamically loaded via XBMC's arcane 
# pseudo-DLL loading scheme (sigh)
Requires: librtmp
Requires: libmad
%if 0%{with_hdhomerun}
BuildRequires: hdhomerun
%endif
%if 0%{with_crystalhd}
Requires: libcrystalhd
%endif
%if 0%{with_libbluray}
Requires: libbluray
%endif
%if 0%{with_libcec}
Requires: libcec
%endif

# needed when doing a minimal install, see
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=1844
Requires: glx-utils
Requires: xorg-x11-utils

# These are just symlinked to, but needed both at build-time
# and for installation
BuildRequires: python-imaging
Requires: python-imaging

%description
XBMC media center is a free cross-platform media-player jukebox and
entertainment hub.  XBMC can play a spectrum of of multimedia formats,
and featuring playlist, audio visualizations, slideshow, and weather
forecast functions, together third-party plugins.

%package devel
Summary: Development files needed to compile C programs against xbmc
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel

XBMC media center is a free cross-platform media-player jukebox and
entertainment hub. If you want to develop programs which use xbmc's
libraries, you need to install this package.

#%%package eventclients
#%Summary: Media center event client remotes

#%%description eventclients
#%This package contains support for using XBMC with the PS3 Remote, the Wii
#%Remote, a J2ME based remote and the command line xbmc-send utility.

#%%package eventclients-devel
#%Summary: Media center event client remotes development files
#%Requires:	%{name}-eventclients = %{version}-%{release}

#%%description eventclients-devel
#%This package contains the development header files for the eventclients
#%library.

%prep

%setup -q -n %{name}-%{DIRVERSION}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1

%if 0%{with_hdhomerun}
%else
  # Remove hdhomerun from the build.
  pushd xbmc/filesystem/
    rm HDHomeRunFile.cpp HDHomeRunFile.h
    rm HDHomeRunDirectory.cpp HDHomeRunDirectory.h
    sed -i Makefile.in -e '/HDHomeRunFile\.cpp/d'
    sed -i Makefile.in -e '/HDHomeRunDirectory\.cpp/d'
    sed -i DirectoryFactory.cpp -e '/HomeRun/d'
    sed -i FileFactory.cpp -e '/HomeRun/d'
  popd
%endif

%build

chmod +x bootstrap
./bootstrap
# Can't use export nor %%configure (implies using export), because
# the Makefile pile up *FLAGS in this case.

./configure \
--prefix=%{_prefix} --bindir=%{_bindir} --includedir=%{_includedir} \
--libdir=%{_libdir} --datadir=%{_datadir} \
--with-lirc-device=/var/run/lirc/lircd \
--enable-external-libraries \
--enable-goom \
--enable-pulse \
%if 0%{with_libcec}
--enable-libcec \
%else
--disable-libcec \
%endif
%if 0%{with_libssh}
--enable-ssh \
%else
--disable-ssh \
%endif
--disable-dvdcss \
--disable-optimizations --disable-debug \
%if 0%{with_external_ffmpeg}
CPPFLAGS="-I/usr/include/ffmpeg" \
CFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/afpfs-ng/ -I/usr/include/ffmpeg -I/usr/include/samba-4.0/ -D__STDC_CONSTANT_MACROS" \
CXXFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/afpfs-ng/ -I/usr/include/ffmpeg -I/usr/include/samba-4.0/ -D__STDC_CONSTANT_MACROS" \
%else
CFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/afpfs-ng/ -I/usr/include/samba-4.0/ -D__STDC_CONSTANT_MACROS" \
CXXFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/afpfs-ng/ -I/usr/include/samba-4.0/ -D__STDC_CONSTANT_MACROS" \
%endif
LDFLAGS="-fPIC" \
%if 0%{?with_hdhomerun}
LIBS=" -lhdhomerun $LIBS" \
%endif
ASFLAGS=-fPIC

make %{?_smp_mflags} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
#make -C tools/EventClients DESTDIR=$RPM_BUILD_ROOT install 
# remove the doc files from unversioned /usr/share/doc/xbmc, they should be in versioned docdir
rm -r $RPM_BUILD_ROOT/%{_datadir}/doc/

desktop-file-install \
 --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
 $RPM_BUILD_ROOT%{_datadir}/applications/xbmc.desktop

# Normally we are expected to build these manually. But since we are using
# the system Python interpreter, we also want to use the system libraries
install -d $RPM_BUILD_ROOT%{_libdir}/xbmc/addons/script.module.pil/lib
ln -s %{python_sitearch}/PIL $RPM_BUILD_ROOT%{_libdir}/xbmc/addons/script.module.pil/lib/PIL
#install -d $RPM_BUILD_ROOT%{_libdir}/xbmc/addons/script.module.pysqlite/lib
#ln -s %{python_sitearch}/pysqlite2 $RPM_BUILD_ROOT%{_libdir}/xbmc/addons/script.module.pysqlite/lib/pysqlite2

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root)
%doc copying.txt CONTRIBUTORS LICENSE.GPL README
%doc docs
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%{_libdir}/xbmc
%{_datadir}/xbmc
%{_datadir}/xsessions/XBMC.desktop
%{_datadir}/applications/xbmc.desktop
%{_datadir}/icons/hicolor/*/*/*.png

%files devel
%{_includedir}/xbmc

#%%files eventclients
#%%defattr(-,root,root)
#%%python_sitelib/xbmc
#%%dir %{_datadir}/pixmaps/xbmc
#%%{_datadir}/pixmaps/xbmc/*.png
#%%{_bindir}/xbmc-j2meremote
#%%{_bindir}/xbmc-ps3d
#%%{_bindir}/xbmc-ps3remote
#%%{_bindir}/xbmc-send
#%%{_bindir}/xbmc-wiiremote

#%%files eventclients-devel
#%%defattr(-,root,root)
#%%dir %{_includedir}/xbmc
#%%{_includedir}/xbmc/xbmcclient.h

%changelog
* Wed Apr 02 2014 Michael Cronenworth <mike@cchtml.com> - 13.0-0.9.Gotham_beta3
- Update to Gotham beta 3

* Tue Mar 25 2014 Michael Cronenworth <mike@cchtml.com> - 13.0-0.8.Gotham_beta2
- Rebuild for ffmpeg bump

* Tue Mar 18 2014 Michael Cronenworth <mike@cchtml.com> - 13.0-0.7.Gotham_beta2
- Switch away from bcond conditionals

* Sun Mar 16 2014 Michael Cronenworth <mike@cchtml.com> - 13.0-0.6.Gotham_beta2
- Update to Gotham beta 2
- use external ffmpeg

* Fri Mar 14 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 13.0-0.5.Gotham_beta1
- Update to Gotham beta 1
- Update Goom/MySQL patch, per RHBZ #1069079

* Fri Feb 21 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 13.0-0.4.Gotham_alpha11
- use internal ffmpeg
- switch to bcond conditionals
- remove hardcoded mysql directory in LIBS, since mysql_config will insert this
  automatically.
- rm BuildRoot

* Mon Jan 27 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 13.0-0.3.Gotham_alpha11
- Update to Gotham alpha 11

* Mon Nov 25 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 13.0-0.3.Gotham_alpha9
- Update to Gotham alpha 9

* Wed Oct 16 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 13.0-0.1.Gotham_alpha8
- Update to Gotham alpha 8
- Add -devel subpackage
- Drop bundled PVR addon (we'll package this separately)

* Thu Jul 04 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.2-5
- Explicitly Require libmad (necessary for the upcoming xbmc 13)

* Wed Jun 05 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.2-4
- Enable _hardened_build

* Tue Jun 04 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.2-3
- force building with libcec (#2798)
- add $DVDREAD_CFLAGS in dvdread patch (#2820)

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 12.2-2
- Rebuilt for x264/FFmpeg

* Mon May 06 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.2-1
- Update to Frodo 12.2
- Rebase hdhomerun and dvdread patches onto 12.2
- Drop upstreamed PA patches
- Drop unused cximage zlib patch

* Thu Apr 25 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.1-2
- Add patches for PA (https://github.com/xbmc/xbmc/pull/2240). Fixes #2655

* Wed Apr 24 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.1-1
- Update to Frodo 12.1
- Update PVR addons snapshot to match snapshot bundled in 12.1

* Tue Feb 05 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-1
- Update to Frodo final
- Add libcec dependency

* Fri Jan 04 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.6.Frodo_rc3
- Update to Frodo RC 3
- Update PVR addons snapshot to match snapshot bundled in rc3

* Fri Dec 28 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 12.0-0.5.Frodo_rc2
- Release number should be bumped on every change when doing 
  pre-release updates
- Remove obsolete MythTV PVR add-on patch from tsp branch

* Wed Dec 26 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.4.Frodo_rc2
- Update to Frodo RC 2
- Update PVR addons snapshot to the latest Git version

* Thu Dec 13 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.4.Frodo_rc1
- Disable crystalhd on non-x86 (by kwizart)
- Enable VAAPI: add BR: libva-devel (#2613)
- Add libcap BR (allows binding on privileged ports)
- Add patch to build pvraddons-with-dependencies

* Wed Dec 12 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.3.Frodo_rc1
- Update to Frodo RC 1

* Wed Dec 05 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.3.Frodo_beta2
- Update to Frodo beta 2
- Drop patch for linking against pulse-simple
- libjpeg is gone in Fedora. Conditionally build against libjpeg-turbo

* Mon Nov 19 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.3.Frodo_alpha7
- Rebase HDHomeRun removal to match upstream's file names
- Conditionally disable libssh BR (unavailable in EL6)

* Mon Nov 19 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.2.Frodo_alpha7
- Add pvr addons

* Tue Nov 13 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 12.0-0.1.Frodo_alpha7
- Update to Frodo alpha 7
- Drop bootstrap patch (system libdvdread works properly now)
- Add upstream patch for linking against pulse-simple
- Add BR for libssh
- Rebase external hdhomerun patch onto alpha7

* Thu Oct  4 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 12.0-0.1.Frodo_alpha6
- Update to Frodo alpha 6
- Use "12.0" as version, rather than "12.8"
- Drop desktop patch (now in Frodo alpha6)
- Add BR for taglib-devel >= 1.8 (libid3tag is being phased out)
- BR for swig and java-devel
- Add CFLAGS option to recognize Samba 4.0 (in f18+)
- Rebase patches to 12.0/Frodo where necessary

* Sun Aug 26 2012 Ken Dreyer <ktdreyer@ktdreyer..com> - 12.8-0.1.Frodo_alpha4
- Upgrade to Frodo alpha 4

* Wed Jul 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 11.0-8
- Switch to pkgconfig(libudev)

* Sun Jul 01 2012 Ken Dreyer <ktdreyer@ktdreyer..com> - 11.0-7
- Set up with_* conditionals for optional dependencies
- Disable hdhomerun and crystalhd for EPEL (#2339)

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 11.0-6
- Rebuilt for FFmpeg

* Wed Jun  6 2012  Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-5
- Add missing BRs for libudev-devel and libplist-devel (needed for AirPlay)

* Tue Jun  5 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-4
- Drop separate dteirney-myth-0.25.patch and ktdryer's boost patch,
  both are merged into tsp's Eden-pvr branch
- Cleanup spec, fix position of scriplets (#2334)

* Sat May 19 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 11.0-3.1
- Changes for EL-6: (#2339)
- Conditionally use gettext-devel instead of gettext-autopoint
- Conditionally disable libbluray and cwiid BRs (unavailable in EL6)
- Patch to build pvr with EL6's boost 1.41

* Thu May 17 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-3
- Remove the old MythTV add-on (no longer works
  and can be confused with the new cmyth-based version)

* Wed May 16 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-2
- Add support for PVR add-ons (backported from tsp's PVR branch to
  Eden), including MythTV
- Workaround bug in compiling against afpfs-ng-devel, will hopefully
  get AirPlay support working (needs testing)
- Drop references to obsolete patches now in Eden
- Add patch from dteirney's branch for MythTV 0.25 support

* Sun Mar 25 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-1
- Update to Eden final 11.0
- Drop libpng 1.5 patches, applied upstream

* Fri Mar  9 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.10.Eden_rc2
- Update to Eden release candidate 2 (rc2)

* Fri Mar  9 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.9.Eden_beta2
- Temporarily drop clientevents package (currently fails to build) to
  fix overall FTBFS.

* Fri Mar  9 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.8.Eden_beta2
- Drop python-sqlite2 BR (obsoleted package), should use internal sqlite3 (#2217)

* Fri Mar 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 11.0-0.7.Eden_beta2
- Rebuilt for FFmpeg/x264

* Sun Jan 29 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.6.Eden_beta2
- Update to Eden beta2

* Fri Dec 30 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.5.Eden_beta1
- Add additional patch from http://trac.xbmc.org/ticket/12001 to
  fix uninitialised pointer with libpng 1.5
- Remove upstreamed, or otherwise obsoleted patches 

* Thu Dec 29 2011 Alex Lancaster <alexlan[AT] fedoraproject org> - 11.0-0.4.Eden_beta1
- Enable libpng 1.5 patch, still needed, upstream bug is at: 
  http://trac.xbmc.org/ticket/12001

* Wed Dec 28 2011 Alex Lancaster <alexlan[AT] fedoraproject org> - 11.0-0.3.Eden_beta1
- Added glx-utils and xorg-x11-utils as Requires, so selecting
  minimal install works out of the box (#1844)

* Wed Dec 28 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.2.Eden_beta1
- Re-enable external ffmpeg
- Add EventClients sub-package (patch thanks to Ben Konrath <ben@bagu.org>)
- More spec cleaning

* Wed Dec 28 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 11.0-0.1.Eden_beta1
- Update to 11.0 beta1
- Disable patches that are obsolete (keep around while testing)
- Update icon cache (#2097)

* Tue Dec 20 2011 Alex Lancaster <alexlan[AT] fedoraproject org> - 10.1-9
- Add patch from OpenElec distribution to fix broken YouTube plugin
  (should fix #1905)

* Wed Dec 14 2011 Xavier Bachelot <xavier@bachelot.org> - 10.1-8
- Add patch for newer libbluray support.
- Add patch for libpng 1.5 support.

* Wed Nov 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 10.1-7
- Rebuilt for libcdio

* Sat Nov  5 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.1-6
- Disable using external ffmpeg for the moment, until such time as
  either we backport a fix for 0.8 ffmpeg or we build XBMC Eden (11.x)
  (see #1962)

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 10.1-5
- Rebuilt for FFmpeg-0.8

* Fri Sep  2 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.1-4
- Remove hal-devel as BuildRequires, dropped in f16 and later:
  http://fedoraproject.org/wiki/Features/HalRemoval
  replaced by udisks, upower, libudev, but not clear if xbmc
  can use those packages yet (fixes #1915).  
- Add dbus-devel, since hal-devel no longer automatically pulls
  package in.

* Tue Apr 05 2011 Nicolas Chauvet <kwizart@gmail.com> - 10.1-3
- Rebuilt for libmysqlclient bump (was built with previous version).

* Wed Mar 30 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.1-2
- Patch from upstream to fix builds for GCC 4.6.x, slightly modified
  to handle previous patches for Makefile.in
  http://trac.xbmc.org/ticket/11383

* Tue Mar 29 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.1-1
- Update to 10.1
- Add support for using system python-imaging and pysqlite modules, thanks to Pierre 
  Ossman for patch (#1575)
- Drop most references to SVNVERSION, upstream now uses git

* Sun Mar 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 10.0-2
- Rebuild for libmysqlclient

* Thu Dec 23 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-1
- Update to 10.0 (Dharma final)

* Sun Dec 12 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.23.Dharma_rc2
- Rebase to Dharma rc2 (SVN r35567)
- Update Python 2.7 patch, to fix DLL search patch problems (#1532).  Thanks to
  Richard Guest for patch.

* Sun Nov 21 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.22.Dharma_rc1
- Need explicit requires for librtmp and libbluray: loaded dynamically
  via XBMC's DLL mechanism which is missed by autodeps

* Fri Nov 19 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.21.Dharma_rc1
- Rebase to Dharma rc1 (SVN r35326)
- Remove conditionals on {librtmp,libbluray}-devel: now present in all
  currently supported releases (f13+)

* Thu Nov 18 2010 Nicolas Chauvet <kwizart@gmail.com> - 10.0-0.20.Dharma_beta4.1
- Rebuilt for libmicrohttpd - ABI bump
 https://admin.fedoraproject.org/updates/libmicrohttpd-0.9.2-3.fc14

* Sun Nov  7 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.20.Dharma_beta4
- Rebase to Dharma beta 4 (SVN r35068)
- Enable libbluray (currently only available for f15+)
- Drop patch disabling SNES (fixed in nasm)

* Thu Oct 14 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.19.Dharma_beta3
- Rebase to Dharma beta3 (SVN r34731)
- Disable VAAPI: crashes XBMC when playing back rtmp streams

* Thu Oct 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 10.0-0.18.Dharma_beta2
- Rebuilt for gcc bug

* Sat Sep 18 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.17.Dharma_beta2
- Enable librtmp support on in F-14 and later (until librtmp is build on F-13)

* Thu Sep 16 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.16.Dharma_beta2
- Enable VAAPI: add BR: libva-freeworld-devel

* Thu Sep 16 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.15.Dharma_beta2
- Add BuildRequires for librtmp-devel, used for various plugins

* Tue Sep 14 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.14.Dharma_beta2
- Rebase to Dharma beta 2 (SVN r33778)

* Tue Sep 14 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.13.Dharma_beta1
- Disable SNES codec (Nintendo sound files) on f14 as nasm >=2.09 has
  trouble compiling with that version on f14 (rhbz#633646)

* Mon Sep 13 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.0-0.12.Dharma_beta1
- Upstream is dropping month from version, using 10.0 as Dharma release version.
- Add explicit Requires for libcrystalhd

* Wed Sep  1 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.9-0.11.Dharma_beta1
- Drop libmodplug/microhttpd patch, no longer needed 

* Wed Sep  1 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.9-0.10.Dharma_beta1
- Rebase to Dharma beta1 release

* Sun Aug 29 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.9.20100820svn32970
- Add -D__STDC_CONSTANT_MACROS for building with ffmpeg > 0.6

* Wed Aug 25 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.8.20100820svn32970
- Default to using /var/run/lirc/lircd (#1325)

* Fri Aug 20 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.7.20100820svn32970
- Rebase patches to r32970 on Dharma branch

* Thu Jul 29 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.7.20100728svn32266
- Add patch from upstream trac ticket 9584 to find Python 2.7
  (needed for F-14+)
- Add BuildRequires: zip

* Thu Jul 29 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.6.20100728svn32266
- Need to conditionally enable gettext-autopoint in BuildRequires
  for F-14+ and gettext otherwise

* Thu Jul 29 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.5.20100728svn32266
- Add gettext-devel to BuildRequires for autopoint

* Wed Jul 28 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.4.20100728svn32266
- Sync with latest Dharma branch (r32266)

* Mon Jul 19 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.3.20100719svn31991
- Remove 24 patches which have been applied upstream, yay!
- Rebased 2 patches: libdvd patch and hdhomerun patch for Dharma
- Add some new patches, some of which have upstream trac tickets,
  others need to
- Renumber patches

* Mon Jul 19 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.2.20100719svn31991
- Sync with Dharma branch

* Mon Jul 19 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 10.5-0.1.20100719svn31977
- Major overhaul for 10.x version of XBMC
- Fix file section for better FHS-compliance
- Drop a lot of patches that have been upstreamed, and rebase others

* Fri May 21 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-19
- Add new BR for libmodplug-devel, expat-devel, libmicrohttpd-devel
  in preparation for 10.x

* Fri Mar 26 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-18
- Exclude ppc64 (not available for F-13+ in any case)

* Fri Mar 26 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-17
- Fixed license tag to include GPLv3+

* Wed Mar 24 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-16
- Add BuildRequires: hdhomerun-devel

* Sun Mar  7 2010 Rolf Fokkens <rolf fokkens[AT]wanadoo nl> - 9.11-15
- Add patch for force using hdhomerun external, had to create a
  hdhomerun-devel package first

* Sat Mar  6 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-14
- Add patch that removes all webserver GoAhead functionality due to
  problematic license
- Drop BR: faac-devel since it was moved to nonfree

* Fri Mar  5 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-13
- Patches to add -lXext to LIBS (thanks Ralf Corsepius)
- Hack to work around ffmpeg sws_scale() incompatibility (thanks Ralf)
- Remove bundled boost, libportaudio, libglew and extra unused zlib
  header from tarball
- Call desktop-file-install as per review guidelines
- Make spyce files executable, quiets rpmlint

* Mon Feb  8 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-12
- More patches from Ralf Corsepius
- Update configure line, specify *FLAGS directly in configure line
  (thanks Ralf)
- Touch rsxs Makefiles to prevent rerunning the autotools (thanks Ralf)
- Add missing %%clean (thanks Ralf)
- Remove even more unused library copies in generate tarball script

* Tue Jan 26 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-11
- Add another patch to ensure Makefile's pass compiler flags properly
  (thanks Ralf C)
- Remove commands no longer needed in install

* Mon Jan 25 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-10
- Patches for RPM_OPT_FLAGS being recognised throughout (thanks
  Ralf C)
- Patch for goom (Ralf C)
- Patch for using external zlib (Ralf C)
- Pass CPPFLAGS to configure (Ralf C)

* Thu Jan 21 2010 Rolf Fokkens <rolf fokkens[AT]wanadoo nl> - 9.11-9
- increase compression ratio of tarball by compressing with cx
  the src.rpm is now about 20% smaller
- remove patch0 and patch1, they are obsolete now
- rename patch2 and patch10 to more meaningful name

* Thu Jan 21 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-8
- Update xbmc script patch (thanks Ralf C)
- Reorder patches, add upstream tickets where possible
- Drop SVN_REV from line until exact version clarified

* Mon Jan 18 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-7
- Remove bundled copies of libraries, and code that we can't
  distribute from upstream tarball with script
- Drop patch against ffmpeg which we removed from tarball
- Trim description

* Sun Jan 17 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-6
- Add patch for web server segfaults on 64-bit (thanks Ralf Corsepius)
- Drop patch backup for .spyce, causes packaging problems (thanks Ralf
  Corsepius)
- Remove bogus header from install (thanks Ralf Corsepius)
- More comprehensive pre-built Win32 binary removal (thanks Ralf
  Corsepius)
- Add SVN_REV to configure line for plugins (thanks Graeme Gillies)

* Tue Jan  5 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-5
- Remove unnecessary BR: mysql-libs
- Prune out unneeded stuff from build (thanks Rolf Fokkens)
- Remove libraries not compiled (thanks Rolf Fokkens)
- Patch to some nasty GCC warnings (thanks Ralf Corsepius)

* Thu Dec 31 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-4
- Patches to fix installation paths to /usr/lib/ (thanks Ralf Corsepius)
- Patch to fix other issues: random number library (thanks Ralf Corsepius)

* Wed Dec 30 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 9.11-3
- Cleanup spec for submission to RPM Fusion
- Fix changelog entries to use standard numbering to quiet rpmlint
- Use standard URL for sourceforge tarballs
- Add BR: pulseaudio-libs-devel and others
- Add patch that removes comments in rules in Makefile.in that
  prevented install target working

* Tue Dec 29 2009 Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-2
- use external libcdio again, patch by MaestroDD

* Fri Dec 25 2009 Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-1
- Update to 9.11

* Fri Dec 18 2009 Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-0.5.rc1
- Update to 9.11 rc1

* Fri Dec 11 2009 Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-0.4.beta2
- Update to 9.11 beta2

* Tue Dec 1 2009  Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-0.3.beta1
- Force using external libdvdread and libdvdcss. libdvdnav is stil internal
  as xbmc needs its internals.

* Sat Nov 28 2009  Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-0.2.beta1
- replaced dependency on libdts by libdca
- removed dependency on external libcdio, use included one instead
  now detection of CD's and DVD's works again
- Compiles and runs on Fedora 11
- Update to 9.11 beta1

* Sun Nov 15 2009  Rolf Fokkens <rolf fokkens wanadoo nl> - 9.11-0.1.alpha2
- Compiles and runs on Fedora 11
- Update to 9.11 alpha2

* Fri May 15 2009 Scott Harvanek <scotth@login.com> - 9.04-1
- Update to 9.04

* Wed Jan 28 2009 Scott Harvanek <scotth@login.com> - 8.10-3
- Added requires for
- alsa-plugins-pulseaudio, libogg, libmad, libvorbis

* Fri Jan 2 2009 Scott Harvanek <scotth@login.com> - 8.10-2
- Patch for English language strings.xml

* Thu Nov 27 2008 Scott Harvanek <scotth@login.com> - 8.10-1
- v8.10
- Fedora 10 RPM
