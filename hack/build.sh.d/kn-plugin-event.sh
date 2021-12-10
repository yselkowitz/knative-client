#!/usr/bin/env bash

knEventVersion="$(grep 'knative.dev/kn-plugin-event ' "$(basedir)/go.mod" \
  | head -n 1 \
  | sed -s 's/.* \(v.[\.0-9]*\).*/\1/')"
readonly upstream_sender_image='gcr.io/knative-releases/kn-event-sender@sha256:8d562077864d6490438ac5b35dd352c6ffa6cd089e81fa06aaf6fe56a0374196'
readonly sender_image="${KN_PLUGIN_EVENT_SENDER_IMAGE:-${upstream_sender_image}}"
export EXTERNAL_LD_FLAGS="${EXTERNAL_LD_FLAGS:-} \
-X knative.dev/kn-plugin-event/pkg/metadata.Image=${sender_image} \
-X knative.dev/kn-plugin-event/pkg/metadata.Version=${knEventVersion}"