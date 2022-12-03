from pprint import pprint

from mistune import create_markdown
from mistune.plugins.extra import plugin_strikethrough
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

    def link(self, link, text, title=None):
        # https://github.com/lepture/mistune/blob/v2/mistune/renderers.py#L137
        return f"[{text}|{link}]"

    def finalize(self, data):
        return "".join(data)


def render_jira_strikethrough(text):
    return f"-{text}-"


def plugin_strikethrough_patch(md):
    plugin_strikethrough(md)

    if md.renderer.NAME == "jira":
        md.renderer.register("strikethrough", render_jira_strikethrough)


if __name__ == "__main__":
    # https://mistune.lepture.com/en/v2/guide.html
    # https://github.com/lepture/mistune/blob/v2/mistune/plugins/extra.py
    md_parser = create_markdown(
        renderer=JiraRenderer(), plugins=[plugin_strikethrough_patch]
    )

    with open("test.md", "r") as f:
        md_data = f.read()

    md_ast_parser = create_markdown(renderer="ast", plugins=["strikethrough"])
    pprint(md_ast_parser(md_data))

    jira_data = md_parser(md_data)
    # print(jira_data)

    with open("test.jira", "w") as f:
        f.write(jira_data)
