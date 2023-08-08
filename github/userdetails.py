import requests

class userdetails:

    def getUserDetailsFromGit(self,username):
        # print("Check is User ",username," exist")

        username = username
        access_token="Your Personal Access Token"

        headers={"Authorization": f"Bearer {access_token}"}
        response_url="https:://api.github.com/users/{username}/repos"

        response=requests.get(repos_url,headers=headers)
        count=0
        if response.status_code==200:
            repos=response.json()
            print("Repositories for ",username)
            for repo in repos:
                count=count+1
        print("User ",username," "+userdetails.findUser(username))
        print("He have total ",count," followers")


    def findUser(username):

        url="connection String"

        if username == "vivekkumar":
            return "exist"
        return "Not_Exist" 

user=userdetails()
userinput = input("Enter User Name : ")
user.getUserDetailsFromGit(userinput)

    