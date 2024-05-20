#!/usr/bin/env bash

cat > /etc/gitlab-runner/config.toml <<- EOM
concurrent = 1
check_interval = 60

[session_server]
  session_timeout = 1800

[[runners]]
  name = "${GLR_NAME}"
  url = "https://dev.tests.ru/"
  token = "${GLR_TOKEN}"
  executor = "shell"
  builds_dir = "/tests/tests"
  [runners.custom_build_dir]
    enabled = true
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]

EOM




graceful() {
  echo "Graceful shutdown signal..."
  kill -3 "$child"
}

trap graceful SIGQUIT

bash /tests/tests/docker/script/run-ssh7.sh ${DOCKER_ARGS} --config[btp.server_name]=docker-dev-$(uname -n) &
gitlab-runner run &

child=$!
wait "$child"