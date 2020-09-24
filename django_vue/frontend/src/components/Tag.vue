<template>
  <v-chip-group column>
    <v-card-text>
      <v-chip label @click="tagFilter(tag.id)" v-for="tag in tagList" v-bind:key="tag.id">
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
      axios.get(this.$apiPath + '/tags/')
        .then((response) => {
          this.tagList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    methods: {
      tagFilter: function ( tagId ) {
        // tagId が取れて、同じ遷移先の場合は遷移しない
        if ( Object.keys(this.$route.params).length ) {
          if ( tagId === this.$route.params.tagId ) {
            return
          }
        }
        this.$router.push({ name: 'tagFilter', params: { tagId: tagId } })
      }
    }
  }
</script>

<style scoped>
</style>
