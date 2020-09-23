<template>
  <v-container fluid>
    <v-row>
      <v-card outlined width="100%">
        <div v-if="isError">
          <v-card-title>
            /posts/{{ this.$route.params.postId }} is not exist.
          </v-card-title>
        </div>
        <v-card-title>
          <span class="headline">{{ postDetail.title }}</span>
        </v-card-title>
        <v-card-subtitle style="color: rgba(0, 0, 0, 0.87);">
          <p>
            <small>
              {{ postDetail.formatted_published_at }}
            </small>
          </p>
        <p>
          <small v-for="tag in postDetail.tags" v-bind:key="tag.id">
            [{{ tag.name }}]
          </small>
        </p>
        </v-card-subtitle>
        <v-card-text style="color: rgba(0, 0, 0, 0.87);">
          <span v-html="postDetail.decoded_content"></span>
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
        postDetail: [],
        isError: false
      }
    },
    created: function () {
      console.log('post mounted')
      const postId = this.$route.params.postId
      axios.get('/blog-api/posts/' + postId)
        .then((response) => {
          this.postDetail = response.data
        })
        .catch((error) => {
          console.log(error)
          this.isError = true
          // 不正なアクセスのため1秒後にリダイレクト
          setTimeout(function () {
            location.href = '/'
          }, 1000);
        })
    },
  }
</script>

<style scoped>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/a11y-dark.min.css">
  .detail-right{
    text-align: right;
  }
</style>
