# 파일이름 : main.py
# 작성자 : lee chan hee
# 프로그램명 : 웨이퍼 결함 분석 시스템 V2.0

#전역변수
wafer_list = []
wafer_count = 0

#메뉴 출력 함수
def print_menu() :
    print("\n=== 웨이퍼 결함 분석 시스템 V2.0 ===")
    print("1. 웨이퍼 등록")
    print("2. 전체 웨이퍼 조회")
    print("3. 평균 결함 점수 확인")
    print("4. 위험 웨이퍼 찾기")
    print("0. 프로그램 종료")

#결함 점수 계산 함수 
def calculate_score(defect_count , defect_area, defect_location) :
    count_score = defect_count * 10

    if defect_area < 10 :
        area_score = 10
    elif defect_area < 50:
        area_score = 30
    else:
        area_score = 60

    if defect_location == "center":
        location_score = 50
    elif defect_location == "edge":
        location_score = 30
    else:
        location_score = 10

    total_score = count_score + area_score + location_score

    return total_score


# 상태 판정 함수
def judge_grade(defect_count, defect_area, defect_location, total_score):
    if defect_count >= 10 and defect_location == "center":
        grade = "긴급위험"
    elif defect_area > 80 or defect_location == "center":
        grade = "특별주의"
    elif total_score < 100:
        grade = "정상"
    elif total_score < 150:
        grade = "주의"
    else:
        grade = "위험"

    return grade


# 웨이퍼 등록 함수
def add_wafer():
    global wafer_count

    print("\n[웨이퍼 등록]")

    wafer_id = input("웨이퍼 번호: ")
    process_name = input("공정명: ")
    defect_count = int(input("결함 개수: "))
    defect_area = float(input("결함 면적: "))
    defect_location = input("결함 위치(center/edge/other): ")

    total_score = calculate_score(defect_count, defect_area, defect_location)
    grade = judge_grade(defect_count, defect_area, defect_location, total_score)

    wafer = [
        wafer_id,
        process_name,
        defect_count,
        defect_area,
        defect_location,
        total_score,
        grade
    ]

    wafer_list.append(wafer)
    wafer_count += 1

    print("\n웨이퍼 등록 완료")
    print(f"현재 등록된 웨이퍼 개수: {wafer_count}개")


# 전체 웨이퍼 조회 함수
def show_all_wafers():
    print("\n[전체 웨이퍼 조회]")

    if len(wafer_list) == 0:
        print("등록된 웨이퍼가 없습니다.")
    else:
        for wafer in wafer_list:
            print("--------------------")
            print(f"웨이퍼 번호: {wafer[0]}")
            print(f"공정명: {wafer[1]}")
            print(f"결함 개수: {wafer[2]}")
            print(f"결함 면적: {wafer[3]}")
            print(f"결함 위치: {wafer[4]}")
            print(f"결함 점수: {wafer[5]}")
            print(f"상태: {wafer[6]}")


# 평균 결함 점수 계산 함수
def calculate_average():
    total = 0

    for wafer in wafer_list:
        total = total + wafer[5]

    average = total / len(wafer_list)

    return average


# 평균 결함 점수 출력 함수
def show_average_score():
    print("\n[평균 결함 점수 확인]")

    if len(wafer_list) == 0:
        print("등록된 웨이퍼가 없어 평균을 계산할 수 없습니다.")
    else:
        average = calculate_average()
        print(f"평균 결함 점수: {average:.2f}점")


# 위험 웨이퍼 찾기 함수
def find_danger_wafer():
    print("\n[위험 웨이퍼 찾기]")

    if len(wafer_list) == 0:
        print("등록된 웨이퍼가 없습니다.")
    else:
        danger_wafer = wafer_list[0]

        for wafer in wafer_list:
            if wafer[5] > danger_wafer[5]:
                danger_wafer = wafer

        print("가장 위험한 웨이퍼")
        print(f"웨이퍼 번호: {danger_wafer[0]}")
        print(f"공정명: {danger_wafer[1]}")
        print(f"결함 점수: {danger_wafer[5]}")
        print(f"상태: {danger_wafer[6]}")


# 메인 함수
def main():
    while True:
        print_menu()

        menu = input("메뉴 선택: ")

        if menu == "1":
            add_wafer()
        elif menu == "2":
            show_all_wafers()
        elif menu == "3":
            show_average_score()
        elif menu == "4":
            find_danger_wafer()
        elif menu == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다. 다시 선택하세요.")


# 프로그램 시작
main()
