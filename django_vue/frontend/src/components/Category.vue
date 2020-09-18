<template>
  <v-container fluid>
    <v-layout column>
      <v-card outlined color="white">
        <div class="headline">
          <v-card-title>
            カテゴリ
          </v-card-title>
        </div>
        <div v-for="category in categoryList" v-bind:key="category.id">
          <v-card-text>
            {{ category.name }}
          </v-card-text>
        </div>
      </v-card>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        categoryList: []
      }
    },
    mounted: function () {
      console.log('mounted')
      axios.get('/blog/categories/')
        .then((response) => {
          this.categoryList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
  @import '../statics/style.css';
</style>
