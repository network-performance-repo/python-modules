import ftplib
import logging
import re

class FTPsession:
    def __init__(self, host, username, password):
        logging.basicConfig(filename='logger.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
        self.host = host
        self.username = username
        self.password = password
        try:
            self.FTPsession = ftplib.FTP(self.host, self.username, self.password)
        except Exception as e:
            logging.error("*****************")
            logging.error("Error connecting to "+self.host+".... ")
            logging.error(e)
            logging.error("\n")
            exit()
        else:
            logging.error("successfully connected to "+self.host+" .... ")

    def uplaod(self, filename='', remote_path='', local_path=''):
        remote_path, local_path = self.check_path_accuracy(remote_path, local_path)
        self.FTPsession.cwd(remote_path)
        try:
            self.FTPsession.storbinary("STOR " + filename, open(local_path+filename, 'rb'))
        except Exception as e:
            logging.error("*****************")
            logging.error("Error uploading "+filename+" to "+self.host+" .... ")
            logging.error(e)
            logging.error("\n")
        else:
            logging.error(filename+" successfully uploaded to "+self.host+" .... ")
        self.FTPsession.cwd("/")

    def download(self, remote_path='', local_path='', filename='', regex=''):
        remote_path,local_path = self.check_path_accuracy(remote_path,local_path)
        if filename != '':
            self.FTPsession.cwd(remote_path)
            with open(local_path+filename, 'wb') as f:
                logging.error(filename+" successfully downloaded from "+self.host+" .... " )
                self.FTPsession.retrbinary('RETR ' + filename, f.write)
        elif regex != '':
            files = self.get_files(remote_path,regex)
            self.FTPsession.cwd(remote_path)
            for file in files:
                with open(local_path + file, 'wb') as f:
                    self.FTPsession.retrbinary('RETR ' + file, f.write)
                    logging.error(file + " successfully downloaded from " + self.host + " .... ")
        self.FTPsession.cwd("/")

    def check_path_accuracy(self,rempte_path, local_path):
        if not rempte_path.startswith('/'):
            rempte_path = '/'+rempte_path
        if not local_path.endswith('/'):
            local_path = local_path + '/'
        return rempte_path, local_path

    def get_files(self, path="/", regex=''):
        self.FTPsession.cwd(path)
        files = self.FTPsession.nlst()
        self.FTPsession.cwd("/")
        if regex != '':
            r_files = []
            for file in files:
                if re.match(regex, file):
                    r_files.append(file)
            return r_files
        return files

    def close(self):
        self.FTPsession.close()
        logging.error("connection closed.")
