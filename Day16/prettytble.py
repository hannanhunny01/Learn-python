from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["pikachu","Squit","charmandel"])
table.add_column("Type",["electric",'water','fire'])
print(table)