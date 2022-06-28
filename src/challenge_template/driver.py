import argparse
import logging

from pathlib import Path

import yaml

import challenge_template as ct


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STEP_OPTIONS = ["run_all", "step1"]


def _argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--key1", type=str, required=True)
    parser.add_argument("--key2", type=str, required=False)

    subparser = parser.add_subparsers(dest="step")
    for step_opt in STEP_OPTIONS:
        _ = subparser.add_parser(step_opt)

    return parser.parse_args()


def _run_driver(args):
    config = _read_config(args.config)
    step_runner = ct.StepRunner(config)

    logger.info("========= %s ===========", args.step)
    if args.step == "run_all":
        step_runner.run_all(args)
    if args.step == "step1":
        step_runner.step1(args)


def _read_config(config_filepath):
    config_path = Path(config_filepath)
    config_txt = config_path.read_text(encoding="utf-8")
    logger.info("Configuration:\n%s", config_txt)

    return yaml.load(config_txt, Loader=yaml.FullLoader)


def main():
    args = _argparser()
    _run_driver(args)


if __name__ == "__main__":
    main()
