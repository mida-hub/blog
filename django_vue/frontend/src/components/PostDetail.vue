<template>
  <v-container fluid>
    <v-row>
      <v-card outlined width="100%">
        <div v-if="isNotDisplay">
          <v-card-title>
            This request is invalid.
          </v-card-title>
        </div>
        <div v-else>
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
            <div v-html="postDetail.decoded_content"></div>
          </v-card-text>
        </div>
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
        isNotDisplay: false
      }
    },
    methods: {
      forceRedirect: function () {
        setTimeout(function () {
              location.href = '/'
            }, 1000);
      }
    },
    created: function () {
      console.log('post mounted')
      const postId = this.$route.params.postId
      axios.get(this.$apiPath + '/posts/' + postId + '/')
        .then((response) => {
          this.postDetail = response.data
          if ( !this.postDetail.is_display ) {
            this.isNotDisplay = true
            // 非公開のため1秒後にリダイレクト
            this.forceRedirect()
          }
        })
        .catch((error) => {
          console.log(error)
          this.isNotDisplay = true
          // Not Found のため1秒後にリダイレクト
          this.forceRedirect()
        })
    },
  }
</script>

<style scoped>
  /* @import '../statics/dark.css'; */

  .detail-right{
    text-align: right;
  }
</style>

<style>
  img {
    max-width: 100%;
    height: auto;
  }

</style>
