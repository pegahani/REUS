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

kmeans_pos = [  {0: 1.0},
 {0: 0.9931612505141918},
 {0: 1.0},
 {0: 0.9931612505141918},
 {0: 0.9862678681612506},
 {0: 0.9796265019373415},
 {0: 0.9767878261444439, 1: 0.00748663101604278},
 {0: 0.9839742550245906, 1: 0.009444829067990834},
 {0: 0.9715232606408231, 1: 0.020730325671324247},
 {0: 0.9905329794961463, 1: 0.0073439887318563785},
 {0: 0.9775030438584578},
 {0: 0.9839943500583572, 1: 0.00977066893830703},
 {0: 0.9791763218653128, 1: 0.0013368983957219253}
]

kmeans_pos_1 = [item[0]  if 0 in item.keys()  else 0 for item in kmeans_pos]
kmeans_pos_2 = [item[1]  if 1 in item.keys() else 0 for item in kmeans_pos]
kmeans_pos_3 = [item[2]  if 2 in item.keys() else 0 for item in kmeans_pos]


kmeans_word2vec = [ {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0, 2: 0.01463692756796205},
 {0: 0.9933777858969675, 2: 0.0010893246187363833},
 {0: 0.9931640625, 2: 0.03781697451172936},
 {0: 0.9988801555104803, 2: 0.023424859454271217},
 {0: 0.9994117647058824, 2: 0.04159700769562362},
 {0: 0.9858409398242057, 2: 0.01791129481981558}
]

kmeans_word2vec_1 = [item[0]  if 0 in item.keys() else 0 for item in kmeans_word2vec]
kmeans_word2vec_2 = [item[1]  if 1 in item.keys() else 0 for item in kmeans_word2vec]
kmeans_word2vec_3 = [item[2]  if 2 in item.keys() else 0 for item in kmeans_word2vec]

kmeans_lexical = [ {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 0.993872549019608},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 0.9930882352941177}
]

kmeans_lexical_1 = [item[0]  if 0 in item.keys() else 0 for item in kmeans_lexical]
kmeans_lexical_2 = [item[1]  if 1 in item.keys() else 0 for item in kmeans_lexical]
kmeans_lexical_3 = [item[2]  if 2 in item.keys() else 0 for item in kmeans_lexical]

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

EM_pos = [ {0: 1.0},
 {0: 1.0},
 {0: 0.9857085407107142, 1: 0.011717252768862091},
 {0: 0.9848613320668063, 1: 0.008947817888226565},
 {0: 0.9862895370012412},
 {0: 0.9722529895713393, 1: 0.012947418934813893},
 {0: 0.9851612262417888, 1: 0.004084967320261438},
 {0: 0.9994929006085194, 1: 0.0069367369589345175},
 {0: 0.9930972388955581},
 {0: 0.9930972388955581, 1: 0.007799760037298888},
 {0: 0.9930555555555555, 2: 0.004357298474945533},
 {0: 1.0},
 {0: 1.0, 1: 0.006127450980392157}
]

EM_pos_1 = [item[0]  if 0 in item.keys() else 0 for item in EM_pos]
EM_pos_2 = [item[1]  if 1 in item.keys() else 0 for item in EM_pos]
EM_pos_3 = [item[2]  if 2 in item.keys() else 0 for item in EM_pos]


EM_word2vec = [ {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 1.0},
 {0: 0.9908747225305218, 1: 0.012803373097490744, 2: 0.007352941176470588},
 {0: 0.8978650670794633, 1: 0.08031674208144797, 2: 0.0057444852941176475},
 {0: 0.8460490911125826, 1: 0.12949241616151105},
 {0: 0.7279321882144358, 1: 0.24327112432777226, 2: 0.007352941176470588},
 {0: 0.6771275816828279, 1: 0.3049363802790727, 2: 0.03676470588235294},
 {0: 0.6911587040415468, 1: 0.25980392156862747, 2: 0.034926470588235295},
 {0: 0.6803779129842619, 1: 0.32295247644512354, 2: 0.03676470588235294}
]

EM_word2vec_1 = [item[0] if 0 in item.keys() else 0 for item in EM_word2vec]
EM_word2vec_2 = [item[1]  if 1 in item.keys() else 0 for item in EM_word2vec]
EM_word2vec_3 = [item[2]  if 2 in item.keys() else 0 for item in EM_word2vec]


EM_lexical = [
]

font_prop = font_manager.FontProperties(size= 12)

# 1: information Exchange, 2: Acts about possible actions,  3:Commenting on previous discussions

title('"Commenting on previous discussions" precision', fontproperties=font_prop)
xlabel('number of clusters', fontproperties=font_prop)
#ylabel('precision', fontproperties=font_prop)

#
#plt.plot(n_clusters, kmeans_pos_1, color=cnames['green'], marker='s', linestyle='dashed', label='kmeans POS Euclidean')
#plt.plot(n_clusters, kmeans_pos_2, color=cnames['green'], marker='s', linestyle='dashed', label='kmeans POS Euclidean', alpha=0.7)
plt.plot(n_clusters, kmeans_pos_3, color=cnames['green'], marker='s', linestyle='dashed', label='kmeans POS Euclidean')

#plt.plot(n_clusters, kmeans_word2vec_1, color=cnames['blue'], marker='s', linestyle='dashed', label='kmeans word2vec Euclidean' )# color='b')
#plt.plot(n_clusters, kmeans_word2vec_2, color=cnames['blue'], marker='s', linestyle='dashed', label='kmeans word2vec Euclidean', alpha=0.7 )
plt.plot(n_clusters, kmeans_word2vec_3, color=cnames['blue'], marker='s', linestyle='dashed', label='kmeans word2vec Euclidean' )

#plt.plot(n_clusters, kmeans_lexical_1, color=cnames['black'], marker='s', label='kmeans lexical Euclidean')
#plt.plot(n_clusters, kmeans_lexical_2, color=cnames['black'], marker='s', label='kmeans lexical Euclidean')
plt.plot(n_clusters, kmeans_lexical_3, color=cnames['black'], marker='s', label='kmeans lexical Euclidean')

# plt.plot(n_clusters, hierarchical_pos, color=cnames['blue'], marker='s', linestyle='dashed', label='hierarchical POS Euclidean')
# plt.plot(n_clusters, hierarchical_word2vec, 'ys-', label='hierarchical word2vec Euclidean')
# plt.plot(n_clusters, hierarchical_lexical, color=cnames['black'], marker='s', linestyle='dashed', label='hierarchical word2vec Euclidean')
#
# plt.plot(n_clusters, hierarchical_pos_cosine, 'rs-', label='hierarchical POS cosine')
# plt.plot(n_clusters, hierarchical_word2vec_cosine, 'gs-', label='hierarchical word2vec cosine ')
# #plt.plot(n_clusters, hierarchical_lexical_cosine, 'ys-', label='hierarchical word2vec cosine')

#plt.plot(n_clusters, EM_pos_1, 'rs-', label='EM POS Euclidean')
#plt.plot(n_clusters, EM_pos_2, 'rs-', label='EM POS Euclidean', alpha=0.7)
plt.plot(n_clusters, EM_pos_3, 'rs-', label='EM POS Euclidean')

#plt.plot(n_clusters, EM_word2vec_1, 'ys-', label='EM word2vec Euclidean')
#plt.plot(n_clusters, EM_word2vec_2, 'ys-', label='EM word2vec Euclidean', alpha=0.7)
plt.plot(n_clusters, EM_word2vec_3, 'ys-', label='EM word2vec Euclidean')

#plt.plot(n_clusters, EM_lexical_1, color=cnames['blue'], marker='s', linestyle='dashed', label='EM lexical Euclidean')
#plt.plot(n_clusters, EM_lexical_2, color=cnames['blue'], marker='s', linestyle='dashed', label='EM lexical Euclidean')
#plt.plot(n_clusters, EM_lexical_3, color=cnames['blue'], marker='s', linestyle='dashed', label='EM lexical Euclidean')


plt.gca().yaxis.grid(True)
#plt.xlim(0,105)
#plt.ylim(0,1.)

plt.legend()

plt.show()