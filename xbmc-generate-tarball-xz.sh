#!/bin/sh

VERSION=${1-9.11}

tar -xzvf xbmc-$VERSION.tar.gz

cd xbmc-$VERSION

# remove bundled libraries (including zlib and OSX), saves space and forces using external versions
# also remove legally problematic libGoAhead library
for i in libass libcdio libCDRip libcurl libenca libfribidi liblzo libmms libpcre libsamplerate sqLite/sqlite libPython/Python cximage-6.0/zlib libid3tag/zlib zlib libSDL-OSX boost libportaudio libglew libGoAhead libhdhomerun
do
    rm -r xbmc/lib/$i
done

# bundled win32 binaries
rm -r xbmc/visualizations/XBMCProjectM/win32

# remove various headers 
rm xbmc/FileSystem/zlib.h

# remove more bundled codecs
# libfaad2, libmad needs upstream patches to be able to remove from tarball
# even though the bundled libaries aren't, I think, compiled
for i in ffmpeg liba52 libmpeg2 libdts
do
    rm -r xbmc/cores/dvdplayer/Codecs/$i
done

# remove DVD stuff we can't ship, or is already in external libraries
for i in libdvdcss libdvdread includes 
do
    rm -r xbmc/cores/dvdplayer/Codecs/libdvd/$i
done

# remove all prebuilt binaries (e.g., .so files and Win32 DLLs)
find \( -name '*.so' -o -name '*.DLL' -o -name '*.dll' -o -name '*.lib' -o -name '*.zlib' -o -name '*.obj' -o -name '*.exe' -o -name '*.vis' \) | xargs rm -f

# remove other packages that should be system-wide 
rm -rf lib

cd -

# repack
tar -cJvf xbmc-$VERSION-patched.tar.xz xbmc-$VERSION
