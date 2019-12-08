#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quick-drupal is the quickest way to install, test and contribute to Drupal."""

import sys
from os.path import isfile


# Drupal variables.
DRUPAL = "core/scripts/drupal"
# export PROFILE=$2
# export PATCH=$3

# function has_profile() {
#   if [[ -z "${PROFILE}" ]]; then
#     export PROFILE="standard"
#   else
#     case "${PROFILE}" in
#       standard)
#         export PROFILE="standard"
#       ;;
#       minimal)
#         export PROFILE="minimal"
#       ;;
#       umami)
#         export PROFILE="demo_umami"
#       ;;
#       # In case we forget to pass a profile and pass a patch instead, we're
#       # smart enough to catch it for later.
#       https://*.patch)
#         export PATCH=${PROFILE}
#         export PROFILE="standard"
#       ;;
#       *)
#         echo "Usage: $(basename "${0}") {standard|minimal|umami}"
#         exit 1
#     esac
#   fi
# }

# function has_patch() {
#   if [[ ! -z "${PATCH}" ]] && [[ "${PATCH}" == https://*.patch ]]; then
#     apply_patch
#   fi
# }

# function apply_patch() {
#   WGET=$(command -v wget)
#   BASENAME=$(command -v basename)

#   ${WGET} "${PATCH}"
#   ${GIT} apply -v $(basename *.patch)
# }


def is_drupal():
    """Check whether or not we're executing the script against a Drupal codebase."""
    if not isfile(DRUPAL):
        sys.exit("This doesn't seem to be a Drupal codebase. Aborting...")
    print("Drupal codebase detected. Proceeding...")


# function git_cleanup() {
#   ${GIT} clean -fdx
#   ${GIT} reset --hard
#   ${GIT} pull
# }

# function install_drupal() {
#   COMPOSER=$(command -v composer)
#   PHP=$(command -v php)
#   SITENAME="drupal"
#   HOST="localhost"
#   PORT="8888" # Other option could be $(shuf -i8000-8999 -n1)

#   if [[ -f "composer.json" ]]; then
#     ${COMPOSER} install
#     ${PHP} ${DRUPAL} quick-start ${PROFILE} --site-name ${SITENAME} --host ${HOST} --port ${PORT}
#   fi
# }

def quick_start():
    """Spin up a test Drupal instance, optionally with a patch."""
    # has_profile()
    is_drupal()
    # has_patch()
    # install_drupal()

# function drupal_cleanup() {
#   DRUPAL_DIRS=("vendor" "sites/default")
#   SUDO=$(command -v sudo)
#   RM=$(command -v rm)

#   for DRUPAL_DIR in "${DRUPAL_DIRS[@]}"; do
#     if [[ -d "${DRUPAL_DIR}" ]]; then
#       ${SUDO} "${RM}" -Rf ./"${DRUPAL_DIR}" || exit
#     fi
#   done
# }

def quick_clean():
    """Cleans up the Drupal repository. This is A DESTRUCTIVE OPERATION"""
    is_drupal()
    # drupal_cleanup()
    # git_cleanup()

quick_start()
