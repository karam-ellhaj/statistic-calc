from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    if request.method=="POST":
        dataset  = request.form["dataset"].split(",")
        return render_template("answer.html",dataset=dataset,mean=mean(dataset),mod=mod(dataset),median=median(dataset))
    return render_template("index.html")

def segma(data):
    segma = 0
    for datum in data:
        datum = int (datum)
        segma += datum
    return segma


def mean(data):
    return segma(data) / data.__len__()

def mod(data):
    counts = []
    for datum in data :
        counts.append(data.count(datum))
    mod = data[counts.index(max(counts))]
    return mod      

def median(data):                                                               
    print(data.__len__())
    median_index =int( data.__len__()/2)
    if data.__len__() % 2 == 0:
        median = mean([data[median_index],data[median_index-1]])
    else:
        median= data[int(data.__len__()/2)]
    return median



app.run(debug=True)
