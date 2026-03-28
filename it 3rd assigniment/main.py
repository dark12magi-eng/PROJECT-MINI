from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

@app.route("/", methods=["GET", "POST"])
def home():
    results = {
        "sum":"","odd_even":"","loop":"","largest":"",
        "factorial":"","table":"",
        "if_else":"","loop_explain":"",
        "importance":"","systems":""
    }

    if request.method == "POST":
        action = request.form.get("action")

        try:
            # 1 Add
            if action == "sum":
                a = request.form.get("a")
                b = request.form.get("b")
                if a and b:
                    results["sum"] = int(a) + int(b)

            # 2 Odd Even
            elif action == "odd_even":
                n = request.form.get("num")
                if n:
                    results["odd_even"] = "Even" if int(n)%2==0 else "Odd"

            # 3 Loop 1-10
            elif action == "loop":
                results["loop"] = " ".join(str(i) for i in range(1,11))

            # 4 Largest
            elif action == "largest":
                x = request.form.get("x")
                y = request.form.get("y")
                z = request.form.get("z")
                if x and y and z:
                    results["largest"] = max(int(x), int(y), int(z))

            # 5 Factorial
            elif action == "factorial":
                n = request.form.get("fact")
                if n:
                    results["factorial"] = factorial(int(n))

            # 6 Multiplication Table
            elif action == "table":
                n = request.form.get("table")
                if n:
                    n = int(n)
                    results["table"] = "<br>".join(f"{n} x {i} = {n*i}" for i in range(1,11))

            # 7 If vs Else If
            elif action == "if_else":
                num = request.form.get("ifnum")
                if num:
                    num = int(num)
                    if num > 10:
                        results["if_else"] = "Greater than 10"
                    elif num == 10:
                        results["if_else"] = "Equal to 10"
                    else:
                        results["if_else"] = "Less than 10"

            # 8 Loop Example
            elif action == "loop_explain":
                n = request.form.get("loopnum")
                if n:
                    n = int(n)
                    results["loop_explain"] = " ".join(str(i) for i in range(1, n+1))

            # 9 Salary Automation System
            elif action == "importance":
                salary = request.form.get("salary")
                bonus = request.form.get("bonus")

                if salary and bonus:
                    salary = int(salary)
                    bonus = int(bonus)

                    tax = salary * 0.1
                    total = salary + bonus - tax

                    results["importance"] = f"""
                    Salary: {salary} <br>
                    Bonus: {bonus} <br>
                    Tax (10%): {tax} <br>
                    Final Salary: {total}
                    """

            # 10 Banking + School System
            elif action == "systems":
                deposit = request.form.get("deposit")
                marks = request.form.get("marks")

                output = ""

                if deposit:
                    balance = 1000
                    balance += int(deposit)
                    output += f"Bank Balance after deposit: {balance}<br>"

                if marks:
                    marks = int(marks)
                    grade = "Pass" if marks >= 50 else "Fail"
                    output += f"Student Result: {grade}"

                results["systems"] = output

        except:
            pass

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)