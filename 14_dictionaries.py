myfamily = {
  "child1" : {
    "name" : "Arys",
    "year" : 2008
  },
  "child2" : {
    "Me" : "Ali",
    "year" : 2006
  },
  "child3" : {
    "name" : "Arsen",
    "year" : 2009
  },
  "child4" : {
    "name" : "Ars",
    "year" : 2003
  },
  "child5" : {
    "name" : "Akzhol",
    "year" : 2005
  }
}

for child, details in myfamily.items():
    print(f"{child}: {details}")