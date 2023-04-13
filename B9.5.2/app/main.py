from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
import wget


app = FastAPI()


@app.get('/download_favicon', tags=['download'])
def d_favicon(url: str):
    # ��������� ������������� �� url �� favicon
    # ���� ������������� �� ���������. ���� ��� ���� �����.
    if url.endswith("favicon.ico"):
        response = wget.download(url, "site.ico")
        print(response)
        # ���������� ���� ������� ����������� ������
        return FileResponse(path=f"/code/{response}", filename=response, media_type='image/x-icon')
    else:
       return f"Wrong URL Try hard!!"
    
    
