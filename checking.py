import FTP
query = "select *  from maps_cell_daily_log where filedate=to_date('2021-03-13','yyyy-mm-dd')"
query2 = "select *  from maps_cell_daily_log where filedate=to_date('2021-03-14','yyyy-mm-dd')"

# session = FTP.FTPsession(host='intftp', username='*****', password='******')
# session.uplaod(filename='testfile', remote_path='NWG_MKT', local_path='.')
# session.download(filename='Gilan_2021-03-18.csv', local_path='.', remote_path='NWG_MKT')
# session.download(regex='Gilan_*', local_path='.', remote_path='NWG_MKT')
# files = session.get_files(path='NWG_MKT',regex='Giladfg_*')
# print(files)
# session.close()


# import DB_connection
# db_session = DB_connection.DbSession(host='****',username='****', password='****')
# db_session.export_from_query(query, 'export.csv')
# print(db_session.df_from_query(query))
# print(db_session.launch_query(query))
# db_session.close()


# import excel
# df = db_session.df_from_query(query)
# df2 = db_session.df_from_query(query2)
# excel.File(df, 'test.xlsx','mysheet')
# excel.append_sheet(df2,'test.xlsx','sheet2')


import CSVmodule
# df = CSVmodule.replace_csvfile(file='./3G_Cell_Daily.csv', column='On air', update_from='inactive', update_to='changed')
# print(df)
# df.to_csv("test.csv")
#
# df2 = CSVmodule.filter_csvfile(file='./3G_Cell_Daily.csv', column='On air', exclude_values=['active'])
# print(df2)
# df2.to_csv("test2.csv")
#
# df3 = CSVmodule.pvot_csvfile(file='./3G_Cell_Daily.csv', column='On air')
# print(df3)
# df3.to_csv("test3.csv")

# df3 = CSVmodule.vlookup_csvfile('./2G_Cell_Daily_2021011610_88cf85e5e10340c882b786554661f52f_101100.csv','2G CELL',
#                                 './2G_atoll.csv','CELL',3)


# import smtp
# smtp.send_email(server='*******', email='*********',password='******',
#                 to=['******'], cc=['*****'],subject='checking smtp', body='just testing',
#                 attachement='test.xlsx')

