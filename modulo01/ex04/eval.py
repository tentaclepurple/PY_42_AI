# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: imontero <imontero@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/03 00:24:12 by imontero          #+#    #+#              #
#    Updated: 2023/09/03 00:24:12 by imontero         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
	def zip_evaluate(self, words, coef):
		if len(words) != len(coef):
			return(-1)
		else:
			result = 0
			for i in zip(words, coef):
				result += len(i[0]) * i[1]
			return(result)
	def enumerate_evaluate(self, words, coef):
		if len(words) != len(coef):
			return(-1)
		else:
			result = 0
			for i, word in enumerate(words):
				result += len(word) * coef[i]
			return(result)


if __name__ == '__main__':
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

	test = Evaluator()
	print(test.zip_evaluate(words, coefs))
	print(test.enumerate_evaluate(words, coefs))