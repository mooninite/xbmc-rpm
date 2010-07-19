%global SVNVERSION 31977
%global DIRVERSION %{version}-%{SVNVERSION}

Name: xbmc
Version: 10.5
Release: 0.1.20100719svn%{SVNVERSION}%{?dist}
URL: http://www.xbmc.org/

Source0: %{name}-%{DIRVERSION}-patched.tar.xz
# xbmc contains code that we cannot ship, as well as redundant private
# copies of upstream libraries that we already distribute.  Therefore
# we use this script to remove the code before shipping it.
# Download the upstream tarball from:
# http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# and invoke this script while in the directory where the tarball is located:
# ./xbmc-generate-tarball-xz.sh <version>
# where <version> is the particular version being used
Source1: xbmc-generate-tarball-xz.sh

# look for libdca, rather than libdts
# http://xbmc.org/trac/ticket/8040
Patch1:	xbmc-9.11-libdca.patch

# Needs work before being submitted upstream
Patch2:	xbmc-9.11-b1-dvdlibs-external.patch

# http://xbmc.org/trac/ticket/8026 (this will be in next release)
Patch3:	xbmc-9.11-use_cdio_system_headers_on_non_win32.patch 

# Next 3 patches to use %{_libdir}
# http://xbmc.org/trac/ticket/8590
Patch4:	xbmc-9.11-fix-Makefile.in.patch
Patch5: xbmc-9.11-Makefile.include.in.diff
Patch6: xbmc-9.11-xbmc.sh.diff

# Next 2 patches submitted upstream
# http://www.xbmc.org/trac/ticket/8629
Patch7: xbmc-9.11-spyce.diff
Patch8: xbmc-9.11-RandomNumberGenerators.hpp.diff

# Needs work before being submitted upstream
Patch9: xbmc-9.11-remlibass.patch

# Fixes GCC warning: partial backport to 9.11
# (should be fixed in next release)
Patch10: xbmc-9.11-changeset-26191.diff

# remove goahead completely from compilation, it's been replaced
# by libmicrohttpd in SVN, so should add that BuildRequires for 10.5
# and drop this patch
Patch11: xbmc-9.11-remove-goahead.patch

# Next 12 patches submitted upstream:
# http://www.xbmc.org/trac/ticket/8629
Patch12: xbmc-9.11-external-zlib.diff
Patch13: xbmc-9.11-goom-missing.diff
Patch14: xbmc-9.11-rsxs-0.9.diff
Patch15: xbmc-9.11-Weather.diff
Patch16: xbmc-9.11-XBMCProjectM-cmake.diff
Patch17: xbmc-9.11-cflags.patch
Patch18: xbmc-9.11-configure.patch
Patch19: xbmc-9.11-gymcodec.patch
Patch20: xbmc-9.11-macdll.patch
Patch21: xbmc-9.11-maclib.patch
Patch22: xbmc-9.11-libid3tag.patch
Patch23: xbmc-9.11-librtv.patch

# these next 2 are (hopefully temporary) hacks
Patch24: xbmc-9.11-swscale.diff
Patch25: xbmc-9.11-xext.diff

# an attempt to force hdhomerun to be external
Patch26: xbmc-9.11-hdhomerun.patch

# new patches for bootstrap
Patch27: xbmc-10-bootstrap.patch

# and libdvdread (supercedes above patch)
Patch28: xbmc-10-dvdread.patch

# and new problem with zlib in cximage
Patch29: xbmc-10-disable-zlib-in-cximage.patch

# grrr, why if an external library is detected does it require that the
# directory exist in the tarball?
Patch30: xbmc-10-remove-libmodplug-libmicrohttpd.patch

# rebase hdhomerun
Patch31: xbmc-10-hdhomerun.patch

# fix "@#" in Makefile which seem to screw things up
Patch32: xbmc-10-Makefile.patch

ExcludeArch: ppc64
Buildroot: %{_tmppath}/%{name}-%{version}
Summary: Media center
License: GPLv2+ and GPLv3+
Group: Applications/Multimedia
BuildRequires: desktop-file-utils
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: fontconfig-devel
BuildRequires: fribidi-devel
BuildRequires: glibc-devel
BuildRequires: hal-devel
BuildRequires: glew-devel
BuildRequires: libstdc++-devel
BuildRequires: glib2-devel
BuildRequires: libjasper-devel
BuildRequires: libjpeg-devel
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
BuildRequires: ffmpeg-devel
BuildRequires: faad2-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libdca-devel
BuildRequires: libass-devel >= 0.9.7
BuildRequires: hdhomerun-devel
BuildRequires: libcrystalhd-devel
BuildRequires: libmodplug-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: expat-devel

%description
XBMC media center is a free cross-platform media-player jukebox and
entertainment hub.  XBMC can play a spectrum of of multimedia formats,
and featuring playlist, audio visualizations, slideshow, and weather
forecast functions, together third-party plugins.

%prep

%setup -q -n %{name}-%{DIRVERSION}

#patch1 -p1 -b .dtsdca
#   patch2 -p1 -b .dvdlibs
#patch3 -p1 -b .cdio
#patch4 -p0 -b .makefilein
#patch5 -p1 -b .makefileincl
#patch6 -p1 -b .xbmcsh
#patch7 -p1
#patch8 -p1 -b .rand
#   patch9 -p1 -b .remlibass
#patch10 -p1 -b .gccwarning
#patch11 -p0 -b .removegoahead
#patch12 -p1 -b .zlib
#patch13 -p1 -b .goom
#patch14 -p1 -b .rsxs
#patch15 -p1 -b .weather
#patch16 -p1 -b .projectm
#patch17 -p1 -b .cflags
#patch18 -p1
#patch19 -p1
#patch20 -p1
#patch21 -p1
#patch22 -p1
#patch23 -p1
#patch24 -p1
#patch25 -p1
#   patch26 -p1 -b .hdhomerun
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0
%patch31 -p1
%patch32 -p0

# Prevent rerunning the autotools.
touch -r xbmc/screensavers/rsxs-0.9/aclocal.m4 \
$(find xbmc/screensavers/rsxs-0.9 \( -name 'configure.*' -o -name 'Makefile.*' \))

%build

chmod +x bootstrap
./bootstrap
# Can't use export nor %%configure (implies using export), because
# the Makefile pile up *FLAGS in this case.
./configure \
--prefix=%{_prefix} --bindir=%{_bindir} --includedir=%{_includedir} \
--libdir=%{_libdir} --datadir=%{_datadir} \
--enable-goom \
--enable-external-ffmpeg --enable-external-python \
--disable-libdts --disable-liba52 \
--disable-dvdcss \
--disable-optimizations --disable-debug \
SVN_REV=%{SVNVERSION} \
CPPFLAGS="-I/usr/include/ffmpeg" \
CFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/ffmpeg" \
CXXFLAGS="$RPM_OPT_FLAGS -fPIC -I/usr/include/ffmpeg" \
LDFLAGS="-fPIC" \
LIBS="-L%{_libdir}/mysql -lhdhomerun $LIBS" \
ASFLAGS=-fPIC

# disable the following:
# --enable-external-libraries
# enumerate all the external libraries because the libdts/liba52 detection 
# is broken upstream: http://trac.xbmc.org/ticket/9277

make %{?_smp_mflags} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# remove the doc files from unversioned /usr/share/doc/xbmc, they should be in versioned docdir
rm -r $RPM_BUILD_ROOT/%{_datadir}/xbmc/doc/

desktop-file-install \
 --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
 $RPM_BUILD_ROOT%{_datadir}/applications/xbmc.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc copying.txt keymapping.txt LICENSE.GPL README.linux
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%{_libdir}/xbmc
%{_datadir}/xsessions/XBMC.desktop
%{_datadir}/applications/xbmc.desktop
%{_datadir}/pixmaps/xbmc.png

%changelog
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
