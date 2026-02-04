students={
    1: {"name":"Mike Smith", "age":19, "university":"Thrombomb University","program":"BSc mathematics"},
    2: {"name":"Rudolfo Epicurenus", "age":22, "university":"Kafoofoo Academic Centre of Excellence", "program":"MSc chemistry"},
    3: {"name":"Samantari Blunderwand", "age": 23, "university":"Stroongwaddel Swedish Braincentre", "program":"MSc physics"}
}

print (f"""
name: {students[1]["name"]} 
age {students[1]["age"]}
university {students[1]["university"]} 
program: {students[1]["program"]}
""")

students[2]["program"]="BSc data science"

print (f"""
name: {students[2]["name"]} 
age {students[2]["age"]}
university {students[2]["university"]} 
program: {students[2]["program"]}
""")

students[1]["modules"]=["mathematics III", "computer science III"]

print (f"""
name: {students[1]["name"]} 
age {students[1]["age"]}
university {students[1]["university"]} 
program: {students[1]["program"]}
modules: {students[1]["modules"]}
""")

del students[2]["age"]

try:
    print (f"""
    name: {students[2]["name"]} 
    age {students[2]["age"]}
    university {students[2]["university"]} 
    program: {students[2]["program"]}
    """)
except Exception as ex:
    print (str(ex))

for key in students[3]:
    print (key)

for value in students[3].values():
    print (value)

for key, value in students[3].items():
    print (f"key '{key}' value '{value}'")