# Sergiy Radyakin, The World Bank, 2021
import datetime, json, uuid, re


def getguid():
    return str(uuid.uuid4())


def getqx(varname):
    # Proto for questionnaire document
    X = {}
    X['Revision']=0
    X['Children']=[]
    X['IsRoster']=False
    X['DisplayMode']=0
    X['RosterSizeSource']=0
    X['FixedRosterTitles']=[]
    X['LastEventSequence']=0
    X['IsUsingExpressionStorage']=False
    X['CustomRosterTitle']=False
    X['IsCoverPageSupported']=False
    X['CoverPageSectionId']="c46ee895-0e6e-4063-8136-31e6bfa7c3f8"
    X['Id']=getguid()
    X['PublicKey']=getguid()
    X['Title']=varname
    X['Description']=varname
    X['VariableName']=varname
    dt=datetime.datetime.utcnow().isoformat()
    X['CreationDate']=dt
    X['LastEntryDate']=dt
    X['IsDeleted']=False
    X['CreatedBy']="44444444-4444-4444-4444-444444444444"
    X['IsPublic']=False
    X['Macros']={}
    X['LookupTables']={}
    X['Attachments']=[]
    X['Translations']=[]
    X['Categories']=[]
    X['ConditionExpression']=""
    X['HideIfDisabled']=False
    return X


def getgroup(title):
    # Proto for group (section, subsection)
    G={}
    G['$type']='Group'
    G['ConditionExpression']=""
    G['HideIfDisabled']=False
    G['IsFlatMode']=False
    G['IsPlainMode']=False
    G['DisplayMode']=0
    G['Enabled']=True
    G['Description']=""
    G['VariableName']=""
    G['IsRoster']=False
    G['CustomRosterTitle']=False
    G['RosterSizeSource']=0
    G['FixedRosterTitles']=[]
    G['PublicKey']=getguid()
    G['Title']=title
    return G


def getbasequestion(typ,vname,qtext,hint):
    # Proto for a question (generic)
    # // todo: validate variable name. Replace to something valid if starts with an underscore, etc.
    if (hint==None):
        hint=""
    Q={}
    Q['$type']="UnknownQuestion"
    Q['Answers']=[]
    Q['Children']=[]
    Q['ConditionExpression']=""
    Q['HideIfDisabled']=False
    Q['Featured']=False
    Q['Instructions']=hint
    Q['Properties']={'HideInstructions':False,'UseFormatting':False,'OptionsFilterExpression': ""}
    Q['PublicKey']=getguid()
    Q['QuestionScope']=0 #// 0=Interviewer; 1=Supervisor; 3=Hidden;
    Q['QuestionText']=qtext
    Q['QuestionType']=-999
    Q['StataExportCaption']=vname
    Q['VariableLabel']=""
    Q['IsTimestamp']= False
    Q['ValidationConditions']=[]
    Q['VariableName']=vname
    return Q


def getquestion(kobo):
    # Proto for a question (specific)
    Q=getbasequestion("Z",kobo['name'],kobo['text'],kobo['hint'])
    if (kobo['type1']=="text"):
      # Free text response
      Q['$type']="TextQuestion"
      Q['QuestionType']=7 # // TextQuestion
    if (kobo['type1']=="integer"):
      # Integer (i.e., whole number) input.
      Q['$type']="NumericQuestion"
      Q['QuestionType']=4
      Q['IsInteger']=True
      Q['UseFormatting']=True #//perhaps this is thousands delimiter?
      Q['Order']=2            #// unknown, suspected ineffective
    if (kobo['type1']=="decimal"):
      # Decimal input.
      Q['$type']="NumericQuestion"
      Q['QuestionType']=4
      Q['IsInteger']=False
      Q['UseFormatting']=False #//perhaps this is thousands delimiter?
      Q['Order']=2             #// unknown, suspected ineffective
    if (kobo['type1']=="select_one"):
      # Multiple choice question; only one answer can be selected.
      Q['$type']="SingleQuestion"
      Q['QuestionType']=0
      Q['ShowAsList']=False
      Q['IsFilteredCombobox']=False
    if (kobo['type1']=="select_multiple"):
      # Multiple choice question; multiple answers can be selected.
      Q['$type']="MultyOptionsQuestion"
      Q['QuestionType']=3
      Q['AreAnswersOrdered']=False
      Q['YesNoView']=False
    if (kobo['type1']=="date"):
      # Date input.
      Q['$type']="DateTimeQuestion"
      Q['QuestionType']=5
    if (kobo['type1']=="image"):
      # Take a picture or upload an image file.
      tokens=kobo['appearance'].split(" ")
      Q['$type']="MultimediaQuestion"
      Q['QuestionType']=11
      Q['IsSignature']="signature" in tokens

    return Q


def gettext(title):
    # Proto for a static text
    T={}
    T['$type']="StaticText"
    T['Children']=[]
    T['VariableName']=""
    T['PublicKey']=getguid()
    T['Text']=title
    T['AttachmentName']=""
    T['ValidationConditions']=[]
    T['ConditionExpression']=""
    T['HideIfDisabled']=False
    return T


def removeCRLF(s):
    s=s.strip()
    result=s.replace("\r"," ")
    result=result.replace("\n"," ")
    g=result.replace("  "," ")
    while (g!=result.replace("  "," ")):
       g=result.replace("  "," ")
    return g

def adaptsubst(s):
    # Use regular expressions to locate and adapt the substitution placeholders.
    # Anything resembling ${something} will be replaced with %something%
    s=removeCRLF(s)
    result = re.findall('\$\{.*?\}', s)
    for t in result:
        s=s.replace(t,"%"+t[2:-1]+"%")
    if (len(s)>500):
        print("!!! WARNING, CONTENT TRUNCATED !!!")
        s=s[0:499]
        # todo: make truncation aware of substitution, not to expose
        #       substitution placeholder carelessly if it falls on the boundary.
    return s


#  END OF FILE
