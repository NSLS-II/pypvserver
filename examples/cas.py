#!/usr/bin/env python2.7
'''An example of using :class:`caServer`, an EPICS channel access server
implementation based on pcaspy
'''
from __future__ import print_function
import time

import config

from pypvserver import CasPV
import epics


def test():
    loggers = ('pypvserver',
               )

    config.setup_loggers(loggers)

    session = config.session
    server = session.cas

    def updated(value=None, **kwargs):
        print('Updated to: %s' % value)

    python_pv = CasPV(config.server_pvnames[0], 123.0, server=server)

    # full_pvname includes the server prefix
    pvname = python_pv.full_pvname

    signal = epics.PV(pvname)
    signal.add_callback(updated)

    time.sleep(0.1)

    for i in range(10):
        python_pv.value = i
        time.sleep(0.05)


if __name__ == '__main__':
    test()
