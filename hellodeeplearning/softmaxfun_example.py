import numpy as np
import matplotlib.pyplot as plt

scores = [3.0, 1.0, 5.0, 8.0]
scores = np.array(scores)
def softmax(x):
	sm = np.exp(x)
	sm = sm/np.sum(sm, axis = 0)
	return sm
print(scores)
print(softmax(scores))
print(softmax(scores/10))
print(sum(softmax(scores)))
print(sum(softmax(scores/10)))


# # print(np.sum(softmax(scores)))

# x = np.arange(-2.0, 6.0, 0.1)
# # print(x)
# scores = np.vstack([x, np.ones_like(x), 0.2* np.ones_like(x)])
# print(scores)
# print(scores.T)
# plt.plot(x, softmax(scores).T, linewidth=2)
# plt.show()