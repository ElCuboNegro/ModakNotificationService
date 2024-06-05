# scripts/bump_version.sh

#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 [major|minor|patch]"
  exit 1
fi

part=$1

current_version=$(cat VERSION)
IFS='.' read -r -a version_parts <<< "$current_version"

major=${version_parts[0]}
minor=${version_parts[1]}
patch=${version_parts[2]}

case $part in
  major)
    major=$((major + 1))
    minor=0
    patch=0
    ;;
  minor)
    minor=$((minor + 1))
    patch=0
    ;;
  patch)
    patch=$((patch + 1))
    ;;
  *)
    echo "Invalid part: $part. Use major, minor, or patch."
    exit 1
    ;;
esac

new_version="$major.$minor.$patch"
echo $new_version > VERSION
echo "Version bumped to $new_version"
