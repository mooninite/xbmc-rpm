#!/bin/sh

set -e

# The xbmc-pvr-addon software does not yet use version numbers, so we'll
# just use git hashes for identifiers.

# Upstream xbmc also hardcodes a Git hash for OSes that bundle
# xbmc-pvr-addons.  Let's try using the same hash that upstream uses. It
# can be found in the source tree like so:
#   grep ^VERSION tools/darwin/depends/xbmc-pvr-addons/Makefile
COMMIT=590f862065d0f07d399fe4443a72dc37394becb4
GITHASH=${COMMIT:0:7}
GITHUBURL=https://github.com/opdenkamp/xbmc-pvr-addons/archive/$GITHASH.zip

# download zipball
if [[ ! -f xbmc-pvr-addons-$GITHASH.zip ]]; then
    curl -o xbmc-pvr-addons-$GITHASH.zip -L $GITHUBURL
fi

# extract zipball
find . -maxdepth 1 -name "xbmc-pvr-addons-$GITHASH*" -type d -exec rm -r '{}' \;
unzip xbmc-pvr-addons-$GITHASH.zip

# Shorten GitHub's auto-generated top-level directory.
if [[ -d pvr-addons ]]; then
       rm -r pvr-addons
fi
find . -maxdepth 1 -name "xbmc-pvr-addons-$GITHASH*" -type d -exec mv '{}' pvr-addons \;

pushd pvr-addons

# remove Windows stuff
rm -r project

popd

# repack
tar -cJvf xbmc-pvr-addons-$GITHASH-patched.tar.xz pvr-addons

rm -r pvr-addons
