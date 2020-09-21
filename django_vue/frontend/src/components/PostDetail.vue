<template>
  <v-container fluid>
    <v-row>
      <v-card outlined>
        <v-card-title>
          <span class="headline">{{ postDetail.title }}</span>
        </v-card-title>
        <v-card-subtitle style="color: rgba(0, 0, 0, 0.87);">
          <p>
            <small>
              {{ postDetail.published_at }}
            </small>
          </p>
        <p>
          <small v-for="tag in postDetail.tags" v-bind:key="tag">
            [{{ tag }}]
          </small>
        </p>
        </v-card-subtitle>
        <v-card-text style="color: rgba(0, 0, 0, 0.87);">
          {{ postDetail.content }}
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        postDetail: []
      }
    },
    created: function () {
      console.log('post mounted')
      axios.get('/blog/posts/')
        .then((response) => {
          const postList = response.data
          console.log(postList[0])
          this.postDetail = postList[0]
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
</script>

<style scoped>
  .detail-right{
    text-align: right;
  }
</style>
