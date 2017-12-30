print("yop")

quotes = ["c'est la vie pas le paradis", "yop, frangin"]
user_answer = input("tapez b")

if user_answer == "B":
  print("b")
elif user_answer == "C":
  print("c")
else:
  print("else")

def montre_tirade(my_list):	

  print(my_list[0])

montre_tirade(quotes)    	

print(quotes.index("yop, frangin"))  
