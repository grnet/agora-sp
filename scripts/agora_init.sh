#!/bin/sh

CONFIGBASE=/etc/agora
RESOURCES=/usr/lib/agora/resources

cmd () {
    echo " "
    echo "--- $@"
    "$@"
}

cmd agora migrate
cmd agora migrate collectstatic

echo ' '
