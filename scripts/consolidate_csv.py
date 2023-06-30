import csv
import glob
#the path of the csv files to combine
path = r'./projects' 
all_files = glob.glob(path + "/*.csv")

html_table = '<table>\n'
html_table += '<thead>\n'
html_table += '<tr class="main-header"><th>Project</th><th colspan="6">Availability</th><th colspan="6">Documentation</th><th colspan="2">Access</th></tr>\n'
html_table += '<tr class="second-header"><th>(maker, bases, URL)</th><th>Open code</th><th>LLM data</th><th>LLM weights</th><th>RLHF data</th><th>RLHF weights</th><th>License</th><th>Code</th><th>Architecture</th><th>Preprint</th><th>Paper</th><th>Modelcard</th><th>Datasheet</th><th>Package</th><th>API</th></tr>\n'
html_table += '</thead>\n'
html_table += '<tbody>\n'

# Read the input CSV file and transpose the rows and columns
for i, fname in enumerate(all_files):

    with open(fname, 'r') as file:
        file.readline()
        reader = csv.reader(file)
        rows = list(reader)
        transposed = list(zip(*rows))

    # add data by looping through each line and adding 2 rows to the html table for every row of the csv.
    # also add classes to the <td> elements for colour coding and links to source of the class judgement: https://github.com/liesenf/awesome-open-chatgpt/issues/12
    # get column indices
    ci = {name: index for index, name in enumerate(transposed[0])}
    cells = ["opencode", "llmdata", "llmweights", "rldata", "rlweights", "license","code","architecture","preprint","paper","modelcard","datasheet","package","api"]
    #attributes = ["_class", "_link", "_notes"]
    for row in transposed[1:]:
        # first row
        r1_html = '<tr class="row-a"><td class="name-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(row[ci["project_link"]], row[ci["project_notes"]], row[ci["project_name"]])
        for c in cells:
            cl = row[ci[c + "_class"]]
            link = row[ci[c + "_link"]]
            notes = row[ci[c + "_notes"]]
            symbol = "&#10004;&#xFE0E" if cl == "open" else "~" if cl == "partial" else "&#10008;" if cl == "closed" else ""
            r1_html += '<td class="{} data-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)
        r1_html += "</tr>\n"
        html_table += r1_html
        # second row
        r2_html = '<tr class="row-b"><td class="org"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(row[ci["org_link"]], row[ci["org_name"]], row[ci["org_name"]])
        r2_html += '<td colspan="3" class="llmbase">LLM base: {}</td><td colspan="3" class="rlbase">RL base: {}</td></tr>\n'.format(row[ci["project_llmbase"]], row[ci["project_rlbase"]])
        html_table += r2_html

html_table += '</tbody>\n'
html_table += '</table>\n'

with open("./docs/table.html", 'w') as file:
    file.write(html_table)
