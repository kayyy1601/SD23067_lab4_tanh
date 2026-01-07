import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

def tanh(x):
    return np.tanh(x)

x = np.linspace(-10, 10, 100)
y = tanh(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Tanh Function")

st.pyplot(fig)
