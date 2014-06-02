'''copy this file as koha_config.py and change the credentials and settings below'''


'''your koha credentials'''
user = 'admin'                                       #put your admin username here
passwd = 'adminpassword'						     #put your admin password here
domain = 'http://mysubdomain-staff.kohalibrary.com'  #this is to be filled with the root domain for your hosted koha staff client

'''export configurations'''
xml_status = 1            #set this to 1 if you want the export to return as XML, else it returns as MARC by default
total = 250000            #this is the total number of bibliographic records you have
increment = 5000          #this is increments in which the records will be downloaded - I have found that more than 5000 records cause a timeout.