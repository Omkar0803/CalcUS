from constants import *

TABLE_TEMPLATE = """
<table class="table">
    <thead>
        <tr>
            <th>{}</th>
            {}
        </tr>
    </thead>
    <tbody>
        {}
    </tbody>
</table>"""

def basis_sets():
    softwares = SOFTWARE_BASIS_SETS.keys()
    basis_sets = []
    header = ""
    for software in softwares:
        header += "<th>{}</th>".format(software)
        for bs in SOFTWARE_BASIS_SETS[software].keys():
            if bs not in basis_sets:
                basis_sets.append(bs)
    body = ""
    for bs in sorted(basis_sets):
        availabilities = ""
        name = ""
        for software in softwares:
            if bs in SOFTWARE_BASIS_SETS[software].keys():
                if name == "":
                    name = SOFTWARE_BASIS_SETS[software][bs]
                availabilities += "<td>X</td>\n"
            else:
                availabilities += "<td></td>\n"

        body += """
            <tr>
                <td>{}</td>
                {}
            </tr>""".format(name, availabilities)

    print(TABLE_TEMPLATE.format("Basis Set", header, body))

def functionals():
    softwares = SOFTWARE_METHODS.keys()
    functionals = []
    header = ""
    for software in softwares:
        header += "<th>{}</th>".format(software)
        for f in SOFTWARE_METHODS[software].keys():
            if f not in functionals:
                functionals.append(f)
    body = ""
    for f in sorted(functionals):
        availabilities = ""
        name = ""
        for software in softwares:
            if f in SOFTWARE_METHODS[software].keys():
                if name == "":
                    name = SOFTWARE_METHODS[software][f]
                availabilities += "<td>X</td>\n"
            else:
                availabilities += "<td></td>\n"

        body += """
            <tr>
                <td>{}</td>
                {}
            </tr>""".format(name, availabilities)

    print(TABLE_TEMPLATE.format("Functionals", header, body))

if __name__ == "__main__":
    basis_sets()
    #functionals()
