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

from couchbase import Couchbase
from couchbase.libcouchbase import Connection

from tests.base import CouchbaseTestCase


BUCKET_NAME = 'test_bucket_for_pythonsdk'


class CouchbaseTest(CouchbaseTestCase):
    def test_is_instance_of_connection(self):
        self.assertIsInstance(
            Couchbase.connect(host=self.host,
                              port=self.port,
                              username=self.username,
                              password=self.password,
                              bucket=self.bucket_prefix),
            Connection)


if __name__ == '__main__':
    unittest.main()
