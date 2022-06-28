from dataclasses import dataclass
from typing import Dict

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class StepRunner:
    config: Dict

    def run_all(self, args):
        self.step1(args)

    def step1(self, args):
        logger.info("Running step1.")
        logger.info("Configuration:\n%s", self.config["step1"])
        for key, val in vars(args).items():
            logger.info("%s: %s", key, val)
