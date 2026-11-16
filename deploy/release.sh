#!/usr/bin/env bash
set -euo pipefail
environment=${1:?environment required}
image=${2:?digest required}
[[ "$environment" == development || "$environment" == production ]]
[[ "$image" =~ ^ghcr\.io/[a-z0-9._/-]+@sha256:[a-f0-9]{64}$ ]]
state=${ATLAS_DEPLOY_HOME:-"$HOME/.config/fieldnote-atlas"}/$environment
umask 077
exec 9>"$state/deploy.lock"
flock 9
export APP_ENV="$environment"
export APP_IMAGE="$image"
export APP_VERSION="${image##*@}"
compose=(docker compose -p "atlas-$environment" --env-file "$state/host.env" -f deploy/compose.yml)
if "${compose[@]}" pull && "${compose[@]}" up -d --wait --wait-timeout 150 &&
   "${compose[@]}" exec -T app curl -fsS http://127.0.0.1:8000/api/atlas >/dev/null &&
   "${compose[@]}" exec -T app curl -fsS http://127.0.0.1:8000/api/version |
     python3 -c 'import json,os,sys; d=json.load(sys.stdin); sys.exit(d != {"environment": os.environ["APP_ENV"], "version": os.environ["APP_VERSION"]})'; then
  if [[ -f "$state/current" ]] && [[ "$(cat "$state/current")" != "$image" ]]; then
    cp "$state/current" "$state/previous"
  fi
  printf '%s\n' "$image" > "$state/current.tmp"
  mv "$state/current.tmp" "$state/current"
else
  if [[ -s "$state/current" ]]; then
    APP_IMAGE=$(cat "$state/current")
    APP_VERSION=${APP_IMAGE##*@}
    "${compose[@]}" up -d --wait --wait-timeout 150
  fi
  exit 1
fi
