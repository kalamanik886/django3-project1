import pandas as pd
import smtplib
import ssl

#importing the csv file & sorting according to leader's cgpa
#if duplicates found in leader's cgpa then look through co leader's cgpa
df = pd.read_csv("studentdata.csv")
df.sort_values(by=['leader_cgpa', 'co_leader_cgpa'], ascending = False, inplace = True)

#assigning all the choices of each student in different lists (f_choice1 to f_choice9)

for i in range(0, 10):
    globals()['f_choice%s' % i] = list(df.iloc[i])
    globals()['f_choice%s' % i] = globals()['f_choice%s' % i][7:]

#look through the choice list in descending order and remove the duplicates

j=0
for i in range(j,10):
    j+=1
    for k in range(j, 10):
        globals()['f_choice%s' % k].remove(globals()['f_choice%s' % i][0])


contact = list(df['contact_mail'])
leader = list(df['leader_name'])

#one choice for every student

final = {}
for i in range(0,10):
    final.update({leader[i]: globals()["f_choice%s" %i][0]})

#final message

final_message = []
for i,j in final.items():
    final_message.append(f"{i} got '{j}' as your thesis subject.")

#sending email to each students their result

sender_email = "ucchash886@gmail.com"
password = input(str("Please enter your password : "))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")

for i in range(0, len(contact)):
    server.sendmail(sender_email, contact[i], final_message[i])
print("Message sent")