#!/usr/bin/python
# -*- coding: utf-8 -*-
###
# Copyright (2016-2017) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

from ansible.compat.tests import unittest
from oneview_module_loader import IdPoolsIpv4SubnetFactsModule
from hpe_test_utils import FactsParamsTestCase

ERROR_MSG = 'Fake message error'

PARAMS_GET_ALL = dict(
    config='config.json',
    name=None
)

PARAMS_GET_BY_NAME = dict(
    config='config.json',
    name="Test IPV4 Subnet"
)

PARAMS_GET_BY_URI = dict(
    config='config.json',
    uri='/rest/ipv4-subnet/test'
)

DEFAULT_SUBNET = {
    "name": "Test IPV4 Subnet",
    "uri": '/rest/ipv4-subnet/test'
}

PRESENT_SUBNETS = [DEFAULT_SUBNET.copy()]


class IdPoolsIpv4SubnetFactsSpec(unittest.TestCase,
                                 FactsParamsTestCase):
    def setUp(self):
        self.configure_mocks(self, IdPoolsIpv4SubnetFactsModule)
        self.id_pools_ipv4_subnets = self.mock_ov_client.id_pools_ipv4_subnets
        FactsParamsTestCase.configure_client_mock(self, self.id_pools_ipv4_subnets)

    def test_should_get_all_id_pools_ipv4_subnets(self):
        self.id_pools_ipv4_subnets.get_all.return_value = PRESENT_SUBNETS
        self.mock_ansible_module.params = PARAMS_GET_ALL

        IdPoolsIpv4SubnetFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(id_pools_ipv4_subnets=PRESENT_SUBNETS)
        )

    def test_should_get_id_pools_ipv4_subnet_by_name(self):
        self.id_pools_ipv4_subnets.get_all.return_value = PRESENT_SUBNETS
        self.mock_ansible_module.params = PARAMS_GET_BY_NAME

        IdPoolsIpv4SubnetFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(id_pools_ipv4_subnets=PRESENT_SUBNETS)
        )

    def test_should_get_id_pools_ipv4_subnet_by_uri(self):
        self.id_pools_ipv4_subnets.get.return_value = DEFAULT_SUBNET
        self.mock_ansible_module.params = PARAMS_GET_BY_URI

        IdPoolsIpv4SubnetFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(id_pools_ipv4_subnets=PRESENT_SUBNETS)
        )


if __name__ == '__main__':
    unittest.main()
