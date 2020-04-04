#!/usr/bin/env python3

from jinja2 import Template, escape

data = '<a>Today is a sunny day</a>'

tm = Template("{{ data | e}}") # The example escapes < and > characters.
msg = tm.render(data=data)

print(msg)
print(escape(data)) #this does the same