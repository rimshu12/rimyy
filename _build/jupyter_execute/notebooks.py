#!/usr/bin/env python
# coding: utf-8

# # Content with notebooks
# 
# You can also create content with Jupyter Notebooks. This means that you can include
# code blocks and their outputs in your book.
# 
# ## Markdown + notebooks
# 
# As it is markdown, you can embed images, HTML, etc into your posts!
# 
# ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# 
# You can also $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# or
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# 
# ## MyST markdown
# 
# MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# ## Code blocks and outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[2]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# In[3]:


import ipywidgets as widgets
widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)


# In[4]:


# Install a pip package in the current Jupyter kernel
import sys
get_ipython().system('{sys.executable} -m pip install numpy')


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)

# In[5]:


import numpy as np


# In[6]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt


# In[7]:


get_ipython().system('{sys.executable} -m pip install plotly')


# In[8]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[9]:


import ipywidgets as widgets
widgets.ColorPicker(
    concise=False,
    description='Pick a color',
    value='blue',
    disabled=False
)


# In[10]:


import ipywidgets as widgets
widgets.DatePicker(
    description='Pick a Date',
    disabled=False
)


# In[11]:


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()


# In[20]:


from IPython.display import Image
Image("peacock.jpg")


# In[21]:


from IPython.display import YouTubeVideo

SalidaVideo = widgets.Output()

with SalidaVideo:
    display(YouTubeVideo('DsROfrRB-1k', width=500, height=500))
    
Salidas = widgets.HBox([SalidaVideo])
display(Salidas)


# In[24]:


import ipywidgets as widgets
widgets.Combobox(
    # value='John',
    placeholder='Choose Someone',
    options=['Peter', 'Rimy', 'Pinky', 'Ringo'],
    description='Combobox:',
    ensure_option=True,
    disabled=False
)


# In[ ]:


import plotly.express as px
df = px.data.tips()
fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)
fig


# In[ ]:





# In[ ]:




