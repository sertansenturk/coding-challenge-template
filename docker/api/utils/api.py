import logging
import os

from flask import Flask, request

from challenge_template.api_request_parser import APIRequestParser

api = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@api.route("/template", methods=["POST"])
def template_post():
    """Returns whatever was posted back as a UTF-8 string"""
    logger.info("Received %s request", request.method)
    if request.method == "POST":
        return APIRequestParser.parse_post_request(request)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    api.run(host="0.0.0.0", port=port, debug=True)
