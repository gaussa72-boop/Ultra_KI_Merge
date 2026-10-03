#!/usr/bin/env bash
set -euo pipefail

OWNER="gaussa72-boop"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$ROOT/.ai-repo-merge-work"
DEST="$ROOT/integrated_repositories"

REPOS=(
  "Quantum.AI."
  "AI-Quantumlight"
  "UltraKI.AI"
  "Quantum-KI-CAT.CHAT."
  "IONOS-KI"
  "ultra-ki-v2"
  "Quantum.KI.Ultra.Pro.V2"
  "galactic-ai-v3"
  "Note-KI"
)

rm -rf "$WORK"
mkdir -p "$WORK" "$DEST"

for repo in "${REPOS[@]}"; do
  echo "=== $repo ==="
  git clone --depth 1 "git@github.com:$OWNER/$repo.git" "$WORK/$repo"
  rm -rf "$WORK/$repo/.git"
  mkdir -p "$DEST/$repo"

  rsync -a "$WORK/$repo/" "$DEST/$repo/"     --exclude '.git/'     --exclude '.venv/'     --exclude 'venv/'     --exclude 'node_modules/'     --exclude '__pycache__/'     --exclude '.pytest_cache/'     --exclude '.mypy_cache/'     --exclude 'dist/'     --exclude 'build/'     --exclude '.DS_Store'     --exclude '.env'     --exclude '*.pyc'     --exclude '*.pyo'     --exclude '*shopify*'     --exclude '*Shopify*'     --exclude '*printful*'     --exclude '*Printful*'     --exclude '*lichtreich*'     --exclude '*Lichtreich*'
done

rm -rf "$WORK"
echo
echo "MERGE-QUELLEN BEREIT:"
find "$DEST" -maxdepth 2 -type f | sort | head -200
echo
echo "Die Original-Repositories bleiben unverändert."
