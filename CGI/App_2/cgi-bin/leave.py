import cgi

form = cgi.FieldStorage()
empname = form.getvalue('e_name')
empemail = form.getvalue('e_mail')
leaveFrom = form.getvalue('e_from')
leaveTo = form.getvalue('e_to')
leaveType = form.getvalue('leave')
leaveReason = form.getvalue('reason')

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
    
    <h1>Leave Applied Successfully...</h1>
    <h4>Name : {}</h4>
</body>
</html>
""".format(empname))