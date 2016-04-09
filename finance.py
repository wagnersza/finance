#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import argparse

def args():
    pass

# def install_itau_bot():
#     os.system('rvm gemset use ruby-2.2.1@finance --create')
#     os.system('gem install bundler')
#     os.system('cd itau_bot; bundle install')

# def run_itau_bot():
#     os.system('cd itau_bot; bundle exec rake itau_bot:run')
def read_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

def json_to_database(json_file):
    data = read_json(json_file)
    balance = data['balance']
    for transaction in balance:
        print transaction

def main():
    json_to_database('itau_bot/return.json')
    # if arg.sync:
    #     run_itau_bot()

    # if arg.install_bot:
    #     install_itau_bot()

    # Jogar dados no banco
    # - rodar o itau_bot
    # - colocar os dados do json no banco
    # - nao sobrescrever nada, ser idenpotente

if __name__ == "__main__":
    main()
