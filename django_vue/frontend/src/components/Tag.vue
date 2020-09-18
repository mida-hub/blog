<template>
  <v-container fluid>
    <v-layout column>
      <v-card outlined color="white">
        <div class="headline">
          <v-card-title>
            タグ
          </v-card-title>
        </div>
        <div v-for="tag in tagList" v-bind:key="tag.id">
          <v-card-text>
            {{ tag.name }}
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
        tagList: []
      }
    },
    mounted: function () {
      console.log('mounted')
      axios.get('/blog/tags/')
        .then((response) => {
          this.tagList = response.data
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
