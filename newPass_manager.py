class PasswordManager:
    def __init__(self):
        self.key=None
        self.password_file=None
        self.password_dict={}
    
    def create_pw_file(self,path, initial_values=None):
        self.password_file=path

        if initial_values is not None:
            for key,value in initial_values.items():
                self.add_pw(key, value)

    def load_password_file(self,path):
        self.password_file=path
    
        with open(path, 'r') as f:
            for line in f:
                site, pw=line.split(":")
                self.password_dict[site]=pw
            
    def add_pw(self,site, password):
        self.password_dict[site]=password

        if self.password_file is not None:
            with open(self.password_file,'a+')as f:
                f.write(site+":"+password+"\n")


    def get_pw(self,site):
        return self.password_dict[site]
    
    def printAllPw(self):
        if self.password_dict is not None:
            for site in self.password_dict:
                print(site,":",self.password_dict[site])

    def deletepw(self,site):
        del self.password_dict[site]
        if self.password_file is not None:
            with open(self.password_file,'w')as f:
                for site in self.password_dict:
                    password=self.password_dict[site]
                    f.write(site+":"+password+"\n")
    
def main():
    password={
        'google': '123',
        'fb':'123'
             }
    pm=PasswordManager()

    print("""Choose operation:
        1 New password file
        2 Load password file
        3 Add new password
        4 Get a password
        5 Print all passwords
        6 Delete a password
        q quit
        """)

    done=False

    while not done:
        choice=input("Enter your choice:")
        match choice:
            case '1':
                path=input("path:")
                pm.create_pw_file(path,password)
            case '2':
                path=input("path:")
                pm.load_password_file(path)
            case '3':
                site=input("site:")
                password=input("Password:")
                pm.add_pw(site, password)
            case '4':
                site=input("site:")
                pw=pm.get_pw(site)
                print("The password of ",site, " is ", pw)
            case '5':
                pm.printAllPw()
            case '6':
                site=input("site:")
                pm.deletepw(site)
            case 'q':
                done=True
                print("Done")
            case _:
                print("Invalid option")

if __name__=="__main__":
    main()
