#!/bin/bash
curl -X PUT -H 'Accept: application/vnd.github.barred-rock-preview' -H "authToken: $GITHUB_AUTH" https://api.github.com/repos/lcyvin/ephemeral.work/import
