"""
menu-driven program
"""


name = input("Enter the name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
   if choice == "H":
      print("hello", name)
      print()
   elif choice == "G":
       print("goodbye", name)
       print()
   else:
       print("Invalid choice")
       print()
   print("(H)ello")
   print("(G)oodbye")
   print("(Q)uit")
   choice = input(">>> ").upper()
print("Finished")