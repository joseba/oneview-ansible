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
from oneview_module_loader import UserFactsModule
from hpe_test_utils import FactsParamsTestCase

ERROR_MSG = 'Fake message error'

PARAMS_GET_ALL = dict(
    config='config.json',
    name=None
)

PARAMS_GET_BY_NAME = dict(
    config='config.json',
    name="Test User"
)

PRESENT_USERS = [{
    "name": "Test User",
    "uri": "/rest/user/c6bf9af9-48e7-4236-b08a-77684dc258a5"
}]


class UserFactsSpec(unittest.TestCase, FactsParamsTestCase):
    def setUp(self):
        self.configure_mocks(self, UserFactsModule)
        self.users = self.mock_ov_client.users
        FactsParamsTestCase.configure_client_mock(self, self.users)

    def test_should_get_all_users(self):
        self.users.get_all.return_value = PRESENT_USERS
        self.mock_ansible_module.params = PARAMS_GET_ALL

        UserFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(users=PRESENT_USERS)
        )

    def test_should_get_user_by_name(self):
        self.users.get_by.return_value = PRESENT_USERS
        self.mock_ansible_module.params = PARAMS_GET_BY_NAME

        UserFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(users=PRESENT_USERS)
        )


if __name__ == '__main__':
    unittest.main()
