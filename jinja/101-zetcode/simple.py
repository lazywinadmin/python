#!/usr/bin/env python3
#example from http://zetcode.com/python/jinja/
from jinja2 import Template

name = input("Enter your name: ")

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)