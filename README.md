# Performance Tracker V1 📈
#### Video Demo: <URL HERE>
#### Description:
Performance Tracker V1 is a Streamlit-based web application designed to analyze student performance in real-time. The application allows users to upload an Excel file containing student data, select specific subjects to visualize, and generate performance insights, all within an intuitive graphical user interface. By leveraging powerful libraries such as Pandas, Plotly, and Streamlit, this tool provides educators with a comprehensive view of student progress and areas needing improvement.


## Project Overview
Performance Tracker V1 addresses the need for quick and effective student performance analysis. By integrating data visualization techniques, it transforms the boring excel sheets into intresting and captivating data visuals using a excel sheet standardised in the format I have provided

## Web App link and standard file format
-  web app: <https://performance-tracker.streamlit.app/>
-  standard excel format : <https://docs.google.com/spreadsheets/d/1scjpNbJAsxlxqITaOqgu7H2bEOzSqLfz/edit?usp=sharing&ouid=115804011227994331024&rtpof=true&sd=true>
### Main Features
- **File Upload**: Users can upload an Excel file containing student performance data.
- **Roll Number Verification**: Ensures that the entered roll number exists in the dataset.
- **Subject Selection**: Allows users to select specific subjects for performance visualization.
- **Performance Visualization**: Generates bar graphs, pie charts, and detailed performance analysis.
- **Feedback and Insights**: Provides personalized feedback based on the student's performance.

## Files in the Project

### project.py
The main Python script that runs the Streamlit web application. It includes the following key functions:
- `main()`: Initializes the Streamlit interface and calls the necessary functions.
- `upload_file()`: Handles the file upload and reads the data using Pandas.
- `check_roll_number()`: Verifies the existence of a roll number within the dataset.
- `visualize_performance()`: Creates interactive visualizations for the selected subjects and provides performance analysis.
- `create_gui()`: Sets up and displays the Streamlit graphical user interface.

### test_project.py
Contains the test functions for the custom functions defined in `project.py`. Tests ensure the correct functionality of the following:
- `test_upload_file()`: Validates the file upload and reading process.
- `test_check_roll_number()`: Tests the roll number verification logic.
- `test_visualize_performance()`: Ensures that performance visualizations are generated correctly.
- `test_create_gui()`: Confirms that the GUI is created without errors.

### requirements.txt
Lists all the required libraries and dependencies to run the project. Ensures that the environment can be replicated accurately.
- streamlit
- pandas
- plotly
- openpyxl
- numpy
- pytest

## Primary applications used
### Design Choices
1. **Streamlit for GUI**: Chosen for its simplicity and ease of use in creating web applications.
2. **Plotly for Visualization**: Provides interactive and visually appealing charts and graphs.
3. **Pandas for Data Handling**: Essential for efficient data manipulation and analysis.

### Challenges
1. **Data Validation**: Ensuring that the uploaded file contains valid and complete data.
2. **Error Handling**: Providing meaningful error messages and feedback to users.

### Future Improvements
1. **Enhanced Error Handling**: Improve the robustness of the application by adding more comprehensive error handling.
2. **Additional Visualizations**: Include more types of charts and graphs for deeper insights.
3. **User Authentication**: Implement user authentication to provide personalized experiences.

## Conclusion
Performance Tracker V1 is a powerful tool designed to assist educators in analyzing student performance efficiently. By converting raw data into actionable insights, it enables more informed decision-making. The project's modular design, detailed visualizations, and intuitive interface make it a valuable addition to any educational institution's toolkit.

For any enquires feel free to reach out to me at <dimareznokov@gmail.com>

Feel free to explore, contribute, and provide feedback to further enhance this project!
