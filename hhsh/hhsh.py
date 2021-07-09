import json
import argparse
import re

import requests
from rich.table import Table
from rich.console import Console


HHSH_GUESS_URL = "https://lab.magiconch.com/api/nbnhhsh/guess"


def make_payload_text(text):
    text_list = re.findall("([a-zA-z0-9]{2,})+", text, flags=re.DOTALL)
    return text_list


def guess_fucking_words(text):
    r = requests.post(
        HHSH_GUESS_URL,
        headers={"content-type": "application/json"},
        data=json.dumps({"text": text}),
    )
    if not r.ok:
        raise Exception("Can not connect hhsh guess api")
    return r.json()


def print_rich_table(text_list):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Fucking Words")
    table.add_column("HHSH")
    for t in text_list:
        if not t.get("trans"):
            continue
        name = t["name"]
        for i in t["trans"][:-1]:
            table.add_row(name, i)
        table.add_row(name, t["trans"][-1], style="underline2")
    if table.rows:
        table.rows[-1].style = None
    console.print(table)


def main():
    parser = argparse.ArgumentParser()
    # add more args for the future here
    parser.add_argument("text", help="your hhsh words")
    options = parser.parse_args()
    text_list = make_payload_text(options.text)
    if not text_list:
        raise Exception("No hhsh words")
    words_list = guess_fucking_words(",".join(text_list))
    print_rich_table(words_list)
