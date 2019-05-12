
# coding: utf-8

# In[18]:


import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib
app = Flask(__name__)
# Load the model
model = joblib.load(open('recommendation_model.joblib','rb'))
@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.recomm((data['exp']))
    output = prediction[:5]
    return jsonify(output)


# In[19]:


if __name__ == '__main__':
    app.run(port=8080, debug=True)

