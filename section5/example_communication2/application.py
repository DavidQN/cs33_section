from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# initial landing page 
@app.route('/', methods=['GET', 'POST'])
def app_home():
    return render_template("index.html", variable_here = 100)

# index.html makes a request to this API endpoint 
@app.route("/getData", methods=['GET'])
def getData():

    # grab the two arguments that were push up to this API
    entry2Value = request.args.get('entry2_id')
    entry1Value = request.args.get('entry1_id')
    print(entry1Value, entry2Value, 'incoming arguments')


    var1 = int(entry2Value) + int(entry1Value)
    var2 = 10
    var3 = 15
    print(var1, var2, var3, "testing2")
    
    # return JSON to frontend
    return jsonify({ 'var1': var1, 'var2': var2, 'var3': var3 })

app.run(debug=True)