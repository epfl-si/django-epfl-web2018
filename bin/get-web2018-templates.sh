#!/usr/bin/env bash
set -euo pipefail

WEB2018_VERSION="8.8.0"
WEB2018_TEMPLATES_PATH="django_epfl_web2018/templates/web2018/includes"
WEB2018_STATIC_PATH="django_epfl_web2018/static/web2018/icons"
WEB2018_RELEASES_URL="https://raw.githubusercontent.com/epfl-si/epfl-theme-elements/v${WEB2018_VERSION}/dist-cdn/releases.tar.xz"
WEB2018_RELEASES_PREFIX="vhosts/web2018.epfl.ch/${WEB2018_VERSION}"

# Ensure required tools are available
for tool in wget tar; do
  if ! command -v "${tool}" &> /dev/null; then
    echo "Error: ${tool} is not installed." >&2
    exit 1
  fi
done

TMP_DIR="$(mktemp -d)" || { echo "Error: mktemp failed." >&2; exit 1; }
trap 'rm -rf "${TMP_DIR}"' EXIT

# Download releases tarball
echo "Downloading ${WEB2018_RELEASES_URL}..."
wget \
  --quiet \
  --output-document="${TMP_DIR}/releases.tar.xz" \
  "${WEB2018_RELEASES_URL}" || { echo "Error: failed to download ${WEB2018_RELEASES_URL}" >&2; exit 1; }

# Extract templates (includes and error pages)
echo "Extracting templates..."
tar \
  --extract \
  --file="${TMP_DIR}/releases.tar.xz" \
  --directory="${WEB2018_TEMPLATES_PATH}" \
  --strip-components=4 \
  "${WEB2018_RELEASES_PREFIX}/includes" \
  "${WEB2018_RELEASES_PREFIX}/errors"

# Extract favicon
echo "Extracting favicon..."
tar \
  --extract \
  --file="${TMP_DIR}/releases.tar.xz" \
  --directory="${WEB2018_STATIC_PATH}" \
  --strip-components=4 \
  "${WEB2018_RELEASES_PREFIX}/icons/favicon.ico"

TEMPLATES_TO_REMOVE=(
  "cf-waf-block.html"
  "cf-waf-challenge.html"
  "drawer-de.html"
  "drawer-en.html"
  "drawer-fr.html"
  "drawer-it.html"
)

for file in "${TEMPLATES_TO_REMOVE[@]}"; do
  if [[ -f "${WEB2018_TEMPLATES_PATH}/${file}" ]]; then
    echo "Removing ${file}..."
    rm "${WEB2018_TEMPLATES_PATH}/${file}"
  fi
done

# Replace GTM markers with Django template conditionals
# so analytics can be opted out.
echo "Replacing GTM markers with Django conditionals..."
for template in "${WEB2018_TEMPLATES_PATH}"/*.html; do
  if grep -qF "<!-- GTM-START -->" "${template}"; then
    sed -i \
      -e '1i {% load web2018 %}' \
      -e "1i {% web2018_setting 'ENABLE_ANALYTICS' as enable_analytics %}" \
      -e 's|<!-- GTM-START -->|{% if enable_analytics %}|' \
      -e 's|<!-- GTM-END -->|{% endif %}|' \
      "${template}"
    echo "  Updated $(basename "${template}")"
  fi
done

# Replace FOOTER-EXTRA-LINKS markers with a Django template include
# so downstream projects can override extra footer links.
echo "Replacing FOOTER-EXTRA-LINKS markers with a Django include..."
for template in "${WEB2018_TEMPLATES_PATH}"/*.html; do
  if grep -qF "<!-- FOOTER-EXTRA-LINKS -->" "${template}"; then
    sed -i \
      -e 's|<!-- FOOTER-EXTRA-LINKS -->|{% include "web2018/includes/footer-extra-links.html" %}|' \
      "${template}"
    echo "  Updated $(basename "${template}")"
  fi
done
