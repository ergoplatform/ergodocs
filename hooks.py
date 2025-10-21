import re

_BULLET = re.compile(r"^[ \t]*([*-+]|[0-9]+\.)[ \t]+", re.M)

def fix_lists(markdown, **kwargs):
    lines = markdown.splitlines()
    out = []
    for i, line in enumerate(lines):
        insert_blank = i > 0 and _BULLET.match(line) and lines[i-1].strip() != ""
        if insert_blank and out and out[-1] != "":
            out.append("")
        out.append(line)
    return "\n".join(out)
