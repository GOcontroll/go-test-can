#!/usr/bin/env python3

import can
import netifaces

def test_can():
    ifaces = netifaces.interfaces()
    test_pass = True

    if "can0" in ifaces and "can1" in ifaces:
        with can.Bus(interface='socketcan', channel='can0') as bus1:
            with can.Bus(interface='socketcan', channel='can1') as bus2:
                msg1 = can.Message(arbitration_id=1, data=[1])
                msg2 = can.Message(arbitration_id=2, data=[2])

                bus1.send(msg1)
                bus2.send(msg2)

                msg_recv1 = bus2.recv(timeout=1)
                msg_recv2 = bus1.recv(timeout=1)

                if msg_recv1 is None or msg_recv2 is None:
                    test_pass = False
                    print("ERR: No communication between can0 and can1")
    else:
        test_pass = False
        print("ERR: missing can interfaces can0 and/or can1")

    if "can2" in ifaces and "can3" in ifaces:
        with can.Bus(interface='socketcan', channel='can2') as bus3:
            with can.Bus(interface='socketcan', channel='can3') as bus4:        
                msg3 = can.Message(arbitration_id=3, data=[3])
                msg4 = can.Message(arbitration_id=4, data=[4])

                bus3.send(msg3)
                bus4.send(msg4)

                msg_recv3 = bus4.recv(timeout=1)
                msg_recv4 = bus3.recv(timeout=1)

                if not msg_recv3 and not msg_recv4:
                    test_pass = False
                    print("ERR: No communication between can2 and can3")
    else:
        print("NOTE: only 2 can interfaces")

    if test_pass:
        print("PASS: All can busses functioning!")
        exit(0)
    else:
        print("FAIL: Test failed")
        exit(1)
