#!/usr/bin/env bash
# The script prepares Serving/Eventing instances on OpenShift and executes E2E tests

source "$(dirname "$0")/e2e-common.sh"

set -Eeuox pipefail

failed=0

# Build binary
(( !failed )) && build_knative_client || failed=1
# Run unit tests
 (( !failed )) && run_unit_tests || failed=1
# Serverless operator setup & tests
# TODO: change branch to "release-1.17" when available
(( !failed )) && install_serverless_operator_branch "main" || failed=1
(( !failed )) && run_client_e2e_tests serving || failed=1
# TODO: temporary workaround
(( !failed )) && install_knative_eventing_branch "release-v0.23" || failed=1
(( !failed )) && run_client_e2e_tests eventing || failed=1

(( failed )) && exit 1

success
