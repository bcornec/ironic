#!/bin/bash

perl -pi -e 's/ironic-api/ironic-conductor/g' /etc/init.d/ironic-conductor

/etc/init.d/rabbitmq-server start
/etc/init.d/ironic-api start
/etc/init.d/ironic-conductor start

ps -ef | egrep "rabbitmq-server|ironic"

/bin/bash
