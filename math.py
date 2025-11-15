try:
  a = float(input("enter first number:"))
  b = float(input("enter second number:"))

  print(f"Addition:{a+b}")
  print(f"subtraction:{a-b}")
except ValueError:
  print("Please enter valid numbers.")
