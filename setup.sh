#!/bin/sh
# Setup script for shared git hooks

echo ">>> Starting Git hooks setup..."

git config core.hooksPath .githooks
echo "Set Git hooks path to .githooks"

echo ">>> Git hooks setup completed."
