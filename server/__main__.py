import json
import socket
import argparse
from routes import get_server_routes


def sys_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-addr', default='')
    parser.add_argument('-port', default=7777)

    return parser


def recv_message():
    while True:
        client, address = sock.accept()
        print(f'Client detected {address}')
        data = client.recv(1024)
        request = json.loads(
            data.decode('utf-8')
        )

        send_answer(client, make_answer(request))


def make_answer(user_request):
    client_action = user_request.get('action')
    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action, get_server_routes()
        )
    )

    route = resolved_routes[0] if resolved_routes else None

    if route:
        controller = route.get('controller')
        status_code = 200
        response_string = controller(user_request.get('data'))

    else:
        status_code = 400
        response_string = 'Action not supported'

    request_json = json.dumps(
        {
            'response': status_code,
            'message': response_string
        }
    )

    return request_json


def send_answer(clt, req_json):
    clt.send(req_json.encode('utf-8'))
    clt.close()


if __name__ == "__main__":
    parser = sys_arg_parser()
    args = parser.parse_args()

    sock = socket.socket()
    sock.bind((args.addr, int(args.port)))
    sock.listen(5)
    recv_message()
