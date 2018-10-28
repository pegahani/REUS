#classes 3 , 20% of each cluster is selected
#20%  3744 for each label: 3*3744 = 11232 total number of samples for clustering

from matplotlib import font_manager
from pylab import figure, title, xlabel, ylabel, xticks, bar, \
    legend, axis, savefig, subplots_adjust, gca, gcf, xlim, ylim, show, plt

cnames = {
'aliceblue':            '#F0F8FF',
'antiquewhite':         '#FAEBD7',
'aqua':                 '#00FFFF',
'aquamarine':           '#7FFFD4',
'azure':                '#F0FFFF',
'beige':                '#F5F5DC',
'bisque':               '#FFE4C4',
'black':                '#000000',
'blanchedalmond':       '#FFEBCD',
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chartreuse':           '#7FFF00',
'chocolate':            '#D2691E',
'coral':                '#FF7F50',
'cornflowerblue':       '#6495ED',
'cornsilk':             '#FFF8DC',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'floralwhite':          '#FFFAF0',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'ghostwhite':           '#F8F8FF',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'ivory':                '#FFFFF0',
'khaki':                '#F0E68C',
'lavender':             '#E6E6FA',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lightblue':            '#ADD8E6',
'lightcoral':           '#F08080',
'lightcyan':            '#E0FFFF',
'lightgoldenrodyellow': '#FAFAD2',
'lightgreen':           '#90EE90',
'lightgray':            '#D3D3D3',
'lightpink':            '#FFB6C1',
'lightsalmon':          '#FFA07A',
'lightseagreen':        '#20B2AA',
'lightskyblue':         '#87CEFA',
'lightslategray':       '#778899',
'lightsteelblue':       '#B0C4DE',
'lightyellow':          '#FFFFE0',
'lime':                 '#00FF00',
'limegreen':            '#32CD32',
'linen':                '#FAF0E6',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumorchid':         '#BA55D3',
'mediumpurple':         '#9370DB',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mintcream':            '#F5FFFA',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navajowhite':          '#FFDEAD',
'navy':                 '#000080',
'oldlace':              '#FDF5E6',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6',
'palegoldenrod':        '#EEE8AA',
'palegreen':            '#98FB98',
'paleturquoise':        '#AFEEEE',
'palevioletred':        '#DB7093',
'papayawhip':           '#FFEFD5',
'peachpuff':            '#FFDAB9',
'peru':                 '#CD853F',
'pink':                 '#FFC0CB',
'plum':                 '#DDA0DD',
'powderblue':           '#B0E0E6',
'purple':               '#800080',
'red':                  '#FF0000',
'rosybrown':            '#BC8F8F',
'royalblue':            '#4169E1',
'saddlebrown':          '#8B4513',
'salmon':               '#FA8072',
'sandybrown':           '#FAA460',
'seagreen':             '#2E8B57',
'seashell':             '#FFF5EE',
'sienna':               '#A0522D',
'silver':               '#C0C0C0',
'skyblue':              '#87CEEB',
'slateblue':            '#6A5ACD',
'slategray':            '#708090',
'snow':                 '#FFFAFA',
'springgreen':          '#00FF7F',
'steelblue':            '#4682B4',
'tan':                  '#D2B48C',
'teal':                 '#008080',
'thistle':              '#D8BFD8',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'violet':               '#EE82EE',
'wheat':                '#F5DEB3',
'white':                '#FFFFFF',
'whitesmoke':           '#F5F5F5',
'yellow':               '#FFFF00',
'yellowgreen':          '#9ACD32'}

n_clusters = [3, 4,5,6,7,8,9,10,11,12, 13, 14, 15]

kmeans_pos= [
0.382662243311172,
0.36394393028994,
0.242459121340074,
0.294282200825712,
0.267363289815234,
0.298587599142097,
0.251451975495894,
0.249924854822822,
0.249247133041022,
0.275682026341649,
0.302757770303048,
0.307532118414347,
0.296732347864337


# 0.342500009223395,
# 0.313725357340842,
# 0.287671232131714,
# 0.312038364902226,
# 0.294094011781117,
# 0.325655979325022,
# 0.282484526846977,
# 0.279735652095923,
# 0.276986760265692,
# 0.296630115623908,
# 0.319739091322494,
# 0.31164848870362,
# 0.311445891949031
]

kmeans_lexical = [
0.235022977550892,
0.254345010207248,
0.248938030037126,
0.29218036740043,
0.297000093269919,
0.329929385081108,
0.352113280642364,
0.345285565528876,
0.324138062112998,
0.361324658327876,
0.383999989548918,
0.364007926382252,
0.403733930963481


# 0.262490798743576,
# 0.282505881836984,
# 0.271789067808235,
# 0.310095127129255,
# 0.308802500982758,
# 0.331326158107201,
# 0.342322846481695,
# 0.336231708186717,
# 0.330047461734254,
# 0.359005492465957,
# 0.37346190369584,
# 0.362157227710741,
# 0.38160816446618
]

kmeans_word2vec = [
0.451290687724131,
0.480562828133294,
0.423492722088403,
0.387013215900069,
0.373313041301961,
0.465667332042279,
0.414249346380367,
0.416578569894382,
0.401199414281007,
0.459686258510891,
0.433406285793842,
0.44283990519215,
0.416175671909842


# 0.435022863010748,
# 0.443233498981708,
# 0.401380410533291,
# 0.368903768846384,
# 0.363273325232541,
# 0.43778977870729,
# 0.398021139608819,
# 0.394519414006877,
# 0.381313678470945,
# 0.437683407404138,
# 0.414644220694062,
# 0.422317076266501,
# 0.402519665277797
]

hierarchical_pos = [
0.356419208207378,
0.484342957733186,
0.598307115884331,
0.586269695811681,
0.605126370058968,
0.600197722908493,
0.585702395038092,
0.567526565850345,
0.569795445316463,
0.563570662606323,
0.516467163635421,
0.515944507950663,
0.475730707401462


# 0.32480531923535,
# 0.417561771698894,
# 0.496279323962179,
# 0.488464527939674,
# 0.509858228195505,
# 0.50175288002446,
# 0.487287296403196,
# 0.477771710823852,
# 0.481941486096837,
# 0.480855531763286,
# 0.437068510901449,
# 0.447908558109851,
# 0.403991346875901
]
hierarchical_pos_cosine = [
0.314883915072997,
0.299452884273636,
0.335065283689024,
0.341736880772427,
0.302122711156176,
0.367451907112907,
0.352858606658786,
0.369744845318668,
0.318858930112019,
0.332501915805864,
0.344067201309374,
0.343077778486059,
0.333891931867535


# 0.306651333337402,
# 0.298645501793135,
# 0.335150120522587,
# 0.329969186955071,
# 0.304723005304384,
# 0.359324994338793,
# 0.348882381637484,
# 0.357451553609812,
# 0.331408923657539,
# 0.336418470403564,
# 0.346321253206715,
# 0.342589590130373,
# 0.333224122416108
]

hierarchical_word2vec = [
0.429004755557112,
0.462072870402022,
0.478591005671564,
0.512474369118531,
0.463191550169336,
0.475808473995853,
0.498699301973038,
0.467058366185503,
0.51228934069868,
0.513580774923413,
0.470614297278785,
0.43870060078096,
0.444419593448516

# 0.402643478518113,
# 0.426475253667719,
# 0.441087997342817,
# 0.462364918527778,
# 0.425069494553051,
# 0.435758864499304,
# 0.457069136143773,
# 0.431762048079382,
# 0.464357974634077,
# 0.483045467361864,
# 0.447665710077074,
# 0.414307868365716,
# 0.417820618002508
]

hierarchical_word2vec_cosine = [
0.369125799577054,
0.414621793198069,
0.464674310031167,
0.476691958923774,
0.473717557262742,
0.47383322754533,
0.446696977867355,
0.457212366360977,
0.497483099980056,
0.478254138348152,
0.472371937631423,
0.499335041887449,
0.472284101512317


# 0.362106433975114,
# 0.392383668083049,
# 0.438110537928843,
# 0.440799293287376,
# 0.433930457294206,
# 0.442341671138404,
# 0.416322881751114,
# 0.4206538023386,
# 0.467706649959203,
# 0.443116838092227,
# 0.442012512852839,
# 0.467046685345894,
# 0.44813446296356
]

hierarchical_lexical = [
0.396959415612967,
0.399927095809266,
0.361076345178471,
0.381820369241752,
0.395954864060079,
0.360993745568258,
0.387598990636006,
0.362452842520708,
0.416272559790401,
0.377895273011101,
0.351493271137007,
0.370916638674237,
0.381592010520941


# 0.376550446417937,
# 0.37665634380709,
# 0.34736623951743,
# 0.374788801278674,
# 0.370689513507526,
# 0.356877048066293,
# 0.374675441912709,
# 0.346676044220168,
# 0.401533610680602,
# 0.375199669190841,
# 0.33384114918115,
# 0.368986211599518,
# 0.368672871031263
]
hierarchical_lexical_cosine = []

EM_pos = [
0.651402629385642,
0.41278607563288,
0.483456672596887,
0.593551547640707,
0.549077830272656,
0.511819101328619,
0.447725980410795,
0.459101563161065,
0.429075484997543,
0.421336718404367,
0.468261274818328,
0.406078796363514,
0.422175813077051

# 0.535957922968914,
# 0.374907568544364,
# 0.424974891617452,
# 0.502802974459612,
# 0.470468623033473,
# 0.444418270031221,
# 0.397523118991397,
# 0.411638562707499,
# 0.390043840655824,
# 0.386622585538328,
# 0.425911951955265,
# 0.370996986832068,
# 0.39419530007801
]

EM_word2vec = [
0.470384958426418,
0.445875959829281,
0.412730302011553,
0.443997139221613,
0.410770873402729,
0.43155809103695,
0.474299612631723,
0.487516806306182,
0.410962553225064,
0.404186512752365,
0.348632487518952,
0.301165205166621,
0.254627345611831


# 0.43075491849874,
# 0.415914111535215,
# 0.40020591006705,
# 0.42069502390236,
# 0.392211931635391,
# 0.402993208767096,
# 0.440781766188837,
# 0.447291818073488,
# 0.397924535890598,
# 0.391332952047616,
# 0.351052135371291,
# 0.319407151552894,
# 0.289557143698335
]
EM_lexical = [
0.338437242642158,
0.308594815852109,
0.284847217219176,
0.26350956186519,
0.271989760727757,
0.295367524705406,
0.284406586112184,
0.2898268800308,
0.330417477968382,
0.32693281862666,
0.319459261006537,
0.257487120148385,
0.364790687768338

# 0.335076958978985,
# 0.325870934321996,
# 0.29705657995115,
# 0.286397240329848,
# 0.28491375071321,
# 0.304104424602107,
# 0.287721694851943,
# 0.296271910098724,
# 0.334678395998339,
# 0.322002121244654,
# 0.311758801238113,
# 0.266423290337721,
# 0.35933524502953
]

font_prop = font_manager.FontProperties(size= 12)

#title('accuracies for clustering methods with different text representation', fontproperties=font_prop)
xlabel('number of clusters', fontproperties=font_prop)
ylabel('accuracy', fontproperties=font_prop)

#
# plt.plot(n_clusters, kmeans_pos, color=cnames['green'], marker='s', linestyle='dashed', label='kmeans POS Euclidean')
# plt.plot(n_clusters, kmeans_word2vec,color=cnames['darkmagenta'], marker='s', linestyle='dashed', label='kmeans word2vec Euclidean' )# color='b')
# plt.plot(n_clusters, kmeans_lexical, color=cnames['red'], marker='s', label='kmeans lexical Euclidean' )# color='b')

plt.plot(n_clusters, hierarchical_pos, color=cnames['blue'], marker='s', linestyle='dashed', label='hierarchical POS Euclidean')
plt.plot(n_clusters, hierarchical_word2vec, 'ys-', label='hierarchical word2vec Euclidean')
plt.plot(n_clusters, hierarchical_lexical, color=cnames['black'], marker='s', linestyle='dashed', label='hierarchical word2vec lexical')

plt.plot(n_clusters, hierarchical_pos_cosine, 'rs-', label='hierarchical POS cosine')
plt.plot(n_clusters, hierarchical_word2vec_cosine, 'gs-', label='hierarchical word2vec cosine ')
# #plt.plot(n_clusters, hierarchical_lexical_cosine, 'ys-', label='hierarchical word2vec cosine')

# plt.plot(n_clusters, EM_pos, 'ys-', label='EM POS Euclidean')
# plt.plot(n_clusters, EM_word2vec, 'ks-', label='EM word2vec Euclidean')
# plt.plot(n_clusters, EM_lexical, color=cnames['blue'], marker='s', linestyle='dashed', label='EM lexical Euclidean')



plt.gca().yaxis.grid(True)
#plt.xlim(0,105)
plt.ylim(0,1.)

plt.legend()

plt.show()