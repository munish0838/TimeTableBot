import discord 
import os

'''def commands() :
  noob=discord.Embed(title='COMMANDS', description="Here is the  list of all commands for the bot", color=discord.Color.red())
  
  noob.add_field(name='.list commands',value ='Lists all commands of the bot',inline = False)

  noob.add_field(name='.today',value='Shows the class schedule for current day',inline=False)

  noob.add_field(name='.tom',value='Shows the class schedule for next day',inline=False)

  noob.add_field(name='CLASS SCHEDULE',value = '.monday\n.tuesday\n.wednesday\n.thursday\n.friday\n',inline = False)
  
  noob.add_field(name='.subjects',value='shows list of subjects in current sem',inline=False)

  noob.add_field(name='.classroom',value='Displays GCR codes for all subjects',inline=False)
  return noob




def classroom() :

  noob=discord.Embed(title='GCR CODES', description="GCR codes for all subjects", color=discord.Color.blue())

  noob.add_field(name=" MA1301-Mathematics 3 ", value="h77rojr",inline=False)

  noob.add_field(name="  Ethics ", value="b23766c",inline=False)

  noob.add_field(name='HS1101',value='HS 1101- CSE L ( SID 1 to 62) = okvejrn\nHS 1101-CSE L (SID 63 onwards) = svj5gnt',inline = False)

  noob.add_field(name='PHYSICS EMT and QM',value = 'f4rm5zx',inline=False)
  
  noob.add_field(name='HSS1101 Practicals',value='CSE1: 20103001-3020   **fk4mhbl**\n CSE2:3021-3040   **ptmp45d**\n CSE3: 3041-3060   **gt2tr3y**\n CSE4: 3061-3080 **qi4pbxs**\n CSE5: 3081-3100   **hla4muv**\n CSE6: 3101-3124   **dbbwn52**',inline = False)

  noob.add_field(name='Intro to Manufacturing    ES1501',value = 'For SID 1-100 : 3gjt4kb',inline= False)

  noob.add_field(name='Intro to Electronic and Electrical Engineering   ES1401',value = '*diueglo*')
  
  noob.add_field(name='Maths Tutorial',value = 'nfsjpnq-CS4,5,6\n stta4oo CS1,2,3',inline = False)
  
  return noob'''






def monday() :

  noob=discord.Embed(title='MONDAY', description="Class schedule ", color=discord.Color.green())

  
  noob.add_field(name='10:00 AM - 11:00 AM  CS1302 (CAO)',value = 'Comp Arch and Org NPTEL Lecture',inline = False)

  noob.add_field(name='11:00 AM - 12:00 AM   ',value='Open elective Lecture',inline = False)

  noob.add_field(name="2:00 PM - 3:00 PM CS1301 (DS)", value="DSA lecture ",inline=False) 
  
  noob.add_field(name='3:00 PM - 4:00 PM   CS1303 (DSCS)',value='Discrete Structures Lecture',inline = False)

  return noob






def tuesday() :

  noob=discord.Embed(title='TUESDAY', description="Class schedule", color=discord.Color.blue())

  noob.add_field(name='9:00 AM - 10:00 AM   ES1701',value ='AI and ML Lecture',inline = False)

  noob.add_field(name='12 Noon - 1:00 PM   CS1303 (DSCS)',value='Discrete Structures Lecture',inline = False)
  
  noob.add_field(name = '2:00 PM - 4:00 PM   ES701 LAB',value = 'AI and ML lab',inline = False)

  return noob






def wednesday() :

  noob=discord.Embed(title='WEDNESDAY', description="Class schedule ", color=discord.Color.green())

  noob.add_field(name='9:00 AM - 10:00 AM CAO',value = 'NPTEL Lecture Comp Arch and Org',inline = False)


  noob.add_field(name='11:00 AM - 12:00 AM   ',value='Open elective Lecture',inline = False)

  noob.add_field(name='12 Noon - 1:00 PM   CS1303 (DSCS)',value='Discrete Structures Lecture',inline = False)

  noob.add_field(name='3:00 PM - 5:00 PM   DS LAB',value = 'Data Structure Lab',inline = False)

  
  return noob  






def thursday() :

  noob=discord.Embed(title='THURSDAY', description="Class schedule ", color=discord.Color.green())

  noob.add_field(name='9:00 AM - 10:00 AM   ES1701',value ='AI and ML Lecture',inline = False)
   
  noob.add_field(name='10:00 AM - 11:00 AM  CS1302 (CAO)',value = 'Comp Arch and Org NPTEL Lecture',inline = False)

  noob.add_field(name='11:00 AM - 12:00 AM Tutorial  ',value='Open elective Tutorial Class',inline = False)

  noob.add_field(name = '12:00 PM - 1:00 PM DSCS',value = 'discrete Strcutures Tutorial Class',inline = False)

  noob.add_field(name = '2:00 PM - 3:00 PM   DS',value = 'Data structures Lecture',inline = False)

  noob.add_field(name = '3:00 PM - 5:00 PM   CAO ',value = 'Lab for Comp Arch and Org',inline = False)

  return noob 



def friday() :

  noob=discord.Embed(title='FRIDAY', description="Class schedule ", color=discord.Color.green())

  noob.add_field(name='11:00 AM - 12:00 AM   ',value='Open elective Lecture',inline = False)
  
  noob.add_field(name = '2:00 PM - 3:00 PM   DS',value = 'Data structures Lecture',inline = False)
  return noob 
