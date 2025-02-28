# Importar librerías
import pandas as pd # importar librería pandas
import streamlit as st # importar librería streamlit
import plotly.express as px #importar librería plotly

st.header('Datos ventas de autos') #título

car_data = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv') #leer los datos
fig = px.histogram(car_data, x='odometer', y='price') #crear histograma
fig.show() #mostrar histograma

fig = px.scatter(car_data, x='odometer', y='price') #crear scatter plot
fig.show() #mostrar scatter plot

hist_button = st.button('Construir histograma') #botón para mostrar histograma
if hist_button: #si se presiona el botón
    #escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer') #crear histograma
    st.plotly_chart(fig, use_contained_width=True) #mostrar histograma

scatter_button = st.button('Construir histograma') #botón para mostrar histograma
if scatter_button: #si se presiona el botón
    #escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer') #crear histograma
    st.plotly_chart(fig, use_contained_width=True) #mostrar histograma    

#crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma') #casilla de verificación
if build_histogram: #si está seleccionada la casilla
    #escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer') #crear histograma
    st.plotly_chart(fig, use_contained_width=True) #mostrar histograma

#crear casillas de verificación
build_scatter = st.checkbox('Construir un histograma') #casilla de verificación
if build_scatter: #si está seleccionada la casilla
    #escribir un mensaje
    st.write('Construir un diagrama de dispersión para la columna odómetro')
    fig = px.scatter(car_data, x='odometer') #crear diagrama de dispersión
    st.plotly_chart(fig, use_contained_width=True) #mostrar diagrama de dispersión
