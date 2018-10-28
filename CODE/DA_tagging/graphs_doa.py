
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

# TCA: ICSI to AMI
#5 labels
n_samples_5_ami_tca = [
580,
1165,
1745,
2325,
2910,
3490
]

weihted_5_ami_tca = [
0.363,
0.0076,
0.055,
0.0058,
0.0095,
0.008
]

accuracy_5_ami_tca = [
0.271,
0.0127,
0.0489,
0.0096,
0.0134,
0.0134
]

#TCA: ICSI to AMI
# 3 labels
n_samples_3_ami_tca = [
267,
534,
801,
1068,
1332,
1599,
1866,
2133,
2400,
2667
]

weihted_3_ami_tca = [
0.1819,
0.171,
0.109,
0.367,
0.403,
0.26,
0.385,
0.377,
0.45,
0.44
    ]

accuracy_3_ami_tca = [
0.248,
0.246,
0.221,
0.356,
0.373,
0.295,
0.359,
0.357,
0.395
]

#TCA: AMI to ICSI
# 5 labels

n_samples_5_icsi_tca = [
95,
190,
285,
375,
470,
565,
660,
755,
850,
945,
1885,
2830,
3775
]

weihted_5_icsi_tca  =[
0.162,
0.088,
0.22,
0.036,
0.231,
0.121,
0.161,
0.114,
0.175,
0.407,
0.062,
0.05,
0.0519
]

accuracy_5_icsi_tca  = [
0.235,
0.163,
0.185,
0.084,
0.257,
0.174,
0.184,
0.152,
0.2063,
0.322,
0.119,
0.105,
0.106
]

#TCA: AMI to ICSI
#3 labels

n_samples_3_icsi_tca  = [
57,
111,
168,
225,
282,
336,
393,
450,
504,
561,
1122,
1686,
2247,
2808,
3369,
3930,
4494,
5055,
5616
]

weihted_3_icsi_tca  = [
0.137,
0.206,
0.294,
0.204,
0.0656,
0.0549,
0.053,
0.126,
0.092,
0.065,
0.075,
0.1046,
0.0621,
0.0566,
0.067,
0.225,
0.055,
0.045,
0.092
]

accuracy_3_icsi_tca  = [
0.221,
0.286,
0.309,
0.27,
0.166,
0.163,
0.161,
0.218,
0.194,
0.172,
0.175,
0.197,
0.165,
0.159,
0.16794,
0.270483460559796,
0.159724076546507,
0.143857566765579,
0.162962962962963
]

#######################

# SCL: ICSI to AMI
#5 labels

n_samples_5_ami_scl  = [
580,
1165,
1745,
2325,
2910,
3490,
4075,
4655,
5235,
5820
]

weihted_5_ami_scl = [
0.297763347946115,
0.268500203440029,
0.340847738691504,
0.295365392399995,
0.28119596403632,
0.307380866785848,
0.372189610393914,
0.342151364123946,
0.318713163131985,
0.298137709281288
]

accuracy_5_ami_scl = [
0.286551724137931,
0.271072961373391,
0.311862464183381,
0.292301075268817,
0.276082474226804,
0.294498567335244,
0.337128834355828,
0.315402792696026,
0.309226361031519,
0.290721649484536
]

# SCL: ICSI to AMI
#3 labels

n_samples_3_ami_scl = [267,
534,
801,
1068,
1332,
1599,
1866,
2133,
2400
]

weihted_3_ami_scl = [
0.480236901446025,
0.488840363951186,
0.390698135225042,
0.517526599152572,
0.41597536726689,
0.366877613239747,
0.456899834145552,
0.378990968817073,
0.417751305990434
]

accuracy_3_ami_scl = [
0.412734082397004,
0.434082397003745,
0.377028714107366,
0.44625468164794,
0.389039039039039,
0.357848655409631,
0.412325830653805,
0.36924519456165,
0.390333333333333
]
# SCL: AMI to ICSI
#5 labels

weihted_5_icsi_scl = [
0.153433433669652,
0.112995897197962,
0.140144416639629,
0.138870094371386,
0.156648732640831,
0.180250689373151,
0.163070211062081,
0.152535236635401,
0.132800199189971,
0.193830202427695,
0.147898659931458,
0.318141732745377,
0.807192772703048,
0.825796788851309,
0.826519088440492,
0.826797267064582
]

accuracy_5_icsi_scl = [
0.176842105263158,
0.150526315789474,
0.166315789473684,
0.173866666666667,
0.186382978723404,
0.205309734513274,
0.197878787878788,
0.195761589403974,
0.185176470588235,
0.221587301587302,
0.19317435082141,
0.27751987281399,
0.552862630812028,
0.563691601165769,
0.564273413697178,
0.56469478592624
]

n_samples_5_icsi_scl = [
95,
190,
285,
375,
470,
565,
660,
755,
850,
945,
9435,
18870,
37745,
56615,
75490,
94360
]
# SCL: AMI to ICSI
#3 labels

n_samples_3_icsi_scl = [
57,
111,
168,
225,
282,
336,
393,
450,
504,
561,
5616,
11232,
22464,
33693,
44925,
56157
]

weihted_3_icsi_scl = [
0.37063550097658,
0.496826544227494,
0.328373436013521,
0.222785215105501,
0.373840618071009,
0.352691491819133,
0.206375844823425,
0.239809483218072,
0.23079961514169,
0.218362323831597,
0.17744883855846,
0.3467369756056,
0.900968222458128,
0.925192000213129,
0.926505538967688,
0.925494556921247
]

accuracy_3_icsi_scl = [
0.336842105263158,
0.452252252252252,
0.357142857142857,
0.278222222222222,
0.369503546099291,
0.363095238095238,
0.272264631043257,
0.292888888888889,
0.293650793650794,
0.284848484848485,
0.254558404558405,
0.357193732193732,
0.721394230769231,
0.737678449529576,
0.738924874791319,
0.737795822426412
]


#################################"""
font_prop = font_manager.FontProperties(size= 12)
xlabel('number of sampled data', fontproperties=font_prop)
ylabel('accuracy', fontproperties=font_prop)

title('accuracies for DoA methods with training on ICSI and testing on the AMI', fontproperties=font_prop)

plt.plot(n_samples_3_ami_scl, weihted_3_ami_scl, color=cnames['blue'], marker='s', linestyle='dashed', label='3 taxonomies SCL')
plt.plot(n_samples_3_ami_tca, weihted_3_ami_tca, color=cnames['black'], marker='s', linestyle='dashed', label='3 taxonomies TCA')
plt.plot(n_samples_5_ami_scl, weihted_5_ami_scl, color=cnames['red'], marker='s', linestyle='dashed', label='5 taxonomies SCL')
plt.plot(n_samples_5_ami_tca, weihted_5_ami_tca, color=cnames['green'], marker='s', linestyle='dashed', label='5 taxonomies TCA')


plt.gca().yaxis.grid(True)
plt.xlim(0,7000)
plt.ylim(0,1.)

plt.legend()
plt.show()
###########################################

font_prop = font_manager.FontProperties(size= 12)
xlabel('number of sampled data', fontproperties=font_prop)
ylabel('accuracy', fontproperties=font_prop)

title('accuracies for DoA methods with training on AMI and testing on the ICSI', fontproperties=font_prop)

#plt.plot(n_samples_3_icsi_scl, weihted_3_icsi_scl, color=cnames['blue'], marker='s', linestyle='dashed', label='3 taxonomies SCL')
plt.plot(n_samples_3_icsi_tca, weihted_3_icsi_tca, color=cnames['black'], marker='s', linestyle='dashed', label='3 taxonomies TCA')
#plt.plot(n_samples_5_icsi_scl, weihted_5_icsi_scl, color=cnames['red'], marker='s', linestyle='dashed', label='5 taxonomies SCL')
plt.plot(n_samples_5_icsi_tca, weihted_5_icsi_tca, color=cnames['green'], marker='s', linestyle='dashed', label='5 taxonomies TCA')


plt.gca().yaxis.grid(True)
plt.xlim(0,6000)
plt.ylim(0,1.)

plt.legend()
plt.show()

