measures = ["", "tys.", "mln.", "mld.", "bln."]
ones = ["", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
tens = ["", "dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]
hundreds = ["", "sto", "dwiescie", "trzysta", "czterysta", "piecset", "szescset", "siedemset", "osiemset", "dziewiecset"]
teens = {
    10: "dziesiec",
    11: "jedenascie",
    12: "dwanascie", 
    13: "trzynascie", 
    14: "czternascie", 
    15: "pietnascie",
    16: "szesnascie",
    17: "siedemnascie",
    18: "osiemnascie",
    19: "dziewietnascie"
}



def splitNumber(number):
	word_number = ""
	splited_number_temp = ""
	index_no = 0
	segment_no = -1
	segment = ""
	for i in range(len(number)-1, -1, -1):
		splited_number_temp = number[i] + splited_number_temp
		index_no += 1
        
		if index_no == 3 or i == 0:
			segment_no += 1
			segment = readNumberSegment(int(splited_number_temp))
			if segment != "":
				word_number = segment + " " + measures[segment_no] + " " + word_number

			index_no = 0
			splited_number_temp = ""
	
	print(word_number.rstrip(" "))


def readNumberSegment(number):
    segment = ""
    
    while number > 0:
        if number >= 100:
            segment += hundreds[int(number / 100)]
            number = number % 100
        
        elif number >= 20:
            segment += tens[int(number / 10)]
            number = number % 10
       
        elif number >= 10:
            segment += teens[number]
            number -= number
        
        elif number >= 1:
            segment += ones[number]
            number -= number
        
        segment += " "
        
    return segment.rstrip(" ")
    


numbers = int(input())

for i in range(0, numbers):
	num = input()
	splited_number = splitNumber(num)
	
