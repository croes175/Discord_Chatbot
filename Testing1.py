# bot.py
from multiprocessing.sharedctypes import Value
import os
from re import A

import discord
from dotenv import load_dotenv
import asyncio
import datetime

load_dotenv()
TOKEN ="OTkwMDg0MTIxMTQ3NjE3MzMw.GqJ1ii.1SALOteGkRKSnYreIkGAIAMZj2YVaRcNu8a9KQ"
Guild="Bot_Testing"
print(TOKEN, "Token")


class chat_bot(discord.Client):

    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)

        self.USER_REQUEST={}

  
# on message method
    async def on_message(self,message):

           a=self.USER_REQUEST
 
           
           if message.author == client.user:
                print(message.author)
                print(dir(message))
                return
    
           messa=message.content.lower()
           print(message.author)

           if client.user in message.mentions :
                
                if  (message.author not in a.keys() ) and "hello" in messa:

                    a[message.author]=False
                    print(a)
                    self.USER_REQUEST=a
                    await message.channel.send("Hello "+str(message.author))


                elif "time" in messa:

                    
                    Value=messa.find(":")
                    s=messa[Value+1:]

                    print(s)
                    Value=int(s)
                    task1 = asyncio.create_task(self.say_after(Value,message))
                    await message.channel.send("Start Rest "+s)

                    await task1
                elif "close" in messa:
                    a[message.author]=True
                    self.USER_REQUEST=a

  
    async def say_after(self,delay,message):

        a=self.USER_REQUEST



        loop=asyncio.get_running_loop()
        end_time=loop.time()+delay
        while True:
            print("estoy esperando")
            print(self.USER_REQUEST)

            

            if (loop.time()>end_time):
                await message.channel.send("Rest is finished")
                break
            elif(self.USER_REQUEST[message.author]):
                await message.channel.send("Close Rest")
                break
        
       
            await asyncio.sleep(1)            
        del self.USER_REQUEST[message.author]  
    
 #on ready method   
    async def on_ready(self):
      for guild in client.guilds:
        if guild.name == Guild:
            break

      print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        )
        

    




if __name__ == '__main__':

    client = chat_bot()  

    client.run(TOKEN)