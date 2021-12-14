#!/usr/bin/env bash

knEventVersion="$(grep 'knative.dev/kn-plugin-event ' "$(basedir)/go.mod" \
  | head -n 1 \
  | sed -s 's/.* \(v.[\.0-9]*\).*/\1/')"
readonly default_sender_image='registry.ci.openshift.org/knative/release-0.26:client-plugin-event-sender'
readonly sender_image="${KN_PLUGIN_EVENT_SENDER_IMAGE:-${default_sender_image}}"
export EXTERNAL_LD_FLAGS="${EXTERNAL_LD_FLAGS:-} \
-X knative.dev/kn-plugin-event/pkg/metadata.Image=${sender_image} \
-X knative.dev/kn-plugin-event/pkg/metadata.Version=${knEventVersion}"
