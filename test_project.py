import pytest
import pandas as pd
from project import upload_file, visualize_performance, create_gui

def test_upload_file(monkeypatch):
    from io import BytesIO

    df = pd.DataFrame({
        'Roll Number': [1, 2],
        'Name': ['John Doe', 'Jane Doe'],
        'English': [85, 90],
        'Pol Sci': [80, 88],
        'History': [90, 85],
        'Economics': [70, 75],
        'Optional': [95, 80]
    })
    
    excel_file = BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    def mock_file_uploader(label, type=None):
        return excel_file
    
    monkeypatch.setattr(st, 'file_uploader', mock_file_uploader)
    
    uploaded_df = upload_file()
    assert uploaded_df.equals(df)

def test_visualize_performance(monkeypatch):
    df = pd.DataFrame({
        'Roll Number': [1],
        'Name': ['John Doe'],
        'English': [85],
        'Pol Sci': [80],
        'History': [90],
        'Economics': [70],
        'Optional': [95]
    })
    selectedroll = df[df['Roll Number'] == 1]
    selection