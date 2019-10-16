import re

def parse(markdown):
    lines = markdown.split('\n')
    accumulator = ''
    in_list = False
    in_list_append = False
    for line in lines:
        if re.match('###### (.*)', line):
            line = '<h6>' + line[7:] + '</h6>'
        elif re.match('## (.*)', line):
            line = '<h2>' + line[3:] + '</h2>'
        elif re.match('# (.*)', line):
            line = '<h1>' + line[2:] + '</h1>'
        match_object = re.match(r'\* (.*)', line)
        if match_object:
            is_bold = False
            is_italic = False
            content = match_object.group(1)
            line = '<li>' + content + '</li>'
            if not in_list:
                in_list = True
                line = '<ul>' + line
                if re.match('(.*)__(.*)__(.*)', content): is_bold = True
                if re.match('(.*)_(.*)_(.*)', content): is_italic = True
        else:
            if in_list:
                in_list_append = True
                in_list = False
        if not re.match('<h|<ul|<p|<li', line): line = '<p>' + line + '</p>'
        match_object = re.match('(.*)__(.*)__(.*)', line)
        if match_object:
            line = match_object.group(1) + '<strong>' + match_object.group(2) + '</strong>' + match_object.group(3)
        match_object = re.match('(.*)_(.*)_(.*)', line)
        if match_object:
            line = match_object.group(1) + '<em>' + match_object.group(2) + '</em>' + match_object.group(3)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        accumulator += line
    if in_list:
        accumulator += '</ul>'
    return accumulator
