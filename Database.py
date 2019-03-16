import glob
import os

import pymongo

class Insert:
    def __init__(self, server, port, dbname):
        conn = pymongo.MongoClient(server, port)
        self.db = conn.get_database(dbname)

    def admin(self, id, username, password):
        try:
            self.db.admin.insert(
                {"id": int(id), "username": str(username), "password": str(password)})
        except Exception as e:
            print("Error !! {0}".format(e))

    def personal(self, id, fname, lname, job, address, age,gender, email, registime,picprofile):
        try:
            self.db.personal.insert(
                {"id": int(id), "fname": str(fname),
                 "lname": str(lname), "job": str(job),
                 "address": str(address), "age": age,"gender":str(gender),
                 "email": str(email), "registime": str(registime),"picprofile":str(picprofile)})

        except Exception as e:
            print("Error !! {0}".format(e))

    def timestamp(self, id, count, datetime):
        try:
            self.db.timestamp.insert(
                {"id": int(id), "count": count, "datetime": str(datetime)})
        except Exception as e:
            print("Error !! {0}".format(e))

    def img(self, name, id, n, ex, image):
        try:
            self.db.img.insert(
                {"name": str(name), "id": int(id), "n": int(n), "ex": str(ex), "image": str(image)})
        except Exception as e:
            print("Error !! {0}".format(e))



class Find:
    def __init__(self, server, port, dbname):
        conn = pymongo.MongoClient(server, port)
        self.db = conn.get_database(dbname)

    # FIND LOGIN BY ADMIN TRUE ID
    def admin(self,username,password):
        cursor = self.db.admin.find({"username":username,"password":password})
        for i in cursor:
            #print(i['id'],i['username'],i['password'])
            return i['id']

    def admin_exist(self,id):
        cursor = self.db.admin.find({"id":int(id)})
        for i in cursor:
            return i['id']

    def personals(self):
        list = []
        cursor = self.db.personal.find()
        for i in cursor:
             list.append([i['id'], i['fname'], i['lname'], i['job'], i['address'], i['age'], i['gender'], i['email'], i['registime']])
        return list;

    #FIND INFOMATION PERSONAL BY ID
    def personal(self,id):
        cursor = self.db.personal.find({"id":int(id)})
        for i in cursor:
            return i['id'], i['fname'], i['lname'], i['job'], i['address'], i['age'],i['gender'], i['email'], i['registime']

    #FIND LOGIN LOG TIME BY ID
    def timestamp(self,id):
        arr =[]
        cursor = self.db.timestamp.find({"id":int(id)})
        for i in cursor:
            arr.append(str(i['id']) +' '+str(i['count'])+' '+i['datetime'])

        return arr

    def img(self,id):
        list = []
        cursor = self.db.img.find({"id": int(id)})
        for i in cursor:
            result = i['name'], i['id'], i['n'], i['ex'], i['image']
            print(result)
            list.append(result)

    def lastID(self):
        id = 0
        cursor = self.db.personal.find().sort([('id', -1)]).limit(1)
        for i in cursor:id =i['id']
        if id:return id
        else:return str(0)

    def lastIDTime(self,pid):
        id = 0
        #cursor = self.db.timestamp.find().sort([('count', -1)]).limit(1)
        cursor = self.db.timestamp.find({"id":pid}).sort([('count',-1)]).limit(1)
        for i in cursor:
            id = i['count']
        if id:
            return id
        else:
            return 0


class Update:
    def __init__(self, server, port, dbname):
        conn = pymongo.MongoClient(server, port)
        self.db = conn.get_database(dbname)

    def updateMobile(self,id):
        res = self.db.Products.update_many({"id": int(id)}, {"$set": {"pprice": 50000, "psize": 9}})
        print("Match {0} Modify {1}".format(res.matched_count, res.modified_count))

    def personal(self, id, fname, lname, job, address, age, gender, email):
        try:
            self.db.personal.update_many(
                {"id": int(id)}, {"$set":{"fname": str(fname),
                 "lname": str(lname), "job": str(job),
                 "address": str(address), "age": age, "gender": str(gender),
                 "email": str(email)}})

        except Exception as e:
            print("Error !! {0}".format(e))


class Delete:
    def __init__(self, server, port, dbname):
        conn = pymongo.MongoClient(server, port)
        self.db = conn.get_database(dbname)

    def admin(self,id):
        self.db.admin.remove({"id": int(id)})

    def personal(self, id):
        self.db.personal.remove({"id": int(id)})

    def timestamp(self,id):
        self.db.timestamp.remove({"id": int(id)})

    def deletepic(self,id):
        for filename in glob.glob("dataset/User."+str(id)+".*"):
            os.remove(filename)

    def delAllById(self,id):
        self.admin(id)
        self.personal(id)
        self.timestamp(id)
        self.deletepic(id)


if __name__ == '__main__':
    find = Find("localhost", 27017, 'Facial_RecogDB')
    find.lastIDTime(1)

