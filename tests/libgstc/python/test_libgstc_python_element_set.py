#!/usr/bin/env python3
import unittest
import gstc

class TestGstcElementSetMethods(unittest.TestCase):

    def test_element_set_property_value(self):
        pipeline = "videotestsrc name=v0 pattern=ball ! fakesink"
        self.gstd_client = gstc.client(loglevel='DEBUG')
        self.gstd_client.pipeline_create ("p0", pipeline)
        self.assertEqual(self.gstd_client.element_get ("p0", "v0", "pattern"), "Moving ball")
        self.gstd_client.element_set ("p0", "v0", "pattern", "bar")
        self.assertEqual(self.gstd_client.element_get ("p0", "v0", "pattern"), "Bar")
        self.gstd_client.pipeline_delete ("p0")

if __name__ == '__main__':
    unittest.main()