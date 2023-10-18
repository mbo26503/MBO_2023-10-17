role = "manager"
permissions = ['modify_finances']
resource = input("Podaj nazwę zasobu, do którego dchesz mieć dostęp: ")

if role == "admin":
    print("dostęp przyznany")
elif role == "manager":
    if resource in ['repors', 'data', 'users']:
        print("Dostep przyznany")
    elif "modify_finances" in permissions and resource == "finances":
        print("Dostęp przyznany")
    else:
        print("Dostęp zabroniony")
elif role == 'employee':
    if resource == "data":
        print("Dostęp przyznany")
    elif "view_reports" in permissions and resource == "reports":
        print("Dostęp przysznany")
else
