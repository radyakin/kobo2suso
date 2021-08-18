# Sergiy Radyakin, The World Bank, 2021

import susoqx, json
from openpyxl import load_workbook

global i
i=1

def processgroup(ws, name, title):
  global i
  G=susoqx.getgroup(title) # // todo: must also pass name
  C=[]

  empty=0
  while (empty<2):
    koboType=ws.cell(column=3,row=i).value
    koboName=ws.cell(column=4,row=i).value
    koboText=ws.cell(column=5,row=i).value
    koboHint=ws.cell(column=6,row=i).value

    i=i+1

    if (koboText==None):
      koboText=""

    koboText=susoqx.adaptsubst(koboText)

    if (koboType==None):
      if (empty==1):
        break
      else:
        empty=empty+1
    else:
      empty=0

      koboType1=koboType.split()[0]
      print(koboType1 + "       " + koboName + "      " + koboText)
      # // note => StaticText
      # // begin_group => SubSection
      # // text => TextQuestion
      # // integer =>
      # // select_one =>
      # // calculate =>
      # // today, start, end, deviceid << system variables
      if (koboType1=="end_group"):
        break # // end of current group

      if (koboType1=="begin_group"):
        # // encountered a nested group
        print(koboName)
        Z=processgroup(ws, koboName, koboText)
        C.append(Z)

      if (koboType1=="note"):
        # // note maps to static text
        T=susoqx.gettext(koboText)
        C.append(T)
      if (koboType1 in ["text","integer","select_one"]):
        # // text maps to TextQuestion
        C.append(susoqx.getquestion(koboType1,koboName,koboText,koboHint))
      if (not(koboType1 in ["end_group", "begin_group", "note", "text", "integer", "select_one"])):
        print("Encountered an unknown type: "+koboType1+", skipping")

  G['Children']=C
  return G

def koboConvert(koboname, susoname):
  global i
  print(filename)
  wb = load_workbook(filename = koboname)
  ws = wb.active
  print(ws.title)
  i=1
  if (ws.cell(column=3,row=i).value!="type"):
    print(">>> ERROR")
    return
  print(">>> OK")
  i=i+1

  data=susoqx.getqx("Q")
  G=processgroup(ws, "Main", "MAIN")
  data['Children'].append(G)

  with open(susoname, 'w') as outfile:
    json.dump(data, outfile, indent=2)
  # todo: pack into a zip-archive

  # END OF FILE
