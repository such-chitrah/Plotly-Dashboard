import dash
from dash import html
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

fig = plt.plot(np.array([1, 2, 3]), np.array([4, 5, 6]))
buf = io.BytesIO()  # create an in-memory buffer
plt.savefig(buf, format="png")  # save your image into this buffer
plt.close()
data = "data:image/png;base64,{}".format(
    base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
eda_layout_plt = html.Img(id='example', src=data)
