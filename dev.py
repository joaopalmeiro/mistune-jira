from mistune import create_markdown
from mistune.renderers import BaseRenderer


# https://github.com/lepture/mistune/blob/v2/mistune/renderers.py
# https://github.com/lepture/mistune/blob/v2/mistune/renderers.py#L103
class JiraRenderer(BaseRenderer):
    NAME = "jira"

    def text(self, text):
        return text

    def heading(self, text, level):
        # https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=headings
        tag = f"h{level}."
        return f"{tag} {text}\n"

    def finalize(self, data):
        return "".join(data)


if __name__ == "__main__":
    # https://mistune.lepture.com/en/v2/guide.html
    md_parser = create_markdown(renderer=JiraRenderer())

    with open("test.md", "r") as f:
        md_data = f.read()

    jira_data = md_parser(md_data)
    print(jira_data)
