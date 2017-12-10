from pythonosc import osc_message_builder
from pythonosc import udp_client

# SCSynthに接続
client = udp_client.UDPClient("127.0.0.1", 57110)

def create_msg(msg_list):
    msg = osc_message_builder.OscMessageBuilder(address= "/s_new")
    msg.add_arg(msg_list[0])
    msg.add_arg(-1)
    msg.add_arg(0)
    msg.add_arg(1)
    for m in msg_list:
        msg.add_arg(m)
    msg = msg.build()

    return msg


def send_msg(msg_list):
    msg = create_msg(msg_list)
    client.send(msg)
