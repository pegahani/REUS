from matplotlib import pyplot as plt, font_manager

font_prop = font_manager.FontProperties(size=18)

result = {'all_meeting_3': [(0.2, 0.9), (0.15, 0.45), (0.2, 0.75), (0.25, 0.7), (0.4, 0.8), (0.4, 0.85), (0.3, 0.8), (0.2, 0.75), (0.25, 0.95), (0.25, 0.75), (0.15, 0.85), (0.2, 0.75), (0.2, 0.95), (0.1, 0.75), (0.1, 0.85), (0.25, 0.8), (0.45, 0.9), (0.25, 0.95), (0.15, 0.8), (0.3, 0.85), (0.2, 0.95), (0.05, 0.9), (0.4, 0.95), (0.35, 0.8), (0.1, 0.7), (0.4, 0.95), (0.4, 0.85), (0.5, 0.9), (0.3, 0.85), (0.25, 0.7), (0.3, 0.7), (0.15, 0.3), (0.3, 1.0), (0.7, 0.85), None, None], 'all_meeting_2': [(0.5, 0.85), (0.15, 0.9), (0.25, 0.95), (0.15, 0.8), (0.15, 0.6), (0.15, 0.8), (0.3, 0.9), (0.3, 0.95), (0.05, 0.8), (0.3, 0.9), (0.3, 1.0), (0.05, 0.7), (0.25, 0.7), (0.3, 0.8), (0.3, 0.9), (0.2, 0.75), (0.15, 0.8), (0.2, 0.9), (0.3, 0.8), (0.55, 0.85), (0.15, 0.85), (0.25, 0.8), (0.2, 0.9), (0.35, 0.8), (0.3, 0.95), (0.35, 0.85), (0.1, 0.85), (0.25, 0.9), (0.25, 0.85), (0.25, 0.8), (0.3, 0.65), (0.5, 0.8), (0.35, 1.0), (0.5, 0.75), (0.3, 0.8), None], 'all_meeting_1': [(0.3, 0.7), (0.4, 0.7), (0.2, 0.95), (0.1, 0.7), (0.25, 0.6), (0.25, 0.55), (0.35, 0.5), (0.3, 0.8), (0.15, 0.9), (0.45, 0.65), (0.1, 0.75), (0.1, 0.85), (0.15, 0.7), (0.05, 0.25), (0.15, 0.65), (0.15, 0.65), (0.45, 0.7), (0.2, 0.3), (0.15, 0.55), (0.2, 0.4), (0.15, 0.95), (0.2, 0.6), (0.05, 0.65), (0.35, 0.75), (0.2, 0.8), (0.1, 0.8), (0.1, 0.65), (0.15, 0.7), (0.45, 0.75), (0.1, 0.65), (0.3, 0.95), (0.05, 0.55), (0.15, 0.65), (0.15, 0.85), (0.25, 0.4), None], 'all_meeting_4': [(0.5, 0.95), (0.15, 0.65), None, (0.5, 0.95), (0.4, 0.75), None, (0.45, 0.75), (0.35, 0.9), (0.5, 0.85), (0.45, 0.9), (0.3, 0.9), (0.25, 0.95), (0.4, 0.95), (0.15, 0.7), (0.15, 0.8), (0.2, 0.75), (0.25, 0.8), (0.35, 0.75), (0.1, 0.5), (0.25, 0.7), (0.35, 0.75), (0.25, 0.75), (0.5, 1.0), (0.35, 0.75), (0.2, 0.7), (0.4, 0.95), (0.2, 0.75), (0.4, 0.9), (0.3, 0.7), (0.2, 0.75), (0.15, 0.95), (0.3, 0.65), (0.35, 0.95), (0.45, 0.55), (0.1, 0.1), None]}


x1 = [i+1 for i in xrange(36)]
print len(x1)
y_1 = result['all_meeting_1']
print(len(y_1))
y_2 = result['all_meeting_2']
y_3 = result['all_meeting_3']
y_4 = result['all_meeting_4']

y_1_abs =[None if item is None else item[0] for item in y_1]
y_1_ex =[None if item is None else item[1] for item in y_1]
y_2_abs =[None if item is None else item[0] for item in y_2]
y_2_ex =[None if item is None else item[1] for item in y_2]
y_3_abs =[None if item is None else item[0] for item in y_3]
y_3_ex =[None if item is None else item[1] for item in y_3]
y_4_abs =[None if item is None else item[0] for item in y_4]
y_4_ex =[None if item is None else item[1] for item in y_4]

plt.title('tf-idf results accuacy w.r.t abstractive summaries', fontproperties=font_prop)
plt.xlabel('scenario-based meeting blocks', fontproperties=font_prop)
plt.ylabel('accuracy', fontproperties=font_prop)
plt.xticks([i+1 for i in xrange(35)])

plt.plot(x1, y_1_abs, 'ro', markersize= 15, alpha=.5, label='meeting 1')#, color='r', marker='o')
plt.plot(x1, y_2_abs, 'bo', markersize= 15, alpha=.5, label='meeting 2' )# color='b')
plt.plot(x1, y_3_abs, 'go', markersize= 15, alpha=.5, label='meeting 3') #, color='g')
plt.plot(x1, y_4_abs, 'yo', markersize= 15, alpha=.5, label='meeting 4')#, color='y')

plt.gca().xaxis.grid(True)
plt.xlim(0,36)
plt.ylim(0.0,1.02)
# plt.grid(b=True, which='major',linewidth=1.0)

plt.legend(loc='upper left')
plt.show()


plt.title('tf-idf results accuracy w.r.t extractive summaries', fontproperties=font_prop)
plt.xlabel('scenario-based meeting blocks', fontproperties=font_prop)
plt.ylabel('accuracy', fontproperties=font_prop)
plt.xticks([i+1 for i in xrange(35)])

plt.plot(x1, y_1_ex, 'ro' , markersize= 15, alpha=.5, label='meeting 1')#,color='r', marker='o')
plt.plot(x1, y_2_ex, 'bo', markersize= 15, alpha=.5, label='meeting 2')#color='b')
plt.plot(x1, y_3_ex, 'go', markersize= 15, alpha=.5, label='meeting 3') #color='g')
plt.plot(x1, y_4_ex, 'yo', markersize= 15, alpha=.5, label='meeting 4')#, color='y')

plt.gca().xaxis.grid(True)
plt.xlim(0,36)
plt.ylim(0.0,1.2)
# plt.grid(b=True, which='major',linewidth=1.0)

plt.legend(loc='lower left')
plt.show()