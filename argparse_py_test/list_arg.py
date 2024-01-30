""" リスト形式の引数の取得
"""
from argparse import ArgumentParser
import pprint

parser = ArgumentParser()

parser.add_argument("--foo", nargs=2, type=float, default=[1.0, 2.0])

cli_kwargs = vars(parser.parse_args())

pprint.pprint(cli_kwargs)

