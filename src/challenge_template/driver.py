import argparse
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ARG_OPTIONS = ["arg1"]


def _argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key1", type=str, required=True)
    parser.add_argument("--key2", type=str, required=True)
    parser.add_argument("--key3", type=str, required=False)

    subparser = parser.add_subparsers(dest="arg")
    for arg_opt in ARG_OPTIONS:
        _ = subparser.add_parser(arg_opt)

    return parser.parse_args()


def _run_driver(args):
    for key, val in vars(args).items():
        logger.info("%s: %s", key, val)


def main():
    args = _argparser()
    _run_driver(args)


if __name__ == "__main__":
    main()
