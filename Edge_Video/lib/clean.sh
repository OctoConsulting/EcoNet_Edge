#!/bin/bash
# script to clean up the libraries when no longer needed

set -x
set -e
set -u

rm ./*.js*
rm ./*.css*