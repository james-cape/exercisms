import re

def parse(markdown):
    lines = markdown.split('\n')
    accumulator = ''
    in_list = False
    in_list_append = False
    for line in lines:
        if re.match('###### (.*)', line) is not None:
            line = '<h6>' + line[7:] + '</h6>'
        elif re.match('## (.*)', line) is not None:
            line = '<h2>' + line[3:] + '</h2>'
        elif re.match('# (.*)', line) is not None:
            line = '<h1>' + line[2:] + '</h1>'
        match_object = re.match(r'\* (.*)', line)
        # breakpoint()
        if match_object:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = match_object.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                line = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = match_object.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                line = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        match_object = re.match('<h|<ul|<p|<li', line)
        if not match_object:
            line = '<p>' + line + '</p>'
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
