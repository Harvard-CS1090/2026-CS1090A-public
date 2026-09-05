"""Helpers for CS1090A Section 1.

Only one thing lives here: a stand-in for a `requests` Response, built from a response we
captured earlier and committed to data/responses/.

Why a recording instead of a live request. Two of the responses this section looks at come
from a site that treats browsers and scripts differently, so a live call would print
something different for every student, and something different again next year. A
recording with a date on it is honest and identical for everyone -- which is the same
discipline the section spends an hour teaching.

It is a class rather than three lines in the notebook because a first-week student should
not have to read a class definition to get to `requests`.
"""
import json

import requests

DATA = "data"


class Recorded:
    """A saved HTTP response. Behaves like the `requests.Response` it came from."""

    def __init__(self, name, data_dir=DATA):
        with open(f"{data_dir}/responses/{name}.json", encoding="utf-8") as f:
            r = json.load(f)
        self.status_code = r["status_code"]
        self.captured = r["captured"]
        self.url = r["url"]
        self.request_user_agent = r["request_user_agent"]
        self.headers = r["headers"]
        # Big bodies are stored whole, next to the notebook, rather than inline.
        if r.get("body_file"):
            with open(f"{data_dir}/{r['body_file']}", encoding="utf-8") as f:
                self.text = f.read()
        else:
            self.text = r["body_first_400"]

    def json(self):
        """Same contract as requests: parse the body as JSON."""
        return json.loads(self.text)

    def raise_for_status(self):
        """Same contract as requests: quiet on 2xx, raises on 4xx/5xx."""
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} Client Error for {self.url}")

    def __repr__(self):
        return f"<Recorded [{self.status_code}] captured {self.captured}>"
