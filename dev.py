from pprint import pprint

from mistune import create_markdown
from mistune.renderers import BaseRenderer


# https://github.com/lepture/mistune/blob/v2/mistune/renderers.py
# https://github.com/lepture/mistune/blob/v2/mistune/renderers.py#L103
# https://mistune.lepture.com/en/v2/advanced.html
class JiraRenderer(BaseRenderer):
    NAME = "jira"

    def text(self, text):
        return text

    def heading(self, text, level):
        # https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=headings
        tag = f"h{level}."
        return f"{tag} {text}\n"

    def paragraph(self, text):
        return f"{text}\n"

    def strong(self, text):
        return f"*{text}*"

    def emphasis(self, text):
        return f"_{text}_"

    def finalize(self, data):
        return "".join(data)


if __name__ == "__main__":
    # https://mistune.lepture.com/en/v2/guide.html
    md_parser = create_markdown(renderer=JiraRenderer(), plugins=["strikethrough"])

    with open("test.md", "r") as f:
        md_data = f.read()

    md_ast_parser = create_markdown(renderer="ast", plugins=["strikethrough"])
    pprint(md_ast_parser(md_data))

    jira_data = md_parser(md_data)
    # print(jira_data)

    with open("test.jira", "w") as f:
        f.write(jira_data)
