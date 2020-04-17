#!/usr/bin/env python
# coding: utf-8

# In[100]:


import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


# In[101]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[102]:


# reflect an existing database into a new model
base = automap_base()


# In[103]:


# reflect the tables
base.prepare(engine, reflect=True)


# In[104]:


# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement


# In[105]:


# Create our session (link) from Python to the DB
session = Session(engine)


# In[106]:


#Flask Setup
app = Flask(__name__)


# In[107]:


# Flask Routes
@app.route("/")
def home():


# In[ ]:





# In[ ]:




