#!/bin/bash

echo "🚀 Start deploy process..."

ssh -tq root@213.239.193.208 <<'EOF'
  set -e

  echo "🔧 Sourcing NVM..."
  source ~/.nvm/nvm.sh || echo "⚠️ Failed to source NVM"

  echo "📂 Changing to project directory..."
  cd /var/www/html/ergodocs || { echo "❌ Failed to cd to project dir"; exit 1; }

  echo "🔄 Pulling latest changes from Git..."
  git pull || { echo "❌ Git pull failed"; exit 1; }

  echo "🧹 Cleaning old MkDocs site..."
  rm -rf site || echo "⚠️ Failed to remove site dir"

  echo "🏗 Building MkDocs site..."
  mkdocs build || { echo "❌ MkDocs build failed"; exit 1; }

EOF

echo "✅ Deployed Successfully!"
exit 0
