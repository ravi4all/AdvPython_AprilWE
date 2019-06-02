import cgi

form = cgi.FieldStorage()
username = form.getvalue('u_name')
useremail = form.getvalue('u_mail')
userpwd = form.getvalue('u_pwd')
usergender = form.getvalue('gender')
usercity = form.getvalue('usercity')

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
    <h1>Registered Successfully...</h1>
    <h4>Name : {}</h4>
    <h4>Email : {}</h4>
    <h4>City : {}</h4>
</body>
</html>
""".format(username, useremail, usercity))