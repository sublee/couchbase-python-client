#
# Copyright 2013, Couchbase, Inc.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from tests.base import ConnectionTestCase
from couchbase.libcouchbase import Connection, FMT_JSON
from couchbase import Couchbase

class ConnectionMiscTest(ConnectionTestCase):

    def test_server_nodes(self):
        nodes = self.cb.server_nodes
        self.assertIsInstance(nodes, (list, tuple))
        self.assertTrue(len(nodes) > 0)
        for n in nodes:
            self.assertIsInstance(n, str)

        def _set_nodes():
            self.cb.server_nodes = 'sdf'
        self.assertRaises(AttributeError, _set_nodes)

    def test_lcb_version(self):
        verstr, vernum = Connection.lcb_version()
        self.assertIsInstance(verstr, str)
        self.assertIsInstance(vernum, int)

    def test_bucket(self):
        bucket_str = self.cb.bucket
        self.assertEqual(bucket_str, self.make_connargs()['bucket'])

    def test_conn_repr(self):
        repr(self.cb)


    def test_connection_defaults(self):
        ctor_params = self.make_connargs()
        # XXX: Change these if any of the defaults change
        defaults = {
            'timeout' : 2.5,
            'quiet' : False,
            'default_format' : FMT_JSON,
            'unlock_gil' : True,
            'transcoder' : None
        }

        cb_ctor = Connection(**ctor_params)
        cb_connect = Couchbase.connect(**ctor_params)

        for option, value in defaults.items():
            actual = getattr(cb_ctor, option)
            self.assertEqual(actual, value)

            actual = getattr(cb_connect, option)
            self.assertEqual(actual, value)
