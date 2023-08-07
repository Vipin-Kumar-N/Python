import email


contacts = {
    "number" : 4,
    'students' :
        [
            {'name' : 'Vipin' , 'email' : 'email1@email.com'},
            {'name' : 'Vk', 'email' : 'email2@email.com'},
            {'name' : 'Vp', 'email' : 'email3@email.com'},
            {'name' : 'Vi', 'email' : 'email4@email.com'}
        ]
}

print("Students email : ")
for student in contacts['students']:
    print(student['email'])
