from flask import Flask, request, jsonify
from collections import OrderedDict

app = Flask(__name__)

FULL_NAME = "divya_srinivasan"
DOB = "23072004"
EMAIL = "divyasriniv9@gmail.com"
ROLL = "22BCE1307"

def make_user_id(name, dob):
    return f"{name.strip().lower().replace(' ', '_')}_{dob}"

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        payload = request.get_json(force=True)
    except:
        return jsonify({"is_success": False, "error": "invalid json"}), 400

    arr = payload.get("data", [])
    ev, od, al, sp = [], [], [], []
    tot = 0

    for x in arr:
        s = str(x)
        if s.isdigit():
            n = int(s)
            if n % 2 == 0:
                ev.append(s)
            else:
                od.append(s)
            tot += n
        elif s.isalpha():
            al.append(s.upper())
        else:
            sp.append(s)

    joined = "".join(al)
    rev = joined[::-1]
    concat = ""
    for i, ch in enumerate(rev):
        concat += ch.upper() if i % 2 == 0 else ch.lower()

    out = OrderedDict([
        ("is_success", True),
        ("user_id", make_user_id(FULL_NAME, DOB)),
        ("email", EMAIL),
        ("roll_number", ROLL),
        ("odd_numbers", od),
        ("even_numbers", ev),
        ("alphabets", al),
        ("special_characters", sp),
        ("sum", str(tot)),
        ("concat_string", concat)
    ])
    
    return jsonify(out), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
