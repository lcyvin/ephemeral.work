#!/bin/bash
curl -X PUT -H 'Accept: application/vnd.github.barred-rock-preview' -H "authToken: $GITHUB_AUTH" --data "{vcs: git, vcs_url: $CANNONICAL_MAIN_REPO}" https://api.github.com/repos/lcyvin/ephemeral.work/import
