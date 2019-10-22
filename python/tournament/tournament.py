def tally(rows):
    accumulator = {}
    for row in rows:
        outcome = row.split(';')[2]
        if outcome != 'draw':
            if outcome == 'win':
                winner = row.split(';')[0]
                loser = row.split(';')[1]
            else:
                loser = row.split(';')[0]
                winner = row.split(';')[1]
            if winner in accumulator:
                accumulator[winner]['MP'] += 1
                accumulator[winner]['W'] += 1
                accumulator[winner]['P'] += 3
            else:
                accumulator[winner] = { 'MP': 1,'W': 1,'D': 0,'L': 0,'P': 3 }
            if loser in accumulator:
                accumulator[loser]['MP'] += 1
                accumulator[loser]['L'] += 1
            else:
                accumulator[loser] = { 'MP': 1,'W': 0,'D': 0,'L': 1,'P': 0 }
        else:
            for team in [row.split(';')[0], row.split(';')[1]]:
                if team in accumulator:
                    accumulator[team]['MP'] += 1
                    accumulator[team]['D'] += 1
                    accumulator[team]['P'] += 1
                else:
                    accumulator[team] = { 'MP': 1,'W': 0,'D': 1,'L': 0,'P': 1 }
    lines = []
    for team in accumulator:
        line = f"{team.ljust(30, ' ')}"
        for stat in accumulator[team]:
            line += " |  {}".format(accumulator[team][stat])
        lines.append(line)
    lines.sort(key = lambda lines: (-int(lines[-1]), lines[0]))
    last_line = '{}| MP |  W |  D |  L |  P'.format('Team'.ljust(31, ' '))
    lines.insert(0, last_line)
    return lines
