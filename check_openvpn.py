#!/usr/bin/python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------
#            Script de Verificação - OpenVPN
#
#       Autor: Bernardo S E Vale
#       Data Inicio:  11/11/2014
#       Data Release: 11/11/2014
#       email: bernardo.vale@lb2.com.br
#       Versão: v1.0
#       LB2 Consultoria - Leading Business 2 the Next Level!
#-------------------------------------------------------------
import subprocess

__author__ = 'bernardovale'


def restart_openvpn():
    """
    Reinicia o servico do OpenVPN
    :return:
    """
    cmd = 'service openvpn restart'
    result = call_command(cmd)


def call_command(command):
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()


def validate_openvpn_pid(result):
    """
    Valida o resultado do check_openvpn_pid
    :param result:
    :return:
    """
    for ps in result:
        if 'openvpn --daemon' in ps:
            print 'OpenVPN Process - OK'
            return True
    print 'OpenVPN Process - DOWN'
    return False


def check_openvpn_pid():
    """
    Verifica se o processo de client do openvpn esta ativo
    :return:
    """
    return call_command('ps aux')[0].split('\n')


def validate_vpn_interface(result):
    """
    Valida o resultado do check_vpn_interface
    :param result:
    :return:
    """
    for iface in result:
        if 'tun0' in iface:
            print 'Interface tun0 - OK'
            return True
    print 'Interface tun0 - DOWN'
    return False


def check_vpn_interface():
    """
    Verifica via netstat se a interface esta ativa
    :return:
    """
    return validate_vpn_interface(call_command('netstat -i')[0].split('\n'))


def validate_ping(result):
    """
    Valida o resultado do check_ping
    :param result: resultado
    :return: bool
    """
    if '0 packets received' in str(result) or 'no answer from' in str(result) or '0 received' in str(result):
        print 'Conectividade - DOWN'
        return False
    print 'Conectividade - OK'
    return True


def check_ping(ip):
    """
    Verifica se é possível realizar um comando de ping

    :return: bool
    """
    return validate_ping(call_command('ping -c1 ' + ip))


def main():
    check_ping('10.200.0.114')
    check_openvpn_pid()
    check_vpn_interface()

if __name__ == '__main__':
    main()
