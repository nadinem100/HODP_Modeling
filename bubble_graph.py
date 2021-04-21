import plotly.graph_objects as go
import csv

num_followers = []
total_retweets = [
    627629,
    5957,
    22562,
    6548,
    2476,
    0,
    83502,
    71405,
    27960
]
names = [
    "RudyGiuliani",
    "TTuberville",
    "SenRickScott",
    "RogerMarshallMD",
    "SenJohnKennedy",
    "SenHydeSmith",
    "SenTedCruz",
    "HawleyMO",
    "CynthiaMLummis",
    "Robert_Aderholt",
    "RepMoBrooks",
    "CarlforAlabama",
    "RepBarryMoore",
    "USRepGaryPalmer",
    "RepMikeRogers",
    "RepAndyBiggsAZ",
    "RepGosar",
    "RepDLesko",
    "RepDavid",
    "RepRickCrawford",
    "KenCalvert",
    "RepMikeGarcia",
    "DarrellIssa",
    "RepLaMalfa",
    "GOPLeader",
    "DevinNunes",
    "JayObernolte",
    "laurenboebert",
    "RepDLamborn",
    "Kat_Cammack",
    "MarioDB",
    "ByronDonalds",
    "DrNealDunnFL2",
    "RepFranklin",
    "mattgaetz",
    "RepCarlos",
    "RepBrianMast",
    "congbillposey",
    "RepRutherfordFL",
    "RepGregSteube",
    "RepWebster",
    "RepRickAllen",
    "RepBuddyCarter",
    "Rep_Clyde",
    "mtgreenee",
    "CongressmanHice",
    "RepLoudermilk",
    "RepRussFulcher",
    "RepBost",
    "RepMaryMiller",
    "RepJimBaird",
    "RepJimBanks",
    "RepGregPence",
    "RepWalorski",
    "RepRonEstes",
    "JakeLaTurner",
    "RepMann",
    "RepHalRogers",
    "RepGarretGraves",
    "RepClayHiggins",
    "RepMikeJohnson",
    "SteveScalise",
    "RepAndyHarrisMD",
    "RepJackBergman",
    "RepLisaMcClain",
    "RepWalberg",
    "RepFischbach",
    "RepHagedorn",
    "RepMichaelGuest",
    "RepTrentKelly",
    "CongPalazzo",
    "RepSamGraves",
    "RepHartzler",
    "USRepLong",
    "RepBlaine",
    "RepJasonSmith",
    "RepRosendale",
    "RepDanBishop",
    "RepTedBudd",
    "RepCawthorn",
    "virginiafoxx",
    "RepRichHudson",
    "RepGregMurphy",
    "RepDavidRouzer",
    "RepHerrell",
    "RepJacobs",
    "NMalliotakis",
    "RepStefanik",
    "RepLeeZeldin",
    "RepAdrianSmith",
    "RepSteveChabot",
    "WarrenDavidson",
    "RepBobGibbs",
    "RepBillJohnson",
    "Jim_Jordan",
    "stephaniebice",
    "TomColeOK04",
    "repkevinhern",
    "RepFrankLucas",
    "RepMullin",
    "RepBentz",
    "RepJohnJoyce",
    "RepFredKeller",
    "MikeKellyPA",
    "RepMeuser",
    "RepScottPerry",
    "GReschenthaler",
    "RepSmucker",
    "CongressmanGT",
    "RepJeffDuncan",
    "RepRalphNorman",
    "RepTomRice",
    "RepTimmons",
    "RepJoeWilson",
    "timburchett",
    "DesJarlaisTN04",
    "RepChuck",
    "RepMarkGreen",
    "DHarshbargerTN1",
    "RepDavidKustoff",
    "RepJohnRose",
    "RepArrington",
    "RepBrianBabin",
    "michaelcburgess",
    "JudgeCarter",
    "RepCloudTX",
    "RepPatFallon",
    "replouiegohmert",
    "Lancegooden",
    "RepRonnyJackson",
    "RepTroyNehls",
    "AugustPfluger",
    "PeteSessions",
    "Bethvanduyne",
    "TXRandy14",
    "RepRWilliams",
    "RepRonWright",
    "BurgessOwens",
    "RepChrisStewart",
    "RepBenCline",
    "RepBobGood",
    "RepMGriffith",
    "RobWittman",
    "RepCarolMiller",
    "RepAlexMooney",
    "RepFitzgerald",
    "TomTiffanyWI"
    ]
marker_sizes = []
print(len(names))

with open("num_followers.csv", 'rt') as f:
    data = csv.reader(f)
    for row in data:
        num_followers.append(int(row[0]))

with open("house_num_retweets.csv", 'rt') as f:
    data = csv.reader(f)
    for row in data:
        for num in row:
            total_retweets.append(int(num))

for num in total_retweets:
    marker_sizes.append(10)

print(total_retweets)

annotations = []

for i in range(len(total_retweets)):
    annotations.append(dict(x=total_retweets[i], y=num_followers[i], text=names[i]))

fig = go.Figure(data=[go.Scatter(
    x=total_retweets, y=num_followers,
    mode='markers',
    marker_size=marker_sizes,
    
    )
])

fig.show()


