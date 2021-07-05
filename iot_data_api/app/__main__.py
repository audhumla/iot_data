#!/usr/bin/env python3

import connexion

from app import encoder


def main():
    app = connexion.App(__name__, specification_dir='openapi/', options={"swagger_ui": True})
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'IoT temperature'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
