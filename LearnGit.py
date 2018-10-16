#Add, Pull, commit, check status using git.
print("Learn Git Commands")
print("1.  Create Repository.")
print("2.  Add Code.")
print("3.  See git Status.")
print("4.  See git Logs.")
print("5.  Do Git Commit.")
print("6.  Push to git repo.")
print("\n")
choice = int(input("Enter your choice..!!\n"))
if choice == 1:
    print("Created Repository in your git account.")
elif choice == 2:
    print("use command : git add 'File-name'")
elif choice == 3:
    print("use command : git status.")
elif choice == 4:
    print("use command : git log.")
elif choice == 5:
    print("use command : git commit -m 'massage'.")
elif choice == 6:
    print("use command : git push.")
else:
    print("Enter Correct choice")