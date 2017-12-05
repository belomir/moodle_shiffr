#!/usr/bin/env python3

def question(name: str, text: str, answer: str, comment: str = "") -> str:
    return "{comment}::{name}::\n{text}\n{{answer}}\n\n".format(name=name, text=text, answer=answer, comment="// "+comment+"\n" if comment != "" else "")
