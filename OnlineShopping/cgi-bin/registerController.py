import model
import cgi

form = cgi.FieldStorage()
name= form.getvalue('u_name')
email = form.getvalue('u_mail')
pwd = form.getvalue('u_pwd')
phno = form.getvalue('phno')
# pic = form.getvalue('u_pic')
pic = form['u_pic']

model.registerUser(name,email,pwd,phno,pic)

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
<h1>Registered Successfully...</h1>
</body>
</html>
""")
