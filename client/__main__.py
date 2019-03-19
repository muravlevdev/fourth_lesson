import json
import socket
import argparse


def sys_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-addr', default='localhost')
    parser.add_argument('-port', default=7777)

    return parser


def send_message(req_json):
    socket.send(req_json.encode('utf-8'))


def make_presence():
    action = input('Enter action: ')
    data = input('Data: ')

    request_json = json.dumps(
        {
            'action': action,
            'data': data
        }
    )

    return request_json


def recv_message():
    while True:
        response = socket.recv(1024)

        if response:
            print(
                unbox_recvd_message(response)
            )

            socket.close()

            break


def unbox_recvd_message(resp_data):
    dict_data = json.loads(
        resp_data.decode('utf-8')
    )
    return dict_data


if __name__ == "__main__":
    parser = sys_arg_parser()
    args = parser.parse_args()

    socket = socket.socket()
    socket.connect((args.addr, int(args.port)))
    print("Connected to ", args.addr, args.port)

    send_message(make_presence())
    recv_message()