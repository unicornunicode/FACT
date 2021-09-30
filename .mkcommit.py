from mkcommit import Keyword, CommitMessage, to_stdout
from mkcommit.model import CommaSeparatedList, ask
from mkcommit.suites import semantic

commit_keywords = [
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


def ask_short_commit_msg() -> str:
    return ask("Provide the short commit msg: ")


def default_short() -> str:
    keywords = CommaSeparatedList(*[k.keyword for k in semantic.ask_keywords()])
    scope = semantic.ask_scope()
    short_commit = ask_short_commit_msg()
    breaking = ""
    if scope:
        return f"{keywords}({scope}){breaking}: {short_commit}"
    else:
        return f"{keywords}{breaking}: {short_commit}"


def commit():
    return CommitMessage(default_short())


def on_commit(msg: CommitMessage):
    semantic.is_semantic(msg.first_line)


if __name__ == "__main__":
    to_stdout(commit())


# vim: set et ts=4 sw=4:
