import dropbox
import os

from dropbox.files import WriteMode 

class TransferData:
    def __init__(self,acess_token):
        self.access_token = acess_token
    def upload_file(self,file_from,file_to,local_path):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to, relative_path)
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))
def main():
    access_token = 'sl.A0ecySiZ9Jcta3OCX8wHujGYNQSZVnk_Bbc62wuyG3EDORkoNWPcgrkS8B5_VdR46iKh-JOPsm0ancDPeEdd0K3IsJOYXdTuH1Eyr0gQxb0mZ-dS_zaofaMphVJnajPhH9w_TCI'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer:- ")
    file_to = input("Enter the full path to upload to dropbox:-")
    local_path = input("Enter the local path for the file:-")
    transferData.upload_file(file_from,file_to,local_path)
    
    print("File has been moved")
main()
