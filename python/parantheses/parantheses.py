class Parantheses:
    def generateParanthesis(self, n):
        results = []
        differential = 0  # closings - openings
        opening_parens = n
        closing_parens = n
        combo = ''

        def add_char(results, differential, opening_parens, closing_parens, combo, char):
            if differential >=0:
                if char == '(' and opening_parens > 0:
                    combo += char
                    opening_parens -= 1
                    differential += 1
                    if len(combo) < n*2:
                        add_char(results, differential, opening_parens, closing_parens, combo, '(')
                        add_char(results, differential, opening_parens, closing_parens, combo, ')')
                    else:
                        results.append(combo)
                elif char == ')' and closing_parens > 0:
                    combo += char
                    closing_parens -= 1
                    differential -= 1
                    if len(combo) < n*2:
                        add_char(results, differential, opening_parens, closing_parens, combo, '(')
                        add_char(results, differential, opening_parens, closing_parens, combo, ')')
                    else:
                        results.append(combo)

        add_char(results, differential, opening_parens, closing_parens, combo, '(')
        add_char(results, differential, opening_parens, closing_parens, combo, ')')

        return results
