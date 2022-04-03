<template>
  <v-app
  >
    <v-data-table
      v-model="selected"
      class="elevation-1 "
      :headers="headers"

      :items="foodDataList"

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
      <!-- <template v-slot:expanded-item="{ headers, item }">
        <td :colspan="headers.length">
          {{ item.foodName }}사진
        </td>
      </template> -->
    </v-data-table>
    <div class="text-center pt-2">
      <button class="bttn-success bttn-unite mr-5" @click="saveMyMenus">선택음식 식단에 저장</button>
      <button class="bttn-success bttn-unite" >음식 추가하러가기</button>
    </div>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex';
import axios from 'axios';
export default {
  name: 'BasketFoodList',
  data () {
    return {
      today: new Date(),
      sendData: {
        menus:[],
      },
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
        { text: '1회 제공량(g)',  align:'end', value: 'servingSize', sortable: false, },
        { text: '1회 당 열량(kcal)', align:'end',  value: 'foodKcal' },
        { text: '당류(g)', align:'end',  value: 'sugar' },
        { text: '탄수화물(g)', align:'end',  value: 'carbohydrate' },
        { text: '단백질(g)', align:'end',  value: 'protein' },
        { text: '지방(g)', align:'end',  value: 'fat' },
        { text: '콜레스테롤(mg)',align:'end',  value: 'cholesterol' },
        { text: '총 포화지방산(g)', align:'end',  value: 'fattyAcid' },
        { text: '장바구니에서 삭제', align: 'end', value: 'actions', sortable: false },
      ],
    }
  },
  methods: {
    ...mapActions([
      'myMenuUpdate',
      'menusUpdate'
    ]),
    // 칼로리 위험도를 제공하기 위해 1회 당 500kcal이 넘는다면 위험, 300kcal이 넘는다면 경고, 300kcal 이하는 적합
    getColor (calories) {
      if (calories > 500) return 'red'
      else if (calories > 300) return 'orange'
      else return 'green'
    },
    // DB에 식단 저장
    saveMyMenus() {
      this.selected.forEach(food => {
        this.sendData.menus.push(
          { foodId: food.id, amount: 1 }
        )
      })
      this.sendData.dateTime = `${this.today.getFullYear()}-0${this.today.getMonth()+1}-${this.today.getDate()}`;
      this.sendData.mealTime = this.$store.state.mealTime;
      this.sendData.username = this.userInfo.username
      // console.log(this.sendData)
      axios({
        method: 'post',
        url: `${process.env.VUE_APP_API_URL}/menu/basket/`,
        data: this.sendData,
        headers: {
          Authorization : `JWT ${this.userToken}`
        }
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 삭제버튼 클릭시
    deleteItem (item) {
      // 선택한 아이템의 index 저장
      this.editedIndex = this.myMenu.indexOf(item)
      this.dialogDelete = true
    },

    // 삭제 모달 확인버튼 클릭시
    deleteItemConfirm () {
      this.myMenu.splice(this.editedIndex, 1)
      this.closeDelete()
      this.menusUpdate(this.myMenu)
    },

    // 취소버튼클릭시
    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

  },
  mounted(){
  },
  computed: {
    // store에 저장된 장바구니정보
    foodDataList() { return this.$store.state.menus },
    // 유저정보
    userInfo() { return this.$store.getters.getUserInfo },
    // API 요청을 위한 JWT
    userToken() { return this.$store.getters.getUserToken },
  },
}
</script>

<style scoped>
.save-btn {
  width: 20vw;
}
</style>