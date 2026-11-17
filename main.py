from pyscript import document, when

grade7 = {"Luisito Balajadia", "Bianca Franco"}
grade8 = {"Winmhar Salazar", "Caitlyn Garcia"}
grade9 = {"Angelina Cristobal", "Bong Alegrid"}
grade10 = {"Ruel Roque", "Roselle Sarmiento"}

members = grade7.union(grade8, grade9, grade10)

@when("click", "#add_button")
def add_member(event):
    global members

    first = document.querySelector("#first_name").value
    last = document.querySelector("#last_name").value

    members = members.union({first + " " + last})

    document.querySelector("#results").innerHTML = f"{members}<br>Total Members: {len(members)}"