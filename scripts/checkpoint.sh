#!/usr/bin/env bash
# Commita e envia todo o estado atual do laboratório para o GitHub.
# Uso: scripts/checkpoint.sh "mensagem descritiva do que avançou"
set -euo pipefail

cd "$(dirname "$0")/.."

if [ -z "${1:-}" ]; then
  echo "Uso: $0 \"mensagem do checkpoint\"" >&2
  exit 1
fi

git add -A
if git diff --cached --quiet; then
  echo "Nada para commitar."
  exit 0
fi

git commit -m "$1"
git push
