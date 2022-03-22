from openpyxl import Workbook, load_workbook
from menus.serializers import FoodSerializer
# openpyxl 설치
# pip install openpyxl

def main():
    print("db_uploader")
    load_wb = load_workbook(filename='datas/통합 식품영양성분DB_음식_20220308.xlsx', data_only=True)
    # 시트명 출력
    sheets = load_wb.sheetnames

    # 시트 이름으로 불러오기
    load_ws = load_wb['Data']

    # 엑셀 파일의 필요 속성 13개
    xls_properties = ["NO", "상용제품", "식품명", "식품대분류", "식품상세분류", "1회제공량", "에너지(㎉)", "총당류(g)", "탄수화물(g)", "단백질(g)"
    , "지방(g)", "콜레스테롤(㎎)", "총 포화 지방산(g)"]

    # Food 테이블의 13개 속성 중 image를 제외한 12가지 매칭 + 품목대표인지 확인을 위해 "상용제품" 속성 추가 필요 -> "상용제품" : commercialFood
    table_properties = {"NO" : "id", "상용제품" : "commercialFood", "식품명" : "foodName", "식품대분류" : "foodCategory", "식품상세분류" : "foodDetailCategory"
    , "1회제공량" : "servingSize", "에너지(㎉)" : "foodKcal", "총당류(g)" : "sugar", "탄수화물(g)" : "carbohydrate"
    , "단백질(g)" : "protein", "지방(g)" : "fat", "콜레스테롤(㎎)" : "cholesterol", "총 포화 지방산(g)" : "fattyAcid"}
    
    # 엑셀 속성의 컬럼 index와 속성명을 매칭
    xls_index_to_values = {}

    for tuples in load_ws['4']:
        # print(tuples.row, tuples.column, tuples.value)
        if tuples.value in xls_properties:
            xls_index_to_values[tuples.column] = tuples.value

    # 모든 음식 데이터 저장
    # all_foods = []

    serializer = FoodSerializer(data=food)

    for row in load_ws.rows:
        if row[0].row < 5: continue;
        food = {}
        for cell in row:
            if cell.column in xls_index_to_values.keys():
                food[table_properties[xls_index_to_values[cell.column]]] = cell.value
        print(food)
        if serializer.is_valid(raise_exception=True):
            serializer.save(food=food)
        break
        # all_foods.append(food)
    # print(all_foods)

        


if __name__ == '__main__':
    main()
