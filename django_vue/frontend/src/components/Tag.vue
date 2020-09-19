<template>
  <v-chip-group column>
    <v-card-text>
      <v-chip v-for="tag in tagList" v-bind:key="tag.id">
        {{ tag.name }}
      </v-chip>
    </v-card-text>
  </v-chip-group>
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
      console.log('tag mounted')
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
