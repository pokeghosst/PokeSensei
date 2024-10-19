import prosodic

def analyze(text):
    txt = prosodic.Text(text)
    parsed = txt.parse()

    analyzed_stanzas = analyze_meter(parsed)
    return analyzed_stanzas

def analyze_meter(parsed):
    analyzed_stanzas = []
    for stanza in parsed.stanzas:
        stanza_positions = []
        for line in stanza.lines:
            line_meter_vals = []
            for positions in line.best_parse.positions:
                line_meter_vals.append(positions.meter_val)
            stanza_positions.append(line_meter_vals)
        analyzed_stanzas.append(stanza_positions)
    return analyzed_stanzas