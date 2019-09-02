# coding: utf-8
from __future__ import unicode_literals

import spacy
import datetime
from pathlib import Path

from neuralcoref import NeuralCoref

raw_input = Path("C:/Users/Sofie/Documents/data/neuralcoref_test/")


def now():
    return datetime.datetime.now()


if __name__ == "__main__":
    start = now()
    print(start, "START")
    nlp = spacy.load("en_core_web_lg")
    coref = NeuralCoref(nlp.vocab)
    nlp.add_pipe(coref, name='neuralcoref')

    processed = 0
    for textfile in raw_input.iterdir():
        if textfile.name.endswith(".txt"):
            article_id = textfile.name.split(".")[0]
            with textfile.open("r", encoding="utf8") as f:
                try:
                    text = f.read()
                    doc = nlp(text)
                    # print("processed", article_id)
                    processed += 1
                except Exception as e:
                    print("Problem parsing article", article_id, e)

    stop = now()
    duration = stop - start
    print(stop, "STOP")
    print(duration, " to process", processed, "articles")

