#!/usr/bin/env bash
git pull
date_str=$(TZ=':Asia/Shanghai' date '+%Y-%m-%d %T')
echo "${date_str}: Record it" > ./README.md

git add ./README.md
git commit -m "${date_str}"
