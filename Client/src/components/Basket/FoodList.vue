<template>
  <v-app
  >
    <v-data-table
      v-model="selected"
      class="elevation-1 "
      :headers="headers"

      :items="myMenu"

      hide-default-footer
      show-select
      :single-select="false"
      item-key="foodName"

    >
    <!-- 장바구니 삭제 -->
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-center">장바구니에서 삭제하시겠어요?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">삭제</v-btn>
                <v-btn color="blue darken-1" text @click="closeDelete">취소</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          small
          @click="deleteItem(item)"
          class="text-h4"
        >
          mdi-delete
        </v-icon>
      </template>
      <!-- 칼로리 숫자 색 -->
      <template v-slot:[`item.foodKcal`]="{ item }">
        <v-chip
          :color="getColor(item.foodKcal)"
          dark
        >
        {{ item.foodKcal}}
        </v-chip>
      </template>
      <!-- 확장(이미지) 등등 -->
      <template v-slot:expanded-item="{ headers, item }">
      <td :colspan="headers.length">
        {{ item.foodName }}사진
      </td>
    </template>
    </v-data-table>
    <div class="text-center pt-2">
      <button class="bttn-success bttn-unite mr-5" @click="test">선택음식 식단에 저장</button>
      <button class="bttn-success bttn-unite mr-5" >음식 추가하러가기</button>
      <button class="bttn-success bttn-unite">식단 저장하기</button>
    </div>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'FoodList',
  data () {
    return {
      dialogDelete: false,
      selected: [],
      expanded: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      headers: [
        { text: '음식이름',  align:'end', value: 'foodName', sortable: true, },
        { text: '1회 제공량(g)',  align:'end', value: 'foodservingSize', sortable: false, },
        { text: '1회 당 열량(kcal)', align:'end',  value: 'foodKcal' },
        { text: '당류(g)', align:'end',  value: 'sugar' },
        { text: '탄수화물(g)', align:'end',  value: 'carbohydrate' },
        { text: '단백질(g)', align:'end',  value: 'protein' },
        { text: '지방(g)', align:'end',  value: 'fat' },
        { text: '콜레스테롤(mg)',align:'end',  value: 'cholesterol' },
        { text: '총 포화지방산(g)', align:'end',  value: 'fattyAcid' },
        { text: '장바구니에서 삭제', align: 'end', value: 'actions', sortable: false },
      ],
      myMenu: [
      {
        dateTime: '',
        mealTime: 1,
        amount: 1,
        foodName: '흰 쌀밥',
        foodCategory: '탄수화물류',
        foodDetailCategory: '밥',
        foodservingSize: 200,
        foodKcal: 100,
        sugar: 3.5,
        carbohydrate: 2,
        protein: 5,
        fat: 6,
        cholesterol: 2,
        fattyAcid: 1,
      },
      {
        dateTime: '',
        mealTime: 1,
        amount: 1,
        foodName: '배추김치',
        foodCategory: '김치류',
        foodDetailCategory: '배추김치류',
        foodservingSize: 300,
        foodKcal: 30,
        sugar: 1,
        carbohydrate: 2,
        protein: 3,
        fat: 4,
        cholesterol: 5,
        fattyAcid: 6,
      },
      {
        dateTime: '',
        mealTime: 1,
        amount: 1,
        foodName: '소고기무국',
        foodCategory: '국류',
        foodDetailCategory: '소고기무국류',
        foodservingSize: 200,
        foodKcal: 230,
        sugar: 2,
        carbohydrate: 3.4,
        protein: 5.2,
        fat: 6.2,
        cholesterol: 1.4,
        fattyAcid: 3.5,
      },
    ],
    }
  },
  methods: {
    ...mapActions([
      'myMenuUpdate'
    ]),
    // 칼로리 위험도를 제공하기 위해 1회 당 500kcal이 넘는다면 위험, 300kcal이 넘는다면 경고, 300kcal 이하는 적합
    getColor (calories) {
      if (calories > 500) return 'red'
      else if (calories > 300) return 'orange'
      else return 'green'
    },
    test() {
      console.log(this.myMenu === this.selected)
      // this.myMenu.forEach(food => {
      //   console.log(food)
      // })
    },
    // 삭제버튼 클릭시
    deleteItem (item) {
      // 선택한 아이템의 index 저장
      this.editedIndex = this.myMenu.indexOf(item)
      // this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    // 삭제 모달 확인버튼 클릭시
    deleteItemConfirm () {
      this.myMenu.splice(this.editedIndex, 1)
      this.closeDelete()
      console.log(this.myMenu)
    },

    // 취소버튼클릭시
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    // 취소버튼클릭시
    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.myMenu[this.editedIndex], this.editedItem)
      } else {
        this.myMenu.push(this.editedItem)
      }
      this.close()
    },
  },
  mounted(){
    this.myMenuUpdate()
  },
  computed: {
    // store에 저장된 장바구니정보
    foodDataList() { return this.$store.getters.getMyMenu },
  },
  watch: {
    selected() { console.log(this.selected) }
  }
}
</script>

<style scoped>
.save-btn {
  /* position: fixed; */
  width: 20vw;
  /* bottom: 10vh; */
  /* left: 50%; */
  /* transform: translateX(-50%); */
}
</style>