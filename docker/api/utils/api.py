import logging
import os

from flask import Flask, request
from challenge_template import __version__

api = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@api.route("/dummy", methods=["POST"])
def dummy_post():
    """Returns whatever was posted back as a UTF-8 string"""
    logger.info("App ver %s: Received %s request", __version__, request.method)
    if request.method == "POST":
        data = request.get_data().decode("utf-8")
        dummy_str = (
            f"[App ver {__version__}] Received {request.method} request: '{data}'"
        )
        return dummy_str


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    api.run(host="0.0.0.0", port=port, debug=True)
