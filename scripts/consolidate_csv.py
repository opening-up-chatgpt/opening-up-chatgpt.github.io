import csv
import glob
import pandas as pd
from bs4 import BeautifulSoup


def create_dataframe(files):
    # initialize list of rows
    lrows = []
    # Read the input CSV file, transpose the rows and columns and save to dictionary
    for i, fname in enumerate(files):
        with open(fname, 'r') as file:
            file.readline()
            reader = csv.reader(file)
            rows = list(reader)
            transposed = list(zip(*rows))
        # get column names
        if i == 0:
            column_names = transposed[0]
        # append transposed row to list of tuples
        lrows.append(tuple(transposed[1]))
    df = pd.DataFrame(lrows, columns = column_names)
    # get rid of rows without a project_name
    df = df[df["project_name"] != ""]
    df.set_index("project_name", inplace = True)
    return df


def calculate_openness(df):
    openness_weights = {
        "opencode": 1, 
        "llmdata": 1, 
        "llmweights": 1, 
        "rldata": 1, 
        "rlweights": 1, 
        "license": 1, 
        "code": 1, 
        "architecture": 1, 
        "preprint": 1, 
        "paper": 1, 
        "modelcard": 1, 
        "datasheet": 1, 
        "package": 1, 
        "api": 1
    }
    class_values = {
        "open": 1,
        "partial": 0.5,
        "closed": 0,
    }
    openness = []
    projects = df.index.tolist()
    for p in projects:
        cumul_openness = 0
        for v, w in openness_weights.items():
            vclass = df.loc[p, v + "_class"]
            vvalue = class_values[vclass] if vclass in class_values else 0
            cumul_openness += w * vvalue
        openness.append(cumul_openness)
    # add the openness variable to the DataFrame
    df["openness"] = openness
    return df


def write_html(df):
    html_table = '<table>\n'
    html_table += '<thead>\n'
    html_table += '<tr class="main-header"><th>Project</th><th colspan="6">Availability</th><th colspan="6">Documentation</th><th colspan="2">Access</th></tr>\n'
    html_table += '<tr class="second-header"><th>(maker, bases, URL)</th><th>Open code</th><th>LLM data</th><th>LLM weights</th><th>RLHF data</th><th>RLHF weights</th><th>License</th><th>Code</th><th>Architecture</th><th>Preprint</th><th>Paper</th><th>Modelcard</th><th>Datasheet</th><th>Package</th><th>API</th></tr>\n'
    html_table += '</thead>\n'
    html_table += '<tbody>\n'
    # loop through projects
    projects = df.index.tolist()
    for p in projects:
        # add data by looping through each row and converting it 2 rows for the html table.
        # also add classes to the <td> elements for colour coding and links to source of the class judgement: https://github.com/liesenf/awesome-open-chatgpt/issues/12
        cells = ["opencode", "llmdata", "llmweights", "rldata", "rlweights", "license", "code", "architecture", "preprint", "paper", "modelcard", "datasheet", "package", "api"]
        # first row
        r1_html = '<tr class="row-a"><td class="name-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(df.loc[p, "project_link"], df.loc[p, "project_notes"], p)
        for c in cells:
            cl = df.loc[p, c + "_class"]
            link = df.loc[p, c + "_link"]
            notes = df.loc[p, c + "_notes"]
            symbol = "&#10004;&#xFE0E" if cl == "open" else "~" if cl == "partial" else "&#10008;" if cl == "closed" else "?"
            r1_html += '<td class="{} data-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)
        r1_html += "</tr>\n"
        html_table += r1_html
        # second row
        r2_html = '<tr class="row-b"><td class="org"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(df.loc[p, "org_link"], df.loc[p, "org_name"], df.loc[p, "org_name"])
        r2_html += '<td colspan="3" class="llmbase">LLM base: {}</td><td colspan="3" class="rlbase">RL base: {}</td></tr>\n'.format(df.loc[p, "project_llmbase"], df.loc[p, "project_rlbase"])
        html_table += r2_html
    # closing tags
    html_table += '</tbody>\n'
    html_table += '</table>\n'
    return html_table


def create_index(table):
    # read and parse the template file
    with open("./docs/template.html", "r") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # find the target location
    target_element = soup.find(id="included-table")
    # Convert the HTML code string into a BeautifulSoup object and append it to the target element
    target_element.append(BeautifulSoup(table, 'html.parser'))
    # write to disk
    with open("./docs/index.html", 'w') as f:
        f.write(str(soup))


#the path of the csv files to combine
path = r'./projects' 
all_files = glob.glob(path + "/*.csv")

df = create_dataframe(all_files)
df = calculate_openness(df)
# sort by openness and project name
df = df.sort_index(ascending=False).sort_values(by="openness", ascending=False)
table = write_html(df)
create_index(table)