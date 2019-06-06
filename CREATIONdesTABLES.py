#%ALTER SESSION SET NLS_DATE_FORMAT = "DD MM SYYYY")
#-- SYYYY means 4-digit-year, S prefixes BC years with "-"
##########################################
####### 41 tables + 6 qui posent problème 
##########################################
import sqlite3
# Etablissement de la connexion, création du curseur
conn=sqlite3.connect('MONDIAL')
cur=conn.cursor()
##################################
### les tables qui posent problème
##################################
ListeDesProblèmes=[]
def TOTO(x):
    ListeDesProblèmes.append(x)
##TOTO('''CREATE OR REPLACE TYPE GeoCoord AS OBJECT(
##Latitude NUMBER,
##Longitude NUMBER)''')
##
### ?????  /
##
##TOTO('''CREATE TABLE Mountain(
##Name VARCHAR2(50) CONSTRAINT MountainKey PRIMARY KEY,
##Mountains VARCHAR2(50),
##Elevation NUMBER,
##Type VARCHAR2(10),
##Coordinates GeoCoord CONSTRAINT MountainCoord
##    CHECK ((Coordinates.Latitude >= -90) AND 
##            (Coordinates.Latitude <= 90) AND
##            (Coordinates.Longitude > -180) AND
##            (Coordinates.Longitude <= 180)))''')
##
##TOTO('''CREATE TABLE Desert(
##Name VARCHAR2(50) CONSTRAINT DesertKey PRIMARY KEY,
##Area NUMBER,
##Coordinates GeoCoord CONSTRAINT DesCoord
##     CHECK ((Coordinates.Latitude >= -90) AND 
##            (Coordinates.Latitude <= 90) AND
##            (Coordinates.Longitude > -180) AND
##            (Coordinates.Longitude <= 180)))''')
##
##TOTO('''CREATE TABLE Island(
##Name VARCHAR2(50) CONSTRAINT IslandKey PRIMARY KEY,
##Islands VARCHAR2(50),
##Area NUMBER CONSTRAINT IslandAr check (Area >= 0),
##Elevation NUMBER,
##Type VARCHAR2(10),
##Coordinates GeoCoord CONSTRAINT IslandCoord
##     CHECK ((Coordinates.Latitude >= -90) AND 
##            (Coordinates.Latitude <= 90) AND
##            (Coordinates.Longitude > -180) AND
##            (Coordinates.Longitude <= 180)))''')
####
####TOTO('''CREATE TABLE Lake(
####Name VARCHAR2(50) CONSTRAINT LakeKey PRIMARY KEY,
####River VARCHAR2(50),
####Area NUMBER CONSTRAINT LakeAr CHECK (Area >= 0),
####Elevation NUMBER,
####Depth NUMBER CONSTRAINT LakeDpth CHECK (Depth >= 0),
####Height NUMBER CONSTRAINT DamHeight CHECK (Height > 0),
####Type VARCHAR2(12),
####Coordinates GeoCoord CONSTRAINT LakeCoord
####     CHECK ((Coordinates.Latitude >= -90) AND 
####            (Coordinates.Latitude <= 90) AND
####            (Coordinates.Longitude > -180) AND
####            (Coordinates.Longitude <= 180)))''')
##
##
##TOTO('''CREATE TABLE River(
##Name VARCHAR2(50) CONSTRAINT RiverKey PRIMARY KEY,
##River VARCHAR2(50),
##Lake VARCHAR2(50),
##Sea VARCHAR2(50),
##Length NUMBER CONSTRAINT RiverLength CHECK (Length >= 0),
##Area NUMBER CONSTRAINT RiverArea CHECK (Area >= 0),
##SourceLatitude FLOAT,
##SourceLongitude FLOAT,
##Mountains VARCHAR2(50),
##SourceElevation NUMBER,
##EstuaryLatitude FLOAT,
##EstyaryLongitude FLOAT,
##EstuaryElevation FLOAT)''')
####TOTO('''CREATE TABLE River(
####Name VARCHAR2(50) CONSTRAINT RiverKey PRIMARY KEY,
####River VARCHAR2(50),
####Lake VARCHAR2(50),
####Sea VARCHAR2(50),
####Length NUMBER CONSTRAINT RiverLength CHECK (Length >= 0),
####Area NUMBER CONSTRAINT RiverArea CHECK (Area >= 0),
####Source GeoCoord CONSTRAINT SourceCoord
####     CHECK ((Source.Latitude >= -90) AND 
####            (Source.Latitude <= 90) AND
####            (Source.Longitude > -180) AND
####            (Source.Longitude <= 180)),
####Mountains VARCHAR2(50),
####SourceElevation NUMBER,
####Estuary GeoCoord CONSTRAINT EstCoord  CHECK ((Estuary.Latitude >= -90) AND 
####            (Estuary.Latitude <= 90) AND
####            (Estuary.Longitude > -180) AND
####            (Estuary.Longitude <= 180)),
####EstuaryElevation NUMBER,
####CONSTRAINT RivFlowsInto CHECK ((River IS NULL AND Lake IS NULL)
####            OR (River IS NULL AND Sea IS NULL)
####            OR (Lake IS NULL AND Sea is NULL)))''')
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
#######################################
def toto(chaine):
    global nbTablesCrées
    nbTablesCrées+=1
    req=chaine
    cur.execute(req)
#######################################
ListeDesTables=["Mountain","Island","Desert","Lake","River","Continent","Country","borders","encompasses","Organization","isMember","Economy","City","Province","Population","Politics","Language","Religion","EthnicGroup","CountryPops",
                "Countryothername","Countrylocalname","Provpops","Provinceothername","Provincelocalname","Citypops","Cityothername","Citylocalname","Sea","RiverThrough","geo_Mountain",
                "geo_Desert","geo_Island","geo_River","geo_Sea","geo_Lake","geo_Source","geo_Estuary","mergesWith","located","locatedOn","islandIn","MountainOnIsland","LakeOnIsland",
                "RiverOnIsland","Airport"]

print('nombre de tables :',len(ListeDesTables))
for x in ListeDesTables:
    print(x)
for x in ListeDesTables:
    try:
        req="DROP TABLE "+x
        cur.execute(req)
    except:
        pass

nbTablesCrées=0
toto('''CREATE TABLE Lake(
Name VARCHAR2(50) CONSTRAINT LakeKey PRIMARY KEY,
River VARCHAR2(50),
Area NUMBER CONSTRAINT LakeAr CHECK (Area >= 0),
Elevation FLOAT,
Depth FLOAT CONSTRAINT LakeDpth CHECK (Depth >= 0),
Height FLOAT CONSTRAINT DamHeight CHECK (Height > 0),
Type VARCHAR2(12),
LakeLatitude FLOAT,
LakeLongitude FLOAT)''')
##toto('''CREATE TABLE Lake(
##Name VARCHAR2(50) CONSTRAINT LakeKey PRIMARY KEY,
##River VARCHAR2(50),
##Area NUMBER CONSTRAINT LakeAr CHECK (Area >= 0),
##Elevation NUMBER,
##Depth NUMBER CONSTRAINT LakeDpth CHECK (Depth >= 0),
##Height NUMBER CONSTRAINT DamHeight CHECK (Height > 0),
##Type VARCHAR2(12),
##Coordinates GeoCoord)''')

toto('''CREATE TABLE Mountain(
Name VARCHAR2(50) CONSTRAINT MountainKey PRIMARY KEY,
Mountains VARCHAR2(50),
Elevation FLOAT,
Type VARCHAR2(10),
MountainLatitude FLOAT,
MountainLongitude FLOAT)''')

toto('''CREATE TABLE Desert(
Name VARCHAR2(50) CONSTRAINT DesertKey PRIMARY KEY,
Area FLOAT,
DesertLatitude FLOAT,
DesertLongitude FLOAT)''')

toto('''CREATE TABLE Island(
Name VARCHAR2(50) CONSTRAINT IslandKey PRIMARY KEY,
Islands VARCHAR2(50),
Area FLOAT CONSTRAINT IslandAr check (Area >= 0),
Elevation FLOAT,
Type VARCHAR2(10),
IslandLatitude FLOAT,
IslandLongitude FLOAT)''')

toto('''CREATE TABLE River(
Name VARCHAR2(50) CONSTRAINT RiverKey PRIMARY KEY,
River VARCHAR2(50),
Lake VARCHAR2(50),
Sea VARCHAR2(50),
Length NUMBER CONSTRAINT RiverLength CHECK (Length >= 0),
Area NUMBER CONSTRAINT RiverArea CHECK (Area >= 0),
SourceLatitude FLOAT,
SourceLongitude FLOAT,
Mountains VARCHAR2(50),
SourceElevation FLOAT,
EstuaryLatitude FLOAT,
EstuaryLongitude FLOAT,
EstuaryElevation FLOAT)''')

##toto('''CREATE TABLE River(
##Name VARCHAR2(50) CONSTRAINT RiverKey PRIMARY KEY,
##River VARCHAR2(50),
##Lake VARCHAR2(50),
##Sea VARCHAR2(50),
##Length NUMBER CONSTRAINT RiverLength CHECK (Length >= 0),
##Area NUMBER CONSTRAINT RiverArea CHECK (Area >= 0),
##Source GeoCoord,
##Mountains VARCHAR2(50),
##SourceElevation NUMBER,
##Estuary GeoCoord,
##EstuaryElevation NUMBER,
##CONSTRAINT RivFlowsInto CHECK ((River IS NULL AND Lake IS NULL)
##            OR (River IS NULL AND Sea IS NULL)
##            OR (Lake IS NULL AND Sea is NULL)))''')
#########################################
toto('''CREATE TABLE Country(
Name VARCHAR2(50) NOT NULL UNIQUE, 
Code VARCHAR2(4) CONSTRAINT CountryKey PRIMARY KEY, 
Capital VARCHAR2(50), Province VARCHAR2(50), 
Area NUMBER CONSTRAINT CountryArea CHECK (Area >= 0), 
Population NUMBER CONSTRAINT CountryPop CHECK (Population >= 0))''')

toto('''CREATE TABLE City(
Name VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
Population NUMBER CONSTRAINT CityPop CHECK (Population >= 0),
Latitude NUMBER CONSTRAINT CityLat CHECK ((Latitude >= -90) AND (Latitude <= 90)),
Longitude NUMBER CONSTRAINT CityLon CHECK ((Longitude >= -180) AND (Longitude <= 180)),
Elevation NUMBER,
CONSTRAINT CityKey PRIMARY KEY (Name, Country, Province))''')

toto('''CREATE TABLE Province(
Name VARCHAR2(50) CONSTRAINT PrName NOT NULL,
Country  VARCHAR2(4) CONSTRAINT PrCountry NOT NULL,
Population NUMBER CONSTRAINT PrPop CHECK (Population >= 0),
Area NUMBER CONSTRAINT PrAr CHECK (Area >= 0),
Capital VARCHAR2(50),
CapProv VARCHAR2(50),
CONSTRAINT PrKey PRIMARY KEY (Name, Country))''')

toto('''CREATE TABLE Economy(
Country VARCHAR2(4) CONSTRAINT EconomyKey PRIMARY KEY,
GDP NUMBER CONSTRAINT EconomyGDP CHECK (GDP >= 0),
Agriculture NUMBER,
Service NUMBER,
Industry NUMBER,
Inflation NUMBER,
Unemployment NUMBER)''')

toto('''CREATE TABLE Population(
Country VARCHAR2(4) CONSTRAINT PopKey PRIMARY KEY,
Population_Growth NUMBER,
Infant_Mortality NUMBER)''')

toto('''CREATE TABLE Politics(
Country VARCHAR2(4) CONSTRAINT PoliticsKey PRIMARY KEY,
Independence DATE,
WasDependent VARCHAR2(50),
Dependent  VARCHAR2(4),
Government VARCHAR2(120))''')

toto('''CREATE TABLE Language(
Country VARCHAR2(4),
Name VARCHAR2(50),
Percentage NUMBER CONSTRAINT LanguagePercent CHECK ((Percentage > 0) AND (Percentage <= 100)),
CONSTRAINT LanguageKey PRIMARY KEY (Name, Country))''')

toto('''CREATE TABLE Religion(
Country VARCHAR2(4),
Name VARCHAR2(50),
Percentage NUMBER CONSTRAINT ReligionPercent CHECK ((Percentage > 0) AND (Percentage <= 100)),
CONSTRAINT ReligionKey PRIMARY KEY (Name, Country))''')

toto('''CREATE TABLE EthnicGroup(
Country VARCHAR2(4),
Name VARCHAR2(50),
Percentage NUMBER CONSTRAINT EthnicPercent CHECK ((Percentage > 0) AND (Percentage <= 100)),
CONSTRAINT EthnicKey PRIMARY KEY (Name, Country))''')

toto('''CREATE TABLE Countrypops(
Country VARCHAR2(4),
Year NUMBER CONSTRAINT CountryPopsYear CHECK (Year >= 0),
Population NUMBER CONSTRAINT CountryPopsPop CHECK (Population >= 0),
CONSTRAINT CountryPopsKey PRIMARY KEY (Country, Year))''')

toto('''CREATE TABLE Countryothername(
Country VARCHAR2(4),
othername VARCHAR2(50),
CONSTRAINT CountryOthernameKey PRIMARY KEY (Country, othername))''')

toto('''CREATE TABLE Countrylocalname(
Country VARCHAR2(4),
localname VARCHAR2(120),
CONSTRAINT CountrylocalnameKey PRIMARY KEY (Country))''')

toto('''CREATE TABLE Provpops(
Province VARCHAR2(50),
Country VARCHAR2(4),
Year NUMBER CONSTRAINT ProvPopsYear CHECK (Year >= 0),
Population NUMBER CONSTRAINT ProvPopsPop CHECK (Population >= 0),
CONSTRAINT ProvPopKey PRIMARY KEY (Country, Province, Year))''')

toto('''CREATE TABLE Provinceothername(
Province VARCHAR2(50),
Country VARCHAR2(4),
othername VARCHAR2(50),
CONSTRAINT ProvOthernameKey PRIMARY KEY (Country, Province, othername))''')

toto('''CREATE TABLE Provincelocalname(
Province VARCHAR2(50),
Country VARCHAR2(4),
localname VARCHAR2(120),
CONSTRAINT ProvlocalnameKey PRIMARY KEY (Country, Province))''')

toto('''CREATE TABLE Citypops(
City VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
Year NUMBER CONSTRAINT CityPopsYear CHECK (Year >= 0),
Population NUMBER CONSTRAINT CityPopsPop CHECK (Population >= 0),
CONSTRAINT CityPopKey PRIMARY KEY (Country, Province, City, Year))''')

toto('''CREATE TABLE Cityothername(
City VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
othername VARCHAR2(50),
CONSTRAINT CityOthernameKey PRIMARY KEY (Country, Province, City, othername))''')

toto('''CREATE TABLE Citylocalname(
City VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
localname VARCHAR2(120),
CONSTRAINT CitylocalnameKey PRIMARY KEY (Country, Province, City))''')

toto('''CREATE TABLE Continent(
Name VARCHAR2(20) CONSTRAINT ContinentKey PRIMARY KEY,
Area NUMBER(10))''')

toto('''CREATE TABLE borders(
Country1 VARCHAR2(4),
Country2 VARCHAR2(4),
Length NUMBER CHECK (Length > 0),
CONSTRAINT BorderKey PRIMARY KEY (Country1,Country2) )''')

toto('''CREATE TABLE encompasses(
Country VARCHAR2(4) NOT NULL,
Continent VARCHAR2(20) NOT NULL,
Percentage NUMBER, 
CHECK ((Percentage > 0) AND (Percentage <= 100)),
CONSTRAINT EncompassesKey PRIMARY KEY (Country,Continent))''')

toto('''CREATE TABLE Organization(
Abbreviation VARCHAR2(12) Constraint OrgKey PRIMARY KEY,
Name VARCHAR2(100) NOT NULL,
City VARCHAR2(50),
Country VARCHAR2(4), 
 Province VARCHAR2(50),
Established DATE,
CONSTRAINT OrgNameUnique UNIQUE (Name))''')

toto('''CREATE TABLE isMember(
Country VARCHAR2(4),
Organization VARCHAR2(12),
Type VARCHAR2(60) DEFAULT "member",
CONSTRAINT MemberKey PRIMARY KEY (Country,Organization) )''')


toto('''CREATE TABLE RiverThrough(
River VARCHAR2(50),
Lake  VARCHAR2(50),
CONSTRAINT RThroughKey PRIMARY KEY (River,Lake) )''')

toto('''CREATE TABLE geo_Mountain(
Mountain VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GMountainKey PRIMARY KEY (Province,Country,Mountain) )''')

toto('''CREATE TABLE geo_Desert(
Desert VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GDesertKey PRIMARY KEY (Province, Country, Desert) )''')

toto('''CREATE TABLE geo_Island(
Island VARCHAR2(50), 
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GIslandKey PRIMARY KEY (Province, Country, Island) )''')

toto('''CREATE TABLE geo_River(
River VARCHAR2(50), 
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GRiverKey PRIMARY KEY (Province,Country, River) )''')

toto('''CREATE TABLE geo_Sea(
Sea VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GSeaKey PRIMARY KEY (Province, Country, Sea) )''')

toto('''CREATE TABLE geo_Lake(
Lake VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GLakeKey PRIMARY KEY (Province, Country, Lake) )''')

toto('''CREATE TABLE geo_Source(
River VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GSourceKey PRIMARY KEY (Province, Country, River) )''')

toto('''CREATE TABLE geo_Estuary(
River VARCHAR2(50),
Country VARCHAR2(4),
Province VARCHAR2(50),
CONSTRAINT GEstuaryKey PRIMARY KEY (Province, Country, River) )''')

toto('''CREATE TABLE mergesWith(
Sea1 VARCHAR2(50),
Sea2 VARCHAR2(50),
CONSTRAINT MergesWithKey PRIMARY KEY (Sea1, Sea2) )''')

toto('''CREATE TABLE located(
City VARCHAR2(50),
Province VARCHAR2(50),
Country VARCHAR2(4),
River VARCHAR2(50),
Lake VARCHAR2(50),
Sea VARCHAR2(50) )''')

toto('''CREATE TABLE locatedOn(
City VARCHAR2(50),
Province VARCHAR2(50),
Country VARCHAR2(4),
Island VARCHAR2(50),
CONSTRAINT locatedOnKey PRIMARY KEY (City, Province, Country, Island) )''')

toto('''CREATE TABLE islandIn(
Island VARCHAR2(50),
Sea VARCHAR2(50),
Lake VARCHAR2(50),
River VARCHAR2(50) )''')

toto('''CREATE TABLE MountainOnIsland(
Mountain VARCHAR2(50),
Island   VARCHAR2(50),
CONSTRAINT MountainIslKey PRIMARY KEY (Mountain, Island) )''')

toto('''CREATE TABLE LakeOnIsland(
Lake    VARCHAR2(50),
Island  VARCHAR2(50),
CONSTRAINT LakeIslKey PRIMARY KEY (Lake, Island) )''')

toto('''CREATE TABLE RiverOnIsland(
River   VARCHAR2(50),
Island  VARCHAR2(50),
CONSTRAINT RiverIslKey PRIMARY KEY (River, Island) )''')

toto('''CREATE TABLE Airport(
IATACode VARCHAR(3) PRIMARY KEY,
Name VARCHAR2(100),
Country VARCHAR2(4),
City VARCHAR2(50),
Province VARCHAR2(50),
Island VARCHAR2(50),
Latitude NUMBER CONSTRAINT AirpLat CHECK ((Latitude >= -90) AND (Latitude <= 90)),
Longitude NUMBER CONSTRAINT AirpLon CHECK ((Longitude >= -180) AND (Longitude <= 180)),
Elevation NUMBER,
gmtOffset NUMBER )''')

toto('''CREATE TABLE Sea(
Name VARCHAR2(50) CONSTRAINT SeaKey PRIMARY KEY,
Area NUMBER CONSTRAINT SeaAr CHECK (Area >= 0),
Depth NUMBER CONSTRAINT SeaDepth CHECK (Depth >= 0))''')

print('*'*50)
print('*'*50)
print('*'*50)
print("nb tables crées :",nbTablesCrées)
print('*'*50)
print('*'*50)
print('*'*50)
print("nb de problèmes :",len(ListeDesProblèmes))
n=0
for x in ListeDesProblèmes:
    print('*'*50)
    n+=1
    print('problème ',n)
    print(x)

