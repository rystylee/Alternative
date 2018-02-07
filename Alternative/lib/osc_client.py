## ------------------------------------------------------------------------------

## osc_client.py
## OSCClient describe processing related to OSC.

## ------------------------------------------------------------------------------


from pythonosc import osc_message_builder
from pythonosc import udp_client


# Connect to SCSynth
client = udp_client.UDPClient("127.0.0.1", 57110)

def create_msg(msg_list):
    msg = osc_message_builder.OscMessageBuilder(address= "/s_new")
    msg.add_arg(msg_list[0])
    msg.add_arg(-1)
    msg.add_arg(0)
    msg.add_arg(1)
    for i in range(len(msg_list)):
        if not i == 0:
            msg.add_arg(msg_list[i])
    msg = msg.build()

    return msg


def send_msg(msg_list):
    msg = create_msg(msg_list)
    client.send(msg)
