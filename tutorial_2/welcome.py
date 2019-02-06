# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from flask import Flask, jsonify, request
from urllib import request as req
from watson_developer_cloud import NaturalLanguageClassifierV1

#We are setting the rootpath for our website
app = Flask(__name__)


workspace_ID = '0e6935x475-nlc-1067' #Your Workspace ID goes here
api_Key = 'HOees-copZVpTK8zXb-Lt9xu4DNmA5CZNANq-MEPXhPu' #Your iam_apikey goes here

#Create a NaturalLanguageClassiferV1 object
natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey= api_Key)


#This connects this Python File to the root directory of our website
#If we wanted to connect to a different website we would say
#@app.route('/about_Page')
#This function is now mapped to our webpage
#This has to return something to the webpage
@app.route('/')
def Welcome():
    return app.send_static_file('index.html')
 
@app.route('/analyze', methods=['GET', 'POST'])
def Analyze():
    #Gets the inputted string from the user
    comment_text = request.form['text']

    #Empty String is passed if text isn't entered
    results = ""

    #If text box isn't empty, do the following
    if comment_text != "":
        #Creates an instance of our natural language classifer with the provided next
        classes = natural_language_classifier.classify(workspace_ID, comment_text)
        #Parses the 'DetailedResponse' object provided by the API call.
        results = jsonify(classes.result)

    #Displays it the window
    return results

#This sets that we want to use local host 5000 for this call
port = os.getenv('PORT', '5003')

#This starts the web server if we are on the correct webpage
#If true, this starts the app with debugging at the correct port
if __name__ == "__main__":
    app.run(port= int(port), debug=True)

