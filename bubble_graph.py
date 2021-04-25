import plotly.graph_objects as go
import csv
import math

# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F']

theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':14, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        coloraxis = {'autocolorscale':False, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)

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
    27960,
    0
]
num_tweets = [
    85, 16, 17, 2, 2, 0, 75, 14, 10
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

with open("num_followers.csv", 'rt') as f:
    data = csv.reader(f)
    for row in data:
        num_followers.append(int(row[0]))


with open("house_num_retweets_correct.csv", 'rt') as f:
    data = csv.reader(f)
    for row in data:
        for num in row:
            total_retweets.append(int(num))

with open("house_reps_tweets_num.csv", 'rt') as f:
    data = csv.reader(f)
    for row in data:
        for num in row:
            num_tweets.append(int(num))

marker_sizes_followers = []

for num in num_followers:
    marker_sizes_followers.append(math.sqrt(num) / 20)

for i in range(len(total_retweets)):
    print(names[i] + ": " + str(num_tweets[i]) + ", " + str(total_retweets[i]) + ", " + str(num_followers[i]))

print(len(num_tweets))
print(len(total_retweets))
print(len(num_followers))
print(len(names))

significant_names = []
significant_followers = []
significant_retweets = []
significant_tweets = []
significant_markers = []

small_names = []
small_followers = []
small_retweets = []
small_tweets = []
small_markers = []

for i in range(len(total_retweets)):
    if num_followers[i] > 500000:
        significant_names.append(names[i])
        significant_followers.append(num_followers[i])
        significant_retweets.append(total_retweets[i])
        significant_tweets.append(num_tweets[i])
        significant_markers.append(marker_sizes_followers[i])
    else:
        small_names.append(names[i])
        small_followers.append(num_followers[i])
        small_retweets.append(total_retweets[i])
        small_tweets.append(num_tweets[i])
        small_markers.append(marker_sizes_followers[i])


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=significant_tweets, y=significant_retweets,
    mode='markers+text',
    marker_size=significant_markers,
    text=significant_names,
    textposition="top left",
    marker_color=primary_colors[0]
    )
)

fig.add_trace(go.Scatter(
    x=small_tweets, y=small_retweets,
    mode='markers',
    marker_size=small_markers,
    marker_color=primary_colors[0]
    )
)

fig.update_layout(
    title='Number of Followers and Number of Rewtweets Versus StopTheSteal Tweets',
    template=theme_hodp,
    xaxis={'title':{'text':'Number of StopTheSteal Tweets'}}, 
    yaxis={'title':{'text':'Total Retweets'}},
    legend={}
    )

fig.show()


