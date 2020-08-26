class Parantheses:
    def __init__(self):
        pass

    def generateParanthesis(self, n):
        results = []
        differential = 0  # closings - openings
        opening_parens = n
        closing_parens = n
        
        combo = ''

        def add_opening(results, differential, opening_parens, closing_parens, combo):
            if opening_parens > 0 and differential >= 0:
                combo += '('
                opening_parens -= 1
                differential += 1
                if len(combo) < n*2:
                    add_opening(results, differential, opening_parens, closing_parens, combo)
                    add_closing(results, differential, opening_parens, closing_parens, combo)
                else:
                    results.append(combo)



        def add_closing(results, differential, opening_parens, closing_parens, combo):
            if closing_parens > 0 and differential >= 0:
                combo += ')'
                closing_parens -= 1
                differential -= 1
                if len(combo) < n*2:
                    add_opening(results, differential, opening_parens, closing_parens, combo)
                    add_closing(results, differential, opening_parens, closing_parens, combo)
                else:
                    results.append(combo)


        add_opening(results, differential, opening_parens, closing_parens, combo)
        add_closing(results, differential, opening_parens, closing_parens, combo)

        return results
