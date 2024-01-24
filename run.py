import urllib.request
import json
import os
import ssl
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


def allowSelfSignedHttps(allowed):
     # bypass the server certificate verification on client side
     if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
         ssl._create_default_https_context = ssl._create_unverified_context
 
allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
# =============================================================================
# data =  {
#   "data": [
#     {
#       "age": request.form['age'],
#       "anaemia": request.form['anaemia'],
#       "creatinine_phosphokinase": request.form['creatinine_phosphokinase'],
#       "diabetes": request.form['diabetes'],
#       "ejection_fraction": request.form['ejection_fraction'],
#       "high_blood_pressure": request.form['high_blood_pressure'],
#       "platelets": request.form['platelets'],
#       "serum_creatinine": request.form['serum_creatinine'],
#       "serum_sodium": request.form['serum_sodium'],
#       "sex": request.form['sex'],
#       "smoking": request.form['smoking'],
#       "time": request.form['time']
#     }
#   ],
#   "method": "predict"
# }
# 
# body = str.encode(json.dumps(data))
# 
# url = 'http://6feb22c7-6913-43a7-9851-38284fda76f6.eastus2.azurecontainer.io/score'
# # Replace this with the primary/secondary key or AMLToken for the endpoint
# api_key = 'ZUPBGBpV7D22vUYFdTW7ZzlycaWO70Wr'
# if not api_key:
#     raise Exception("A key should be provided to invoke the endpoint")
# 
# 
# headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
# 
# req = urllib.request.Request(url, body, headers)
# =============================================================================

# =============================================================================
import openai
 
# =============================================================================
# openai.api_key = "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"
#  
# response = openai.Completion.create(
#    model="text-davinci-003",
#    prompt=request.form['chatgpt'],
#    temperature=0.4,
#    max_tokens=500,
#    top_p=1,
#    frequency_penalty=0,
#    presence_penalty=0
#  )
#  
# print(response)
# =============================================================================
# 
# =============================================================================
# =============================================================================
# =============================================================================
# @app.route('/predict',methods=['POST'])
# def login():
#      openai.api_key = "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"
#      answer = openai.Completion.create(
#        model="text-davinci-003",
#        prompt=request.form['chatgpt'],
#        temperature=0.4,
#        max_tokens=500,
#        top_p=1,
#        frequency_penalty=0,
#        presence_penalty=0
#  )
#      print(answer)
#      return render_template('predictor.html', answer='Prediction: {}'.format(answer))
# =============================================================================
# =============================================================================

# =============================================================================
@app.route('/predict',methods=['POST'])
def predict():
#     
#     openai.api_key = "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"
#     answer = openai.Completion.create(
#       model="text-davinci-003",
#       prompt=request.form['chatgpt'],
#       temperature=0.4,
#       max_tokens=500,
#       top_p=1,
#       frequency_penalty=0,
#       presence_penalty=0
# )
#     print(answer)
#     #return render_template('predictor.html', answer='Prediction: {}'.format(answer))
# =============================================================================
    
    data =  {
      "data": [
        {
          "age": request.form['age'],
          "anaemia": request.form['anaemia'],
          "creatinine_phosphokinase": request.form['creatinine_phosphokinase'],
          "diabetes": request.form['diabetes'],
          "ejection_fraction": request.form['ejection_fraction'],
          "high_blood_pressure": request.form['high_blood_pressure'],
          "platelets": request.form['platelets'],
          "serum_creatinine": request.form['serum_creatinine'],
          "serum_sodium": request.form['serum_sodium'],
          "sex": request.form['sex'],
          "smoking": request.form['smoking'],
          "time": request.form['time']
        }
      ],
      "method": "predict"
    }

    body = str.encode(json.dumps(data))

    url = 'http://6feb22c7-6913-43a7-9851-38284fda76f6.eastus2.azurecontainer.io/score'
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = 'ZUPBGBpV7D22vUYFdTW7ZzlycaWO70Wr'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)
    
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        res=[]
        res=result.split()
        print(res)
        if res[1]== b'[1]}"':
            result1="High Risk"
        elif res[1]== b'[0]}"':
            result1="Low Risk"
        print(result1)
# =============================================================================
#         if res[18]==1:
#             result1="High Risk"
#         else:
#             result1="Low Risk"
# =============================================================================
                
            
       
        return render_template('index.html', prediction_text='Prediction: {}'.format(result1))
        #return render_template('predictor.html', answer='Prediction: {}'.format(answer))


        

    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        # print(error.info())
        # print(error.read().decode("utf8", 'ignore'))

if __name__ == "__main__":
    app.run(debug=True)