import xml.dom.minidom as m
document = m.parse("C:\\Users\\thiag\\Documents\\GitHub\\SENAC\\senac_django\\USANDO_VERSIONAMENTO\\python_cHTML")
table_list = document.getElementById("nome")
print(table_list)