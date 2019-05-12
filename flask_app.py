
# coding: utf-8

# In[1]:


import numpy as np
import json
from flask import Flask, request, jsonify
import pickle
app = Flask(__name__)
# Load the model

@app.route('/api',methods=['POST'])
def predict():
    try:
        data=request.get_json(force=True)
        course_name=str(data["course_name"])
        model = pickle.load(open('recommendation_model.pkl','rb'))
    except ValueError:
        return jsonify("Enter number")

   
    return json.dumps(model.recomm(course_name))


# In[2]:


if __name__ == '__main__':
    app.run(port=8080, debug=True)

