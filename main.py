import sqlite3
conn=sqlite3.connect('student_database.db')
c=conn.cursor()

print '################################################################\nSTUDENT PROFILE APPLICATIONS\n################################################################'

def insert_data():
    rollno=int(input('enter the rollno'))
    name=raw_input('enter the name')
    dept=raw_input('enter the dept')
    age=int(input('enter the age'))
    gender=raw_input('enter the gender M or F')
    eme=int(input('enter the eme suject mark'))
    npm=int(input('enter the npm suject mark'))
    cd=int(input('enter the cd suject mark'))
    gmm=int(input('enter the gmm suject mark'))
    dmdw=int(input('enter the dmdw suject mark'))
    pt=int(input('enter the pt suject mark'))
    c.execute("insert into student_details VALUES(?,?,?,?,?)",(rollno,name,dept,age,gender))
    total=eme+npm+cd+gmm+dmdw+pt;
    avg=total/6
    if((eme >=50) & (npm >=50) & (cd >=50) & (gmm>=50) & (dmdw>=50) & (pt>=50)):
        if(avg >=90):
            grade='S'
        elif((avg >=80) & (avg <90)):
            grade='A'
        elif((avg >=70) & (avg <80)):
            grade='B'
        elif((avg >=60) & (avg <70)):
            grade='C'
        else:
            grade='D'
    else:
        grade='F'
    c.execute("INSERT INTO student_academics VALUES(?,?,?,?,?,?,?,?,?,?)",(rollno,eme,npm,cd,gmm,dmdw,pt,total,avg,grade))
    if c>0:
        print 'Data Inserted Successfully'
    conn.commit()

def sub_count():
    passcount=0
    failcount=0
    std_count=0
    counts=conn.execute("select rollno from student_academics")
    for c in counts:
        std_count=std_count+1
    print("the student count =%d"%std_count)
    sub=raw_input("enter the subject to get the fail and pass count...:")
    print(sub)
    if(sub=='eme'):
        cursor=conn.execute("select eme from student_academics")
        for row in cursor.fetchall():
            mark=row[0]
            if(mark>=50):
                passcount=passcount+1
            else:
                failcount=failcount+1
        pass_percent=(float(passcount)/float(std_count))*100
        fail_percent=(float(failcount)/float(std_count))*100
    elif(sub=='npm'):
        cursor=conn.execute("select npm from student_academics")
        for row in cursor:
            mark=row[0]
            if(mark>=50):
                passcount=passcount+1
            else:
                failcount=failcount+1
        pass_percent=(float(passcount)/float(std_count))*100
        fail_percent=(float(failcount)/float(std_count))*100
    elif(sub=='cd'):
        cursor=conn.execute("select cd from student_academics")
        for row in cursor:
            mark=row[0]
            if(mark>=50):
                passcount=passcount+1
            else:
                failcount=failcount+1
        pass_percent=(float(passcount)/float(std_count))*100
        fail_percent=(float(failcount)/float(std_count))*100
    elif(sub=='gmm'):
        cursor=conn.execute("select gmm from student_academics")
        for row in cursor:
            mark=row[0]
            if(mark>=50):
                passcount=passcount+1
            else:
                failcount=failcount+1
        pass_percent=(float(passcount)/float(std_count))*100
        fail_percent=(float(failcount)/float(std_count))*100
    elif(sub=='dmdw'):
        cursor=conn.execute("select dmdw from student_academics")
        for row in cursor:
            mark=row[0]
            if(mark>=50):
                passcount=passcount+1
            else:
                failcount=failcount+1
        pass_percent=(float(passcount)/float(std_count))*100
        fail_percent=(float(failcount)/float(std_count))*100
    elif(sub=='pt'):
        cursor=conn.execute("select pt from student_academics")
        for row in cursor:
            mark=row[0]
            if(mark>=50):
                passcount=passcount+1
            else:
                failcount=failcount+1
        pass_percent=(float(passcount)/float(std_count))*100
        fail_percent=(float(failcount)/float(std_count))*100
    else:
        print("subject not found....")
    print ('pass count=%d'%passcount)
    print ('pass percentage=%.2f'%pass_percent)
    print("fail count=%d"%failcount)
    print("fail percentage=%.2f"%fail_percent)
    
def class_percent():
    passcount=0
    failcount=0
    std_count=0
    
    counts=conn.execute("select rollno from student_academics")
    for c in counts:
        std_count=std_count+1
    print("the student count =%d"%std_count)
    cursor=conn.execute("select grade from student_academics")
    for c in cursor:
        if(c[0]=='F'):
            failcount=failcount+1
        else:
            passcount=passcount+1
    pass_percentage=(float(passcount)/float(std_count))*100
    fail_percentage=(float(failcount)/float(std_count))*100
    print ('no of student passed=%d'% passcount)
    print ('pass percentage=%.2f'%pass_percentage)
    print("no of student failed=%d"%failcount)
    print("fail percentage=%f"%fail_percentage)

def disp():
    '''c.execute('SELECT * FROM student_academics FULL OUTER JOIN student_details ON student_academics.rollno = student_details.rollno')'''
    c.execute('select * from  student_details  natural join student_academics ')
    print("Rollno \t name \t\t dept \t age \t gender \t eme \t npm \t cd \t gmm \t dmdw \t pt \t total \t avg \t\t grade")
    for row in c.fetchall():
        rollno=row[0]
        name=row[1]
        dept=row[2]
        age=row[3]
        gender=row[4]
        eme =row[5]
        npm=row[6]
        cd=row[7]
        gmm=row[8]
        dmdw=row[9]
        pt=row[10]
        total=row[11]
        avg=row[12]
        grade=row[13]
        print("%d \t %s\t \t %s \t %d \t %s \t \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %f \t %s"%(rollno,name,dept,age,gender,eme,npm,cd,gmm,dmdw,pt,total,avg,grade))


def display_by_rollno():
    r=int(input('enter the rollno to display the student details'))
    sql= "select * from student_details  join student_academics using (rollno)"
    c.execute(sql)
    results = c.fetchall()
    try:
        for row in results:
            if(row[0]==r):
                rollno=row[0]
                name=row[1]
                dept=row[2]
                age=row[3]
                gender=row[4]
                eme =row[5]
                npm=row[6]
                cd=row[7]
                gmm=row[8]
                dmdw=row[9]
                pt=row[10]
                total=row[11]
                avg=row[12]
                grade=row[13]
                print("Rollno\tname\tdept\tage\tgender\teme\tnpm\tcd\tgmm\tdmdw\tpt\ttotal\tavg\tgrade")
                print("%d\t%s\t%s\t%d\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%.2f \t%s"%(rollno,name,dept,age,gender,eme,npm,cd,gmm,dmdw,pt,total,avg,grade))
    except:
       print("Error unable to fetch the data")
        
def grade_disp():
    grade1=raw_input("enter the grade to get the list of students")
    c.execute("select * from student_details JOIN student_academics using(rollno)")
    print("Rollno \t name \t\t dept \t age \t gender \t eme \t npm \t cd \t gmm \t dmdw \t pt \t total \t avg \t grade")
    for row in c.fetchall():
        grade2=row[13]
        if((grade1=='A') & (grade2=='A')):
            c.execute("select * from student_details JOIN student_academics using(rollno)")
            print("%d \t %s\t \t %s \t %d \t %s \t \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %.2f \t %s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
        elif((grade1=='B') & (grade2=='B')):
            c.execute("select * from student_details JOIN student_academics using(rollno)")
            print("%d \t %s\t \t %s \t %d \t %s \t \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %.2f \t %s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
        elif((grade1=='C') & (grade2=='C')):
            c.execute("select * from student_details JOIN student_academics using(rollno)")
            print("%d \t %s\t \t %s \t %d \t %s \t \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %.2f \t %s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])) 
        elif((grade1=='D') & (grade2=='D')):
            c.execute("select * from student_details JOIN student_academics using(rollno)")
            print("%d \t %s\t \t %s \t %d \t %s \t \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %.2f \t %s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])) 
        elif((grade1=='F') & (grade2=='F')):
            c.execute("select * from student_details JOIN student_academics using(rollno)")
            print("%d \t %s\t \t %s \t %d \t %s \t \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %.2f \t %s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))    

def main_prg():
    opt=0
    dispch=0
    while (opt != 3):
        print '1)Insert\t2)Display\t3)Exit'
        opt=input('Enter your choice =>')
        dispch=0
        if opt==1:
            insert_data()
        elif opt==2:
            print '################################################################'
            print '1)Whole_class\t2)Individual_subjects\t3)Individual_students\t4)Total_Display\t5)W.R.To_Grade\t6)Exit'
            dispch=input('Enter your choice-->')
            if dispch==1:
                print '################################################################'
                class_percent()
            elif dispch==2:
                print '################################################################'
                sub_count()
            elif dispch==3:
                print '################################################################'
                display_by_rollno()
            elif dispch==4:
                print '################################################################'
                disp()
            elif dispch==5:
                print '################################################################'
                grade_disp()
            elif dispch==6:
                break
        elif opt==3:
            break
        print '################################################################'
    
    
main_prg()
