# bar chart example
from matplotlib import font_manager
from pylab import figure, title, xlabel, ylabel, xticks, bar, \
    legend, axis, savefig, subplots_adjust, gca, gcf, xlim, ylim, show, plt

font_prop = font_manager.FontProperties(size= 18)


nucleotides = [str(i+1) for i in xrange(34)]
print nucleotides

# for tf-idf
counts_tfidf = [(0.25, 0.7),
(0.15, 0.6),
(0.1, 0.75),
(0.1, 0.65),
(0.2, 0.5),
(0.1, 0.8),
(0.1, 0.45),
(0.25, 0.9),
(0.15, 0.9),
(0.35, 0.75),
(0.1, 0.65),
(0.0, 0.85),
(0.0, 0.75),
(0.1, 0.45),
(0.2, 0.65),
(0.1, 0.35),
(0.1, 0.65),
(0.05, 0.6),
(0.1, 0.5),
(0.05, 0.35),
(0.05, 0.8),
(0.05, 0.65),
(0.0, 0.7),
(0.1, 0.65),
(0.3, 0.75),
(0.1, 0.6),
(0.1, 0.45),
(0.35, 0.7),
(0.05, 0.55),
(0.2, 0.65),
(0.15, 0.55),
(0.2, 0.2),
(0.15, 0.15),
(0.0, 0.05)
]

#for NMF
counts_nmf = [(0.55, 0.85),
(0.45, 0.95),
(0.4, 0.9),
(0.45, 1.0),
(0.45, 0.85),
(0.35, 0.9),
(0.45, 0.85),
(0.6, 0.95),
(0.45, 0.95),
(0.6, 0.85),
(0.4, 0.8),
(0.2, 0.8),
(0.25, 0.75),
(0.3, 0.8),
(0.55, 0.8),
(0.25, 0.65),
(0.5, 0.8),
(0.3, 0.85),
(0.4, 0.7),
(0.25, 0.65),
(0.35, 0.95),
(0.25, 0.95),
(0.45, 0.95),
(0.35, 0.8),
(0.4, 0.9),
(0.45, 0.95),
(0.35, 1.0),
(0.3, 0.75),
(0.4, 0.85),
(0.4, 0.9),
(0.45, 0.85),
(0.45, 0.7),
(0.3, 0.35),
(0.25, 0.4)]

print sum(item[1] for item in counts_nmf)/sum(item[0] for item in counts_nmf)

figure()  # make separate figure

plt.subplot(2, 1, 1)

title('tf-idf results vs abstractive and extractive summaries', fontproperties=font_prop)
xlabel('scenario-based meetings', fontproperties=font_prop)
ylabel('accuracy', fontproperties=font_prop)

x1 = [(i+1)*(3.0) for i in xrange(34)]
x2 = [x - 1.0 for x in x1]

xticks(x1, nucleotides)

plt.bar(x2, [item[0] for item in counts_tfidf], width=1.0, color="#87CEEB", label="w.r.t abstractive resume")
plt.bar(x1, [item[1] for item in counts_tfidf], width=1.0, color="#F4A460", label="w.r.t extractive resume")

plt.gca().yaxis.grid(True)
plt.xlim(0,105)
plt.ylim(0,1.2)

plt.legend()


plt.subplot(2, 1, 2)
plt.title('NMF topic modelling results vs abstractive and extractive summaries', fontproperties=font_prop)
plt.xlabel('scenario-based meetings', fontproperties=font_prop)
plt.ylabel('accuracy',fontproperties=font_prop)


plt.xticks(x1, nucleotides)

plt.bar(x2, [item[0] for item in counts_nmf], width=1.0, color="#87CEEB", label="w.r.t abstractive resume")
plt.bar(x1, [item[1] for item in counts_nmf], width=1.0, color="#F4A460", label="w.r.t extractive resume")

plt.gca().yaxis.grid(True)
plt.xlim(0,105)
plt.ylim(0,1.2)

plt.legend()


plt.show()