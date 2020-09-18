<template>
  <v-chip-group>
    <v-card-text>
      <v-chip v-for="category in categoryList" v-bind:key="category.id">
        {{ category.name }}
      </v-chip>
    </v-card-text>
  </v-chip-group>
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
