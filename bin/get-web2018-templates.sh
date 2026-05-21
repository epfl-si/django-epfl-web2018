#!/usr/bin/env bash

WEB2018_VERSION="8.5.0"
WEB2018_STATIC_PATH="django_epfl_web2018/static/web2018/icons"
WEB2018_TEMPLATES_PATH="django_epfl_web2018/templates/web2018/includes"
WEB2018_URL="https://web2018.epfl.ch/${WEB2018_VERSION}/download-me.html"

# Ensure required tools are available
if ! command -v wget &> /dev/null; then
  echo "Error: wget is not installed." >&2
  exit 1
fi

# Mirror templates
wget \
  --no-parent \
  --no-directories \
  --recursive \
  --timestamping \
  --level=1 \
  --directory-prefix="${WEB2018_TEMPLATES_PATH}" \
  "${WEB2018_URL}"

TEMPLATES_TO_REMOVE=(
  "robots.txt"
  "download-me.html"
  "drawer-de.html"
  "drawer-en.html"
  "drawer-fr.html"
)

for file in "${TEMPLATES_TO_REMOVE[@]}"; do
  if [[ -f "${WEB2018_TEMPLATES_PATH}/${file}" ]]; then
    echo "Removing ${file}..."
    rm "${WEB2018_TEMPLATES_PATH}/${file}"
  fi
done

wget \
  --timestamping \
  --directory-prefix="${WEB2018_STATIC_PATH}" \
  https://web2018.epfl.ch/${WEB2018_VERSION}/icons/favicon.ico
