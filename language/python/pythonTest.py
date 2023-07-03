############################################################
# (A) ANSWER START


def checkMultipleOfThree(number):
    if(number%3==0):
        return True
    return False

def calcQuotientAndRemain(number):
    list1 = [number//3, number%3]
    return list1


def calcCumulativeValue(x,y):
    result =0
    i=1
    while(i<y):
        if(i%x==0):
            result+=i
        i=i+1
    return result

def calcCumulativeList(x,y):
    list1=[]
    i=1
    while(i<y):
        if(i%x==0):
            list1.append(i)
        i=i+1
    return list1

def calcCumulativeValueAndList(x,y):
    list1=[]
    first = calcCumulativeValue(x,y)
    second = calcCumulativeList(x,y)
    list1.append(first)
    list1.append(second)
    return list1


# (A) ANSWER END
############################################################

############################################################
# (B) STANDARD ANSWER START


def STANDARD_checkMultipleOfThree(givenNum):
    if givenNum % 3 == 0:
        return True
    else:
        return False


def STANDARD_calcQuotientAndRemain(givenNumber):
    quotient = givenNumber // 3
    remain = givenNumber % 3
    return [quotient, remain]


def STANDARD_calcCumulativeValue(givenCondition, givenLimitation):
    sum = 0
    num = 1

    while num < givenLimitation:
        if num % givenCondition == 0:
            sum += num
        num += 1

    return sum


def STANDARD_calcCumulativeList(givenCondition, givenLimitation):
    list = []
    num = 1

    while num < givenLimitation:
        if num % givenCondition == 0:
            list.append(num)
        num += 1

    return list


def STANDARD_calcCumulativeValueAndList(givenCondition, givenLimitation):
    res = []
    list = []
    sum = 0
    num = 1

    while sum < givenLimitation:
        if num % givenCondition == 0:
            list.append(num)
            sum += num
        num += 1

    res.append(sum)
    res.append(list)
    return res

# (B) STANDARD ANSWER END
############################################################

############################################################
# (C) SCORING START


# (C) SCORING END
############################################################

totalScore = 0


def printAnswers(yourAnser, rightAnswer):
    print("     Your Answer  : (", yourAnser, ") -->", type(yourAnser))
    print("     Right Answer : (", rightAnswer, ") -->", type(rightAnswer))


try:
    value = 5

    res_standard = STANDARD_checkMultipleOfThree(value)
    res_given = checkMultipleOfThree(value)

    if res_standard == res_given:
        totalScore += 1
        print("[01] Question - Correct [+1].")
        printAnswers(res_given, res_standard)
    else:
        print("[01] Question - Fail.")
        printAnswers(res_given, res_standard)
except:
    print("[01] Question - Exception.")

try:
    value = 5

    res_standard = STANDARD_calcQuotientAndRemain(value)
    res_given = calcQuotientAndRemain(value)

    if res_standard == res_given:
        totalScore += 1
        print("[02] Question - Correct [+1].")
        printAnswers(res_given, res_standard)
    else:
        print("[02] Question - Fail.")
        printAnswers(res_given, res_standard)
except:
    print("[02] Question - Exception.")

try:
    lv = 3
    rv = 10

    res_standard = STANDARD_calcCumulativeValue(lv, rv)
    res_given = calcCumulativeValue(lv, rv)

    if res_standard == res_given:
        totalScore += 2
        print("[03] Question - Correct [+2].")
        printAnswers(res_given, res_standard)
    else:
        print("[03] Question - Fail.")
        printAnswers(res_given, res_standard)
except:
    print("[03] Question - Exception.")

try:
    lv = 3
    rv = 10

    res_standard = STANDARD_calcCumulativeList(lv, rv)
    res_given = calcCumulativeList(lv, rv)

    if res_standard == res_given:
        totalScore += 2
        print("[04] Question - Correct [+2].")
        printAnswers(res_given, res_standard)
    else:
        print("[04] Question - Fail.")
        printAnswers(res_given, res_standard)
except:
    print("[04] Question - Exception.")

try:
    lv = 3
    rv = 10

    res_standard = STANDARD_calcCumulativeValueAndList(lv, rv)
    res_given = calcCumulativeValueAndList(lv, rv)

    if res_standard == res_given:
        totalScore += 4
        print("[05] Question - Correct [+4].")
        printAnswers(res_given, res_standard)
    else:
        print("[05] Question - Fail.")
        printAnswers(res_given, res_standard)
except:
    print("[05] Question - Exception.")

print("--------------------------------")
print("[**] Total Score : ", totalScore, "(MAX: 10)")

# (C) SCORING END
############################################################
