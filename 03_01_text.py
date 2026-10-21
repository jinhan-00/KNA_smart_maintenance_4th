# notice = """설비 점검 안내
# 1.전원 확인
# 2.센서점검"""
# print(notice)

# \n 줄바꿈
# \t 간격 (탭)
# \\  역슬래시

# notice = """가동점검표
# 1.온도확인
# 2.압력확인"""
# print(notice)

# code="pump_A"
# st="정상"
# date="2026.10.21"
# print(code+ "/"+ st +"/"+ date)



code = "설비"
st = "상태"
check_date = "2026.10.21"
# run_hour = int(4)
run_hour = 4
card = "[설비 정보 카드]\n" + "설비: " + code + "\n" + "상태: " + st + "\n" + "점검일: " + check_date + "\n" + "가동시간: " + str(run_hour) + "시간"

print(card)
