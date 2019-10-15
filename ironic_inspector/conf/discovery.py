# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo_config import cfg

from ironic_inspector.common.i18n import _


_OPTS = [
    cfg.StrOpt('enroll_node_driver',
               default='fake-hardware',
               help=_('The name of the Ironic driver used by the enroll '
                      'hook when creating a new node in Ironic.')),
]


def register_opts(conf):
    conf.register_opts(_OPTS, 'discovery')


def list_opts():
    return _OPTS
