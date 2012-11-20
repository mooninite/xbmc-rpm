#!/bin/sh

set -e

# The xbmc-pvr-addon software does not yet use version numbers, so we'll
# just use git hashes for identifiers.

GITHASH=1e666ced21
GITHUBURL=https://github.com/opdenkamp/xbmc-pvr-addons/archive/$GITHASH.zip

# download zipball
if [[ ! -f xbmc-pvr-addons-$GITHASH.zip ]]; then
    curl -o xbmc-pvr-addons-$GITHASH.zip -L $GITHUBURL
fi

# extract zipball
find . -maxdepth 1 -name "xbmc-pvr-addons-$GITHASH*" -type d -exec rm -r '{}' \
unzip xbmc-pvr-addons-$GITHASH.zip

# Shorten GitHub's auto-generated top-level directory.
if [[ -d pvr-addons ]]; then
       rm -r pvr-addons
fi
find . -maxdepth 1 -name "xbmc-pvr-addons-$GITHASH*" -type d -exec mv '{}' pvr-

pushd pvr-addons

# remove Windows stuff
rm -r project

popd

# repack
tar -cJvf xbmc-pvr-addons-$GITHASH-patched.tar.xz pvr-addons

rm -r pvr-addons
