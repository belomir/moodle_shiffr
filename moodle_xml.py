#!/usr/bin/env python3

questiontype = type("questiontype", (), {i: i for i in "multichoice|truefalse|shortanswer|matching|cloze|essay|numerical|description".split("|")})

class Answer:
    pass

class Question:
    def __init__(self, name, text, type=questiontype.shortanswer, feedback='', answers=[], hints=[], grade=1, penalty=0.25, comment=''):
        self.type = type
        self.name = name
        self.text = text
        self.feedback = feedback
        self.answers = answers
        self.hints = hints
        self.grade = grade
        self.penalty = penalty
        self.comment = comment
    def xml(self):
        pass

#def question(name: str, text: str, answer: str, comment: str = "") -> str:
#    return "{comment}::{name}\n::{text}\n{{{answer}}}\n\n".format(name=name, text=text, answer=answer, comment="// "+comment+"\n" if comment != "" else "")

#debug
q1 = Question("q1", "qq1")
print(q1.type)
