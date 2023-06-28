import csv
import glob
#the path of the csv files to combine
path = r'./projects' 
all_files = glob.glob(path + "/*.csv")

html_table = '<table>\n'
html_table += '<thead>\n'
html_table += '<tr><th class="main-header">Project</th><th colspan="6" class="main-header">Availability</th></tr>\n'
html_table += '<tr><th class="row-b">(maker, bases, URL)</th><th class="second-header">Open code</th><th class="second-header">LLM data</th><th class="second-header">LLM weights</th><th class="second-header">RLHF data</th><th class="second-header">RLHF weights</th><th class="second-header">License</th></tr>\n'
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
    cells = ["opencode", "llmdata", "llmweights", "rldata", "rlweights", "license"]
    #attributes = ["_class", "_link", "_notes"]
    for row in transposed[1:]:
        # first row
        r1_html = '<tr><td class="row-a name-cell"><a href="{}" title="{}">{}</a></td>'.format(row[ci["project_link"]], row[ci["project_notes"]], row[ci["project_name"]])
        for c in cells:
            cl = row[ci[c + "_class"]]
            link = row[ci[c + "_link"]]
            notes = row[ci[c + "_notes"]]
            symbol = "&#10004;" if cl == "open" else "~" if cl == "partial" else "&#10008;" if cl == "closed" else ""
            r1_html += '<td class="{} row-a data-cell"><a href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)
        r1_html += "</tr>\n"
        html_table += r1_html
        # second row
        r2_html = '<tr><td class="row-b"><a href="{}" title="{}">{}</a></td>'.format(row[ci["org_link"]], row[ci["org_notes"]], row[ci["org_name"]])
        r2_html += '<td colspan="3" class="row-b">LLM base: {}</td><td colspan="3" class="row-b">RLHF base: {}</td></tr>\n'.format(row[ci["project_llmbase"]], row[ci["project_rlbase"]])
        html_table += r2_html

html_table += '</tbody>\n'
html_table += '</table>\n'

with open("./site/table.html", 'w') as file:
    file.write(html_table)
