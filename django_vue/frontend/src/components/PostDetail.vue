<template>
  <v-container fluid>
    <v-row>
      <v-card outlined width="100%">
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
      const postId = this.$route.params.postId
      axios.get('/blog-api/post/' + postId)
        .then((response) => {
          this.postDetail = response.data
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
