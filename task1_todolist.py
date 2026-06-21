tasks=[]

while True:
  print("1.Add 2.View 3.Exit")
  ch=input("Choice: ")

  if ch=="1":
     tasks.append(input("Task: "))
  elif ch=="2":
     for i in tasks:
         print(i)
  elif ch=="3":
     break
