<template>
  <v-container fluid>
    <div v-for="post in postList" v-bind:key="post.id">
      <div v-if="isDisplay(post.is_public, post.published_at)">
        <v-row>
          <v-card-title>
            <span class="headline">
              <router-link
                v-bind:to="{name: 'postDetail', params: {postId: post.id}}"
                class="post-link"
              >
                {{ post.title }}  
              </router-link>
            </span>
          </v-card-title>
          <v-card-text>
            {{ post.summarized_content }}
          </v-card-text>
          <v-card-subtitle>
            <p>
              <small>
                {{ post.formatted_published_at }}
              </small>
              <small v-for="tag in post.tags" v-bind:key="tag.id">
                [{{ tag.name }}]
              </small>
            </p>
          </v-card-subtitle>
        </v-row>
        <v-divider></v-divider>
      </div>
    </div>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import moment from "moment"

  export default {
    data () {
      return {
        postList: []
      }
    },
    created: function () {
      console.log('post mounted')
      axios.get('/blog-api/posts/')
        .then((response) => {
          this.postList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    computed: {
      /**
       * 公開フラグ & 公開日付が現在日付より過去になった場合に表示する
       * @param {bool} is_public    - 公開フラグ
       * @param {Date} published_at - 公開日付
       */
      isDisplay: function () {
        return function (is_public, published_at) {
          const formated_published_at = moment(published_at, 'YYYY-MM-DD HH:mm')
          const formated_current_at = moment(new Date(), 'YYYY-MM-DD HH:mm')
          
          if (is_public && formated_published_at <= formated_current_at) {
            return true
          } else {
            return false
          }
        }
      }
    }
  }
</script>

<style scoped>
  .post-link {
    text-decoration: none;
    color: inherit;
  }
  .post-link:hover{
    padding-bottom: 3px;
    border-bottom: 1px solid;
    color: dimgray;
  }
</style>
