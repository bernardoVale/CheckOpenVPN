import unittest
from check_openvpn import *
__author__ = 'bernardovale'


class TestOpenVPN(unittest.TestCase):

    def file_to_string(self, my_file):
        with open(my_file, 'r') as f:
            string = f.read()
        return string.split('\n')

    def test_validate_vpn_interface(self):
        #SUCCESS
        result_success_linux = self.file_to_string('tests/validate_vpn_interface/result_success_linux.txt')
        result_success_macos = self.file_to_string('tests/validate_vpn_interface/result_success_macos.txt')
        self.assertTrue(validate_vpn_interface(result_success_linux))
        self.assertTrue(validate_vpn_interface(result_success_macos))
        #FAILURES
        result_failure_linux = self.file_to_string('tests/validate_vpn_interface/result_failure_linux.txt')
        result_failure_macos = self.file_to_string('tests/validate_vpn_interface/result_failure_macos.txt')
        result_failure_solaris = self.file_to_string('tests/validate_vpn_interface/result_failure_solaris.txt')
        result_failure_aix = self.file_to_string('tests/validate_vpn_interface/result_failure_aix.txt')
        self.assertFalse(validate_vpn_interface(result_failure_linux))
        self.assertFalse(validate_vpn_interface(result_failure_macos))
        self.assertFalse(validate_vpn_interface(result_failure_solaris))
        self.assertFalse(validate_vpn_interface(result_failure_aix))

    def testvalidate_openvpn_pid(self):
        result_success_linux = self.file_to_string('tests/validate_openvpn_pid/result_success_linux.txt')
        result_success_macos = self.file_to_string('tests/validate_openvpn_pid/result_success_macos.txt')
        self.assertTrue(validate_openvpn_pid(result_success_linux))
        self.assertTrue(validate_openvpn_pid(result_success_macos))
        #FAILURES
        result_failure_linux = self.file_to_string('tests/validate_openvpn_pid/result_failure_linux.txt')
        result_failure_macos = self.file_to_string('tests/validate_openvpn_pid/result_failure_macos.txt')
        result_failure_solaris = self.file_to_string('tests/validate_openvpn_pid/result_failure_solaris.txt')
        result_failure_aix = self.file_to_string('tests/validate_openvpn_pid/result_failure_aix.txt')
        self.assertFalse(validate_openvpn_pid(result_failure_linux))
        self.assertFalse(validate_openvpn_pid(result_failure_macos))
        self.assertFalse(validate_openvpn_pid(result_failure_solaris))
        self.assertFalse(validate_openvpn_pid(result_failure_aix))

    def test_validate_ping(self):
        result_failure_linux = "PING 10.200.0.114 (10.200.0.114) 56(84) bytes of data. \
From 10.0.0.90 icmp_seq=1 Destination Host Unreachable \
\
--- 10.200.0.114 ping statistics --- \
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 3005ms"
        result_failure_aix = "PING 10.200.0.110: (10.200.0.110): 56 data bytes \
\
--- 10.200.0.110 ping statistics --- \
1 packets transmitted, 0 packets received, 100% packet loss"
        result_failure_solaris = "no answer from 10.8.0.2"
        self.assertFalse(validate_ping(result_failure_aix))
        self.assertFalse(validate_ping(result_failure_linux))
        self.assertFalse(validate_ping(result_failure_solaris))
        result_success_solaris = "10.8.0.1 is alive"
        result_success_aix = "PING 192.168.210.9: (192.168.210.9): 56 data bytes \
64 bytes from 192.168.210.9: icmp_seq=0 ttl=255 time=0 ms \
\
--- 192.168.210.9 ping statistics --- \
1 packets transmitted, 1 packets received, 0% packet loss \
round-trip min/avg/max = 0/0/0 ms"
        result_success_linux = "PING 10.8.0.1 (10.8.0.1) 56(84) bytes of data. \
64 bytes from 10.8.0.1: icmp_seq=1 ttl=64 time=21.3 ms \
\
--- 10.8.0.1 ping statistics --- \
1 packets transmitted, 1 received, 0% packet loss, time 21ms \
rtt min/avg/max/mdev = 21.346/21.346/21.346/0.000 ms"
        self.assertTrue(validate_ping(result_success_aix))
        self.assertTrue(validate_ping(result_success_solaris))
        self.assertTrue(validate_ping(result_success_linux))