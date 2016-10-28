# Copyright 2016 Hewlett Packard Enterprise
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg

from ironic.common.i18n import _

opts = [
    #cfg.IntOpt('client_timeout',
               #default=60,
               #help=_('Timeout (in seconds) for Redfish operations')),
    #cfg.PortOpt('client_port',
                #default=443,
                #help=_('Port to be used for Redfish operations')),
    #cfg.BoolOpt('use_web_server_for_images',
                #default=False,
                #help=_('Set this to True to use http web server to host '
                       #'floppy images and generated boot ISO. This '
                       #'requires http_root and http_url to be configured '
                       #'in the [deploy] section of the config file. If this '
                       #'is set to False, then Ironic will use Swift '
                       #'to host the floppy images and generated '
                       #'boot_iso.')),
    #cfg.IntOpt('power_retry',
               #default=6,
               #help=_('Number of times a power operation needs to be '
                      #'retried')),
    #cfg.IntOpt('power_wait',
               #default=2,
               #help=_('Amount of time in seconds to wait in between power '
                      #'operations')),
    #cfg.StrOpt('default_boot_mode',
               #default='auto',
               #choices=['auto', 'bios', 'uefi'],
               #help=_('Default boot mode to be used in provisioning when '
                      #'"boot_mode" capability is not provided in the '
                      #'"properties/capabilities" of the node. The default is '
                      #'"auto" for backward compatibility. When "auto" is '
                      #'specified, default boot mode will be selected based '
                      #'on boot mode settings on the system.')),
]


def register_opts(conf):
    conf.register_opts(opts, group='redfish')
