#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create snippets based on a template.

For example, once you create a snippet that will filter adversaries, you can easily create copies of that snippet for all of the other group types. This script is code, to write code (snippets), to write code (scripts that talk to ThreatConnect's API via the Python SDK).
"""

# define the starting template we will use to create the other snippets
snippet_template = """<snippet>
    <content><![CDATA[
tcex.log.debug('${1:message}')
]]></content>
    <tabTrigger>tcedebug</tabTrigger>
    <scope>source.python</scope>
    <description>TcEx Debug Logging</description>
</snippet>"""

"""Names of the items to be replaced from the template snippet.
PLURAL NAME MUST COME FIRST!!! This prevents any the first part of the plural instances of the name (the part before the 's') being replaced as if they were singular."""
object_names = ["debug"]

# replace any brackets with other characters (this will be undone later)
snippet_template = snippet_template.replace("{", "!?!").replace("}", "?!?")

"""Singular names of the objects that will replace any of the object_names found in the snippet template."""
replacements = ["critical", "error", "warning", "info"]

# iterate through all of the replacements and replace them appropriately
for replacement in replacements:
    new_snippet = snippet_template

    # find and replace each object name with the appropriate replacement
    for name in object_names:
        # if the object name is plural, use a plural form of the replacement
        if name.endswith("s"):
            current_replacement = replacement + "s"
        # if the object name is plural, keep the singular replacement
        else:
            current_replacement = replacement

        # replace the object name
        new_snippet = new_snippet.replace(name, "{0}")
        # replace the capitalized object name
        new_snippet = new_snippet.replace(name.title(), "{0}")

        # replace the object name with the new replacement
        new_snippet = new_snippet.format(current_replacement)

    # add the original brackets back into the snippet
    new_snippet = new_snippet.replace("?!?", "}").replace("!?!", "{")

    # write the new snippet to the appropriate file
    with open("../snippets/" + "tce" + replacement + ".sublime-snippet",
              "w+") as f:
        f.write(new_snippet)
