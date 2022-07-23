#값 입력
l, c = map(int, input().split())
chars = list(map(str, input().split()))
chars.sort()
cryptos = []
consonants = ['a', 'e', 'i', 'o', 'u']

#재귀를 통해 모든 경우의 수를 탐색
def combination(remain_chars, word, depth):
	if depth == l:
		temp = list(word)
		cnt = 0
        #자음 갯수 계산
		for i in temp:
			if i in consonants:
				cnt += 1
        #자음이 1개보다 작거나 모음이 2개보다 작으면 리턴
		if cnt < 1 or l - cnt < 2:
			return
		else:
			cryptos.append(word)
	elif remain_chars == None:
		return
	else:
		for i in range(len(remain_chars)):
			temp = list(remain_chars)
			del temp[:i+1]
			combination(temp, word+remain_chars[i], depth + 1)
        
        
combination(chars, "", 0)
print(*cryptos)

