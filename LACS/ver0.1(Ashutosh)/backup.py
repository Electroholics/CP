from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


id = "17931401448-h6puvcair4l6roodiataefaaq40e988o@developer.gserviceaccount.com"
key = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC71OYGoHqotDYi\n/rsbmcezTOziRXsehX1ymUuvVcXaGQCbWtRtHlk9MHTIpqB4Vkj7Kn6o0X83zRSJ\nED/DeMZ7+iW00inGpIzzSI28avKJhRXpfxu47gZS3RZ6zwA2ZgK+f/YZvKHbokds\n7pIcegRNxFDSDoxQCAIgC76ZFoYhS3SNS6+u4uZ+3/13RYPkRO7+GW1yzYUwx+Vh\nQlN4aWXHT+h3UEN160nIQZedXH0q98s6/GEmqkgXZAL3QyTtd412MS/ULS9gSk1T\nCHO1ARXopTKxxhP+UpnqXo4EJaeYPCaCk8YHebjPFVqlbKUecloIbfh99rTsU/7A\nYDYzzSLxAgMBAAECggEAQP5A/egHqVp6JQ/JhJpojHVAvmbWXFBKgR3kH25pgLcI\nC7mZKYzHyjF7J3bordsFc8tXemjLQW63/VlfBu9CluGOrIvQIskLcJ8ZVCoZdFZV\np67w08Og8olH3wTDiQ8xQeObL3qi8xGq71l5u1rJJHOal6SrDoJG4fnOYMB3dwtB\nT2aRh0/6dCJo6vTn4jEOQNf4aGEaHIWVmjV2WtnF2Bnkqf1xWIHu71Of/Kutr2Mw\nC24YYahSMXRan/mtucqLiq87p1iQHkmsHleVCZsWama/+MLogEnXLPFsaiPzj5pq\nei0lAD/Cu4vuHvtyjib/d7UsEqNuB4IyuIRhmRV7QQKBgQD0HRrWNNht7T9yQ8mR\nQQRoztDjdN+ITGuj9MkRgI7DxtUu5TuzDTHGySd8K7hgP8mQZXqf3/trORQ96jos\nwnUPlYfNt1QlDLzp90++7OmucDVH2vz6xn4y1rtm+RxqhDxKjZRvu7j99g7QWLv/\nrGja4ZsGv/kj3ndRENoaL6ePWQKBgQDE+jvVoOcyEWWxmiAgB5EINlM89pvPVYB6\n//O5sgql9FXeecBbGmYMHuWNsj2GrEqJpYnXC0XGgeqeoX4sxPFuKSaS+eIoFfZH\n2M6DHop71IrCIA1k0W9TxmcXVXLoH1KSlVPg0YTAdHS2isL8Gqd6lTv08Ga/7TkZ\nQu8hItoVWQKBgGEe+0BiAgGqNGXnplhN/80bC2yTYSO/E8xFZYG7HhGyF7rypM/V\n3gnyme0DD/XrKuxyE1lsKYE9UlpXyBFqxFwQ59jmqWmcKcUECgwyAb7PEcOm0qOL\nOUZMvH55ed6/AaW/smDJ1Q3lSXuG8jUEiSscOytyUVL9/YaZJ8znTMjxAoGAKrvH\nA1+3CKuxjkhLs+cwVcHDaTRvNRntl8GzlJPFr59EidGMI7ekb/i8AHOs2WzDdv1M\n3DR73McOqX+LqhbH8ghHcBd6MwwgtBGbK+MSVC8WM2tUvIybRGeEshE9rpItDdQL\nsHiD/mTFdVzBVIRL1VJPAaKuB/FlM8/LpTq0aXECgYBI0yMKPJ19FCztpSlp9gvq\nUSDTCZgvjfXSSbT5Qieu/ewrCtfC9R5DehGCNARqcuma1BhoimL8gIEoIQSOl82p\niZxrdcDqv0WNkwGEFlEF/4kLFMQvRiiWWXwEUVNEtiBMwn9KPGMal7td0PmS5L8U\nVK/lt6McBxoUgQFMZdvhTA\u003d\u003d\n-----END PRIVATE KEY-----\n"
#print gauth.GetAuthUrl()

credentials = SignedJwtAssertionCredentials(id, key, scope='https://www.googleapis.com/auth/drive')
credentials.authorize(httplib2.Http())

gauth = GoogleAuth()
gauth.credentials = credentials

drive = GoogleDrive(gauth)
fileName = "logs/logs-298yhjhboihnt.csv"
fh = open(fileName, "r")
l = fh.read()
file1 = drive.CreateFile({'title': 'BackUp1.txt'})
file1.SetContentString(l)
file1.Upload()
