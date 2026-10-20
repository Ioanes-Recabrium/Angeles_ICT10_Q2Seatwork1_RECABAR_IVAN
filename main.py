from pyscript import document

club_members = ["Michel Jackson", "Ivan Hamburger", "Chicken Nugget", "Peter Schmit"]

def check_candidate(e):
    first = document.getElementById("first-name").value.strip()
    last = document.getElementById("last-name").value.strip()
    full_name = first + " " + last
    is_member = full_name in club_members
    msg_false = "sorry " + full_name + ", your name is not on mickey mouse."
    msg_true = "congrats " + full_name + "! welcome to the mickey squad"
    messages = [msg_false, msg_true]
    message_element = document.getElementById("result")
    message_element.innerHTML = messages[int(is_member)]
    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""