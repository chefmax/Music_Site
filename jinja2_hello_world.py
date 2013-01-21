from jinja2 import Template

tem = """
{% if contents.__len__() == 12 %}
{{contents}}
{% else %}
<h1>false</h1>
contents len is {{contents.__len__()}}
{% endif %}
"""

t = Template(tem)
print t.render(contents = 'Hello World!')