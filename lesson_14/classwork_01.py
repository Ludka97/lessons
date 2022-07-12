from flask import Flask, request
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)


def dfl(data: dict) -> str:
    t = []
    for key, value in data.items():
        t.append(f"{key}:{value}")
    return ", ".join(t)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        logger.info(dfl(request.form.to_dict()))
        request.form.to_dict().items()
        return

    logger.info(dfl(request.args.to_dict()))
    return request.args.to_dict()


@app.route("/test/", methods=["GET"])
def test():
    return "Test URL"

if __name__ == "__main__":
    app.run()
