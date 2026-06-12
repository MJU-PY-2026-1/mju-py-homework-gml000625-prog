# 파일이름 : main.py
# 작성자 : 이찬희
# 프로그램명 : 웨이퍼 결함 분석 시스템 V4.0

wafer_list = []
wafer_count = 0
FILE_NAME = "wafer_data.txt"


def print_menu():
    print("\n===== 웨이퍼 결함 분석 관리 시스템 V4.0 =====")
    print("1. 웨이퍼 등록")
    print("2. 전체 웨이퍼 조회")
    print("3. 평균 결함 점수 확인")
    print("4. 위험 웨이퍼 찾기")
    print("5. 웨이퍼 검색")
    print("6. 파일 저장")
    print("7. 파일 불러오기")
    print("0. 프로그램 종료")


def calculate_score(defect_count, defect_area, defect_location):
    count_score = defect_count * 10

    if defect_area < 10:
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

    return count_score + area_score + location_score


def judge_grade(defect_count, defect_area, defect_location, total_score):
    if defect_count >= 10 and defect_location == "center":
        return "긴급위험"
    elif defect_area > 80 or defect_location == "center":
        return "특별주의"
    elif total_score < 100:
        return "정상"
    elif total_score < 150:
        return "주의"
    else:
        return "위험"


def add_wafer():
    global wafer_count

    try:
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

        print(f"\n{wafer_id} 웨이퍼 등록 완료")
        print(f"결함 점수: {total_score}")
        print(f"상태: {grade}")

    except ValueError:
        print("입력 오류: 결함 개수는 정수, 결함 면적은 숫자로 입력하세요.")


def show_all_wafers():
    if len(wafer_list) == 0:
        print("등록된 웨이퍼가 없습니다.")
        return

    labels = ["웨이퍼 번호", "공정명", "결함 개수", "결함 면적", "결함 위치", "결함 점수", "상태"]

    for i in range(len(wafer_list)):
        print("\n------------------------------")
        print(f"[{i + 1}번 웨이퍼]")

        for j in range(len(labels)):
            print(f"{labels[j]}: {wafer_list[i][j]}")


def calculate_average():
    if len(wafer_list) == 0:
        return 0

    total = 0

    for wafer in wafer_list:
        total += wafer[5]

    return total / len(wafer_list)


def show_average_score():
    if len(wafer_list) == 0:
        print("등록된 웨이퍼가 없습니다.")
        return

    average = calculate_average()
    print(f"전체 웨이퍼 평균 결함 점수: {average:.2f}")


def find_danger_wafer():
    if len(wafer_list) == 0:
        print("등록된 웨이퍼가 없습니다.")
        return

    found = False

    for wafer in wafer_list:
        if "위험" in wafer[6]:
            print(f"웨이퍼 번호: {wafer[0]}, 공정명: {wafer[1]}, 점수: {wafer[5]}, 상태: {wafer[6]}")
            found = True

    if found == False:
        print("위험 판정을 받은 웨이퍼가 없습니다.")


def search_wafer():
    search_id = input("검색할 웨이퍼 번호: ")

    for wafer in wafer_list:
        if wafer[0] == search_id:
            print("\n[검색 결과]")
            print(f"웨이퍼 번호: {wafer[0]}")
            print(f"공정명: {wafer[1]}")
            print(f"결함 개수: {wafer[2]}")
            print(f"결함 면적: {wafer[3]}")
            print(f"결함 위치: {wafer[4]}")
            print(f"결함 점수: {wafer[5]}")
            print(f"상태: {wafer[6]}")
            return

    print("해당 웨이퍼를 찾을 수 없습니다.")


def save_file():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for wafer in wafer_list:
                file.write(f"{wafer[0]},{wafer[1]},{wafer[2]},{wafer[3]},{wafer[4]},{wafer[5]},{wafer[6]}\n")

        print(f"{FILE_NAME} 파일 저장 완료")

    except:
        print("파일 저장 중 오류가 발생했습니다.")


def load_file():
    global wafer_list
    global wafer_count

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        loaded_list = []

        for line in lines:
            data = line.strip().split(",")

            wafer = [
                data[0],
                data[1],
                int(data[2]),
                float(data[3]),
                data[4],
                int(data[5]),
                data[6]
            ]

            loaded_list.append(wafer)

        wafer_list = loaded_list
        wafer_count = len(wafer_list)

        print(f"{FILE_NAME} 파일에서 {wafer_count}개 데이터를 불러왔습니다.")

    except FileNotFoundError:
        print("저장된 파일이 없습니다. 먼저 파일 저장을 해주세요.")
    except ValueError:
        print("파일 안의 숫자 데이터 형식이 올바르지 않습니다.")
    except IndexError:
        print("파일 안의 데이터 항목 수가 올바르지 않습니다.")


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
        elif menu == "5":
            search_wafer()
        elif menu == "6":
            save_file()
        elif menu == "7":
            load_file()
        elif menu == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")


main()