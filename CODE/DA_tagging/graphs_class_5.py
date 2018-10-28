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

kmeans_pos= [0.122703054596,
0.307950273011,
0.299528599665,
0.378164016605,
0.253273470018,
0.200130044599,
0.209857952745,
0.217084267678,
0.225686413333,
0.237676837122,
0.244841305259,
0.239182566386,
0.237279892858
]

kmeans_lexical = [
]

kmeans_word2vec = [0.40441173732,
0.57821391698,
0.374879506897,
0.360348510517,
0.354602467051,
0.347279170477,
0.325046215363,
0.315125744533,
0.312291622652,
0.298640391581,
0.291545246704,
0.315633775872,
0.339511018848
]

hierarchical_pos = [
]
hierarchical_pos_cosine = [
]

hierarchical_word2vec = [
]

hierarchical_word2vec_cosine = [
]

hierarchical_lexical = [
]
hierarchical_lexical_cosine = []

EM_pos = [0.153786538776,
0.0784486457437,
0.0797015789019,
0.0778541433934,
0.0762698803645,
0.0860772094045,
0.102040553715,
0.123011639979,
0.168645792257,
0.196505460173,
0.233590223611,
0.27297750278,
0.290632958522
]
EM_word2vec = [0.472400483813,
0.400859448079,
0.320656000148,
0.25225940729,
0.320074380858,
0.369134754941,
0.393159461343,
0.417255873646
]
EM_lexical = [
]

font_prop = font_manager.FontProperties(size= 12)

#title('accuracies for clustering methods with different text representation', fontproperties=font_prop)
xlabel('number of clusters', fontproperties=font_prop)
ylabel('weighted accuracy', fontproperties=font_prop)

#
plt.plot(n_clusters, kmeans_pos, color=cnames['green'], marker='s', linestyle='dashed', label='kmeans POS Euclidean')
plt.plot(n_clusters, kmeans_word2vec,color=cnames['blue'], marker='s', linestyle='dashed', label='kmeans word2vec Euclidean' )# color='b')
#plt.plot(n_clusters, kmeans_lexical, color=cnames['red'], marker='s', label='kmeans lexical Euclidean' )# color='b')

# plt.plot(n_clusters, hierarchical_pos, color=cnames['blue'], marker='s', linestyle='dashed', label='hierarchical POS Euclidean')
# plt.plot(n_clusters, hierarchical_word2vec, 'ys-', label='hierarchical word2vec Euclidean')
# plt.plot(n_clusters, hierarchical_lexical, color=cnames['black'], marker='s', linestyle='dashed', label='hierarchical word2vec Euclidean')
#
# plt.plot(n_clusters, hierarchical_pos_cosine, 'rs-', label='hierarchical POS cosine')
# plt.plot(n_clusters, hierarchical_word2vec_cosine, 'gs-', label='hierarchical word2vec cosine ')
# #plt.plot(n_clusters, hierarchical_lexical_cosine, 'ys-', label='hierarchical word2vec cosine')

plt.plot(n_clusters, EM_pos, 'rs-', label='EM POS Euclidean')
#plt.plot(n_clusters, EM_word2vec, 'ks-', label='EM word2vec Euclidean')
#plt.plot(n_clusters, EM_lexical, color=cnames['blue'], marker='s', linestyle='dashed', label='EM lexical Euclidean')



plt.gca().yaxis.grid(True)
#plt.xlim(0,105)
plt.ylim(0,1.)

plt.legend()

plt.show()