#!/bin/sh

MAJORVERSION=10.0

# pull from Dharma branch
SVNURL=https://xbmc.svn.sourceforge.net/svnroot/xbmc/branches/Dharma

# uncomment this to switch to trunk
#SVNURL=https://xbmc.svn.sourceforge.net/svnroot/xbmc/trunk

# use SVN version number passed from script, or otherwise use default
SVNVERSION=${1-35326}
# uncomment following if you want to always pull from tip of branch
# SVNVERSION=$(svn info $SVNURL  |grep "Revision:"|cut -d' ' -f2)

#VERSION=$MAJORVERSION-$SVNVERSION
VERSION=Dharma_rc1

# remove existing checkout
rm -r xbmc-$VERSION

#svn export -r $SVNVERSION $SVNURL xbmc-$VERSION

# don't need to extra tarball, already expanded
# comment out with tarball
tar -xzvf xbmc-$VERSION.tar.gz

# rename tarball directory
mv -i $VERSION xbmc-$VERSION
cd xbmc-$VERSION

# remove bundled libraries (including zlib and OSX), saves space and forces using external versions
# also remove legally problematic libGoAhead library
#for i in libass libcdio libCDRip libcurl libenca libfribidi liblzo libmms libpcre libsamplerate sqLite/sqlite libPython/Python cximage-6.0/zlib libid3tag/zlib zlib libSDL-OSX boost libportaudio libglew libGoAhead libhdhomerun
for i in liblzo libmms libsamplerate sqLite/sqlite libPython/Python cximage-6.0/zlib libid3tag/zlib zlib boost libhdhomerun
do
    rm -r xbmc/lib/$i
done

# bundled win32 binaries
rm -r xbmc/visualizations/XBMCProjectM/win32

# remove more bundled codecs
# libfaad2, libmad needs upstream patches to be able to remove from tarball
# even though the bundled libaries aren't, I think, compiled
# grrr, have to keep in ffmpeg for now (2010-07-019) since upstream
# seems to require files within that subdirectory <sigh>
for i in liba52 libmpeg2 libdts
do
    rm -r xbmc/cores/dvdplayer/Codecs/$i
done


# remove DVD stuff we can't ship, or is already in external libraries
for i in libdvdcss libdvdread includes 
do
    rm -r xbmc/cores/dvdplayer/Codecs/libdvd/$i
done

# remove all prebuilt binaries (e.g., .so files and Win32 DLLs)
find \( -type f -name '*.so' -o -name '*.DLL' -o -name '*.dll' -o -name '*.lib' -o -name '*.zlib' -o -name '*.obj' -o -name '*.exe' -o -name '*.vis' \) | xargs rm -f

# remove all other packages that should be system-wide
# except for libass, cpluff, jsoncpp (need to figure out how to
# remove these too)
# xbmc-dll-symbols seems to be XBMC-specific
for i in enca freetype fribidi libcdio libcrystalhd libcurl-OSX libiconv liblame libmicrohttpd libmicrohttpd_win32 libmodplug libmysql_win32 libSDL-OSX libssh_win32 pcre libbluray libbluray_win32 librtmp bzip2
do
    rm -r lib/$i
done

# TODO/FIXME: remove tools/XBMCLive/ and other things under tools/ 
# also remove anything to do with win32
for i in arm MingwBuildEnvironment PackageMaker win32buildtools XBMCLive XBMCTex
do
    rm -r tools/$i
done

cd -

# repack
tar -cJvf xbmc-$VERSION-patched.tar.xz xbmc-$VERSION

echo "Release:"
echo "$(date +'%Y%m%d')svn${SVNVERSION}"

