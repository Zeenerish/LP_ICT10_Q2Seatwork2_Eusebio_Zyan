from pyscript import document, display

#Define
def Calculate(e):
    fname = document.getElementById("Fname").value
    lname = document.getElementById("Lname").value
    science = int(document.getElementById("Science").value)
    math = int(document.getElementById("Math").value)
    english = int(document.getElementById("English").value)
    Fil = int(document.getElementById("Filipino").value)
    ICT = int(document.getElementById("ICT").value)
    pe = int(document.getElementById("PE").value)

#Formula
    equation = (science + math + english + ICT + Fil + pe) / 6
    averagegrade = round(equation, 2)

#Display
    display(f"Name: {fname} {lname}", target="name", append=False)
    display(f"Science: {science}", target="grades", append=False)
    display(f"Math: {math}", target="grades")
    display(f"English: {english}", target="grades")
    display(f"ICT: {ICT}", target="grades")
    display(f"Filipino: {Fil}", target="grades")
    display(f"PE: {pe}", target="grades")
    display(f"Your general weighted average is {averagegrade}", target="average", append=False)