#!/usr/bin/env bash

# Executables.
GIT=$(command -v git)
export GIT

# Drupal variables.
export DRUPAL="core/scripts/drupal"
export PROFILE=$2
export PATCH=$3

has_profile() {
  if [[ -z "${PROFILE}" ]]; then
    export PROFILE="standard"
  else
    if [[ "${PROFILE}" = "standard" ]]; then
      export PROFILE="standard"
    elif [[ "${PROFILE}" = "minimal" ]]; then
      export PROFILE="minimal"
    elif [[ "${PROFILE}" = "umami" ]]; then
      export PROFILE="demo_umami"
    # In case we forget to pass a profile and pass a patch instead, we're smart
    # enough to catch it for later. 
    elif [[ "${PROFILE}" == https://*.patch ]]; then
      export PATCH=${PROFILE}
      export PROFILE="standard"
    else
      echo "This is not a valid profile: allowed values are 'standard', 'minimal' and 'umami'."
      exit 0
    fi
  fi
}

apply_patch() {
  WGET=$(command -v wget)
  BASENAME=$(command -v basename)

  ${WGET} "${PATCH}"
  ${GIT} apply -v $(basename *.patch)
}

has_patch() {
  if [[ ! -z "${PATCH}" ]] && [[ "${PATCH}" == https://*.patch ]]; then
    apply_patch
  fi
}

is_drupal() {
  if [[ -f ${DRUPAL} ]]; then
    echo "Drupal codebase detected. Proceeding..."
  else
    echo "This doesn't seem to be a Drupal codebase. Aborting..."
    exit 0
  fi
}

git_cleanup() {
  ${GIT} clean -fdx
  ${GIT} reset --hard
  ${GIT} pull
}

install_drupal() {
  COMPOSER=$(command -v composer)
  PHP=$(command -v php)
  SITENAME="drupal"
  HOST="localhost"
  PORT="8888" # Other option could be $(shuf -i8000-8999 -n1)

  if [[ -f "composer.json" ]]; then
    ${COMPOSER} install
    ${PHP} ${DRUPAL} quick-start ${PROFILE} --site-name ${SITENAME} --host ${HOST} --port ${PORT}
  fi
}

quick-start() {
  has_profile
  is_drupal
  git_cleanup
  has_patch
  install_drupal
}

quick-restart() {
  is_drupal
  install_drupal
}

drupal_cleanup() {
  DRUPAL_DIRS=("vendor" "sites/default")
  SUDO=$(command -v sudo)
  RM=$(command -v rm)

  for DRUPAL_DIR in "${DRUPAL_DIRS[@]}"; do
    if [[ -d "${DRUPAL_DIR}" ]]; then
      ${SUDO} "${RM}" -Rf ./"${DRUPAL_DIR}" || exit
    fi
  done
}

quick-clean() {
  is_drupal
  drupal_cleanup
  git_cleanup
}

# Allows to expand to the arguments of the command line that are specified.
"$@"
