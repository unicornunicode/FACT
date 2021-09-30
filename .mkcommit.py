from mkcommit import Keyword, CommitMessage
from mkcommit.validators import matches
from mkcommit.model import ask, ValidationFailedException

type_keywords = [
    Keyword("feat", "A new feature"),
    Keyword("fix", "A bug fix"),
    Keyword("docs", "Documentation only changes"),
    Keyword("style", "Changes that do not affect the meaning of the code"),
    Keyword("refactor", "A code change that neither fixes a bug nor adds a feature"),
    Keyword("test", "Adding missing tests or correcting existing tests"),
    Keyword("ci", "Changes to our CI configuration files and scripts"),
    Keyword("chore", "Other changes that don't modify src or test files"),
    Keyword("wip", "Work-in-progress"),
]


def is_conventional(s: str) -> bool:
    types = "(" + "|".join([k.keyword for k in type_keywords]) + ")"
    scope = r"(\(.+\))?"
    breaking = r"!?"
    subject = r".+"

    expression = f"{types}{scope}{breaking}: {subject}"
    if not matches(expression)(s):
        raise ValidationFailedException(
            "The message is not a valid Conventional Commit"
        )
    return True


def is_word(s: str) -> bool:
    if not matches(r"\S+"):
        raise ValidationFailedException(
                "The scope should be a single word"
        )
    return True


def is_sentence(s: str) -> bool:
    if " " not in s or len(s) < 3:
        raise ValidationFailedException("The message should at least contain two words")
    return True


def ask_type() -> str:
    return ask(
        "Select the type of change that you're committing", one_of=type_keywords
    )


def ask_scope() -> str:
    return ask("What is the scope of this change (Optional)", check=is_word)


def ask_subject() -> str:
    return ask(
        "Write a short, imperative tense description of the change",
        check=is_sentence,
    )


def ask_body() -> str:
    return ask(
        "Provide a longer description of the change (Optional)",
    )


# NOTE: Breaking change not implemented


def message_simple() -> str:
    type = ask_type().keyword
    scope = ask_scope()
    subject = ask_subject()
    if scope:
        return f"{type}({scope}): {subject}"
    else:
        return f"{type}: {subject}"


def commit():
    first_line, body = message_simple(), ask_body()
    is_conventional(first_line)
    return CommitMessage(first_line, body)


def on_commit(msg: CommitMessage):
    is_conventional(msg.first_line)


# vim: set et ts=4 sw=4:
