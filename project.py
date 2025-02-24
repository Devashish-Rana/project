import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

def main():
    create_gui()

def upload_file():
    fileupload = st.file_uploader('Please Upload your file here', type='XLSX')
    if fileupload is not None:
        try:
            df = pd.read_excel(fileupload, engine='openpyxl')
            st.success('Data Uploaded successfully')
            return df
        except Exception as error:
            st.error('Error: Please reupload the file')
            return None
    else:
        st.info('Please upload the file')
        return None

def visualize_performance(selectedroll, selection):
    studentname = selectedroll['Name'].values[0]
    splitname = studentname.split()[0]
    st.write(f"{studentname} performance in selected subjects")
    
    student_performance = selectedroll[selection].T
    student_performance.columns = ['Marks']
    student_performance['Marks'] = student_performance['Marks'].astype(float)
    student_performance['Subjects'] = student_performance.index

    bar_colors = ['#ADD8E6', '#FA8072', '#FFD700', '#2E8B57', '#EE82EE']
    markercolors = ['#FFFFFF', '#8B0000', '#FF8C00', '#008080', '#800080']

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Bar(x=student_performance['Subjects'], y=student_performance['Marks'], name='Marks', marker_color=bar_colors), secondary_y=False)
    fig.add_trace(go.Scatter(x=student_performance['Subjects'], y=student_performance['Marks'], name='Score marker', mode='lines+markers', line=dict(color='white'), marker=dict(color=markercolors, size=10)), secondary_y=False)

    fig.update_layout(title_text=f"{studentname}'s performance in Selected Subjects", xaxis_title="Subjects", yaxis_title="Marks", yaxis=dict(range=[0, 100]), width=1500, height=509, showlegend=True)
    st.plotly_chart(fig)

    strongestsubject = student_performance['Marks'].idxmax()
    weakestsubject = student_performance['Marks'].idxmin()

    pie = px.pie(values=student_performance['Marks'], names=student_performance['Subjects'], title=f"{splitname} performance in selected subjects")
    st.plotly_chart(pie)

    st.header(f"{splitname}'s Performance Analysis 🧠")
    st.subheader("Strengths 💪")
    st.write(f"{splitname} scored highest in {strongestsubject}")
    st.subheader("Cons 📉")
    st.write(f"{splitname} needs to work more on {weakestsubject}")

    Total = student_performance['Marks'].sum()
    percentage = Total / 500 * 100
    standardpercentage = f"{percentage:.2f}"
    st.subheader(f"{splitname}'s percentage is {standardpercentage}")

    percentage2 = percentage + 3
    standardpercentage2 = f"{percentage2:.2f}"

    if percentage >= 90:
        st.write(f'Excellent job {splitname}, keep it up!')
    elif 85 > percentage > 79:
        st.write(f'Good Work {splitname}, next time target for {standardpercentage2}%')
    else:
        st.write(f'Keep Working Hard {splitname}, next time target for {standardpercentage2}%')

def create_gui():
    st.set_page_config(page_title='Performance Tracker V1')
    st.header('Performance Tracker V1 🧑‍🏫')
    st.subheader('Analyse Student Performance in real time')

    df = upload_file()
    if df is not None:
        roll_num = st.number_input("Please enter the student's roll number")
        if roll_num in df['Roll Number'].values:
            st.success('Roll number present')
            selectedroll = df[df['Roll Number'] == roll_num]
            selection = st.multiselect('Choose subjects to visualise', ('English', 'Pol Sci', 'History', 'Economics', 'Optional'))
            if selection:
                visualize_performance(selectedroll, selection)
            else:
                st.warning('Please select subjects to visualise')
        else:
            st.error('Please enter a valid roll number')

if __name__ == "__main__":
    main()